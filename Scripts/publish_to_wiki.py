#!/usr/bin/env python3
"""Publish the locked revision of the SOPs from this repo to the GitHub wiki.

Usage:
    python Scripts/publish_to_wiki.py [--pdf] [--wiki-path PATH]
                                       [--manifest publish.yaml] [--dry-run]

Reads the manifest (default: ``publish.yaml`` at the repo root), and for each
listed page:

* Copies the source ``.md`` into the wiki working tree at
  ``<wiki>/<wiki_page>.md``.
* Injects a "Locked revision" banner directly under the H1 title.
* Rewrites image references that point at ``*_media/...`` to
  ``media/<wiki_page>/...``.
* Copies the matching ``*_media/`` directory into ``<wiki>/media/<wiki_page>/``.

It also regenerates ``Home.md`` and ``_Sidebar.md`` from the manifest, grouping
pages by category.

With ``--pdf``, each manifest page is also rendered to
``releases/Rev<revision>/<wiki_page>.pdf`` via ``pandoc`` (must be on PATH).

With ``--dry-run``, nothing is written or copied; planned actions are printed.

Requires:
    pyyaml  (pip install pyyaml)
Optional:
    pandoc + a PDF engine (e.g. xelatex, wkhtmltopdf, weasyprint) for --pdf.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.exit("pyyaml is required. Install with: pip install pyyaml")


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_MANIFEST = REPO_ROOT / "publish.yaml"
DEFAULT_WIKI_PATH = REPO_ROOT.parent / f"{REPO_ROOT.name}.wiki"

# Static wiki assets injected into the published wiki.
# - Home intro lives under Protocols/ so it's easy for editors to find.
# - Footer template lives next to the publish script.
WIKI_ASSETS_DIR = SCRIPT_DIR / "wiki_assets"
HOME_INTRO_FILE = REPO_ROOT / "Protocols" / "Home" / "Home_Intro.md"
FOOTER_FILE = WIKI_ASSETS_DIR / "_Footer.md"

# Pandoc assets used when rendering PDFs.
PANDOC_ASSETS_DIR = SCRIPT_DIR / "pandoc"
GFM_ALERTS_FILTER = PANDOC_ASSETS_DIR / "gfm-alerts.lua"
# Assigns relative column widths to every Table so the LaTeX writer emits
# wrapping `p{...}` columns instead of overflowing `l` columns.
TABLE_WIDTHS_FILTER = PANDOC_ASSETS_DIR / "table-widths.lua"
LATEX_HEADER = PANDOC_ASSETS_DIR / "header.tex"
# Extra header included only for standalone checklist PDFs to tighten the
# title block so the heading fits on the first page.
LATEX_CHECKLIST_HEADER = PANDOC_ASSETS_DIR / "checklist-header.tex"

# Matches Markdown image references whose target points into a *_media/ folder
# adjacent to the source file. We only rewrite those — external URLs and other
# relative paths are left alone.
_IMG_RE = re.compile(r"(!\[[^\]]*\]\()([^)\s]*_media/[^)\s]+)(\))")

# Matches Markdown links whose target is a (relative) ``.md`` file, with an
# optional ``#anchor`` fragment. Only non-image links are matched (negative
# lookbehind on ``!``). External URLs and absolute / scheme-prefixed targets
# are left alone by ``rewrite_md_links``.
_MD_LINK_RE = re.compile(
    r"(?<!!)(\[[^\]]*\]\()"   # 1: "[text]("
    r"([^)\s#]+\.md)"          # 2: target .md path (no spaces, no fragment)
    r"(#[^)\s]*)?"              # 3: optional #anchor
    r"(\))"                     # 4: closing ")"
)


# ---------------------------------------------------------------------------
# Field EWG review pipeline
# ---------------------------------------------------------------------------

# Ordered list of (id, label) for the Field EWG review stages each page passes
# through. Page status in the manifest is a list of completed stage IDs.
REVIEW_STAGES: list[tuple[str, str]] = [
    ("drafted", "Drafted"),
    ("ewg_feedback", "EWG feedback"),
    ("modified", "Modified"),
    ("approved", "Approved"),
    ("adopted", "Adopted"),
]
_VALID_STAGE_IDS = {sid for sid, _ in REVIEW_STAGES}

# Where the human-readable tracker mirror lives in the source repo.
STATUS_FILE = REPO_ROOT / "Protocols" / "STATUS.md"

# Wiki page name for the published tracker.
STATUS_WIKI_PAGE = "Status"

# The protocols changelog, also published verbatim to the wiki.
CHANGELOG_FILE = REPO_ROOT / "Protocols" / "CHANGELOG.md"
CHANGELOG_WIKI_PAGE = "Changelog"


def page_status(page: dict[str, Any]) -> list[str]:
    """Return validated, ordered list of completed stage IDs for a page."""
    raw = page.get("status") or []
    if not isinstance(raw, list):
        sys.exit(f"page status must be a list: {page.get('source')}")
    unknown = [s for s in raw if s not in _VALID_STAGE_IDS]
    if unknown:
        sys.exit(f"unknown status stage(s) {unknown!r} on page {page.get('source')}; "
                 f"valid: {sorted(_VALID_STAGE_IDS)}")
    # Preserve canonical stage order regardless of YAML order.
    return [sid for sid, _ in REVIEW_STAGES if sid in raw]


def status_summary(page: dict[str, Any]) -> str:
    """Render a one-line status summary suitable for the per-page banner."""
    completed = set(page_status(page))
    parts = []
    for sid, label in REVIEW_STAGES:
        marker = "✅" if sid in completed else "⬜"
        parts.append(f"{marker} {label}")
    return " · ".join(parts)


def page_last_revised(page: dict[str, Any], manifest: dict[str, Any]) -> str:
    """Return the revision in which this page last changed.

    Reads the page's optional ``last_revised`` field and falls back to the
    manifest-wide ``revision`` when it is missing.
    """
    value = page.get("last_revised")
    if value is None:
        return str(manifest["revision"])
    return str(value)


# Shields.io colours keyed off the most-advanced completed stage. The label
# shown on the badge mirrors that stage; if no stages are complete we show
# "not started" in red.
_STATUS_BADGE_COLORS: dict[str, str] = {
    "drafted":      "orange",
    "ewg_feedback": "yellow",
    "modified":     "yellowgreen",
    "approved":     "blue",
    "adopted":      "brightgreen",
}
_STATUS_BADGE_NONE = ("not started", "red")


def status_badge(page: dict[str, Any]) -> str:
    """Return a shields.io <img>-link describing the page's review status."""
    completed = page_status(page)
    if completed:
        latest = completed[-1]  # canonical order — last == most advanced
        label = dict(REVIEW_STAGES)[latest].lower()
        color = _STATUS_BADGE_COLORS.get(latest, "lightgrey")
    else:
        label, color = _STATUS_BADGE_NONE
    badge_label = label.replace("-", "--").replace("_", "__").replace(" ", "%20")
    url = f"https://img.shields.io/badge/status-{badge_label}-{color}"
    return (
        f'<a href="{STATUS_WIKI_PAGE}">'
        f'<img src="{url}" alt="status: {label}" /></a>'
    )


# ---------------------------------------------------------------------------
# Sensor fieldbook nav-badge strip
# ---------------------------------------------------------------------------


def render_nav_badges(manifest: dict[str, Any], current_wiki_page: str | None = None) -> str:
    """Render the centred shields.io badge strip declared in ``nav_badges``.

    Returns an empty string if no badges are configured. The badge for the
    page currently being rendered (``current_wiki_page``) is shown in a
    muted colour and is not linked, so readers can see where they are.
    """
    badges = manifest.get("nav_badges") or []
    if not badges:
        return ""

    parts = ["<p align=\"center\">"]
    for b in badges:
        wiki_page = b["wiki_page"]
        label = b["label"]
        color = b.get("color", "6f901e")
        # shields.io collapses double underscores; replace them so labels keep
        # their spaces. Spaces become %20 in the badge URL.
        badge_label = label.replace("-", "--").replace("_", "__")
        badge_url = (
            f"https://img.shields.io/badge/"
            f"{badge_label.replace(' ', '%20')}-{color}"
        )
        if wiki_page == current_wiki_page:
            # Muted, non-linked badge for the current page.
            muted = badge_url.replace(f"-{color}", "-555555")
            parts.append(f'  <img src="{muted}" alt="{label} (current)" />')
        else:
            parts.append(
                f'  <a href="{wiki_page}">'
                f'<img src="{badge_url}" alt="{label}" /></a>'
            )
    parts.append("</p>")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Manifest loading
# ---------------------------------------------------------------------------


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.is_file():
        sys.exit(f"manifest not found: {path}")
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        sys.exit(f"manifest root must be a mapping: {path}")
    if "revision" not in data or "pages" not in data:
        sys.exit(f"manifest must define 'revision' and 'pages': {path}")
    return data


# ---------------------------------------------------------------------------
# Markdown transforms
# ---------------------------------------------------------------------------


def rewrite_media(markdown: str, wiki_page: str) -> str:
    """Rewrite ``*_media/foo.png`` image targets to ``media/<wiki_page>/foo.png``."""
    def _sub(m: re.Match[str]) -> str:
        target = m.group(2)
        # Take only the trailing filename component.
        filename = target.rsplit("/", 1)[-1]
        return f"{m.group(1)}media/{wiki_page}/{filename}{m.group(3)}"
    return _IMG_RE.sub(_sub, markdown)


def build_slug_map(manifest: dict[str, Any]) -> dict[Path, str]:
    """Map each manifest page's resolved source path to its wiki slug.

    Used by :func:`rewrite_md_links` to turn relative cross-document
    ``.md`` links in the source repo into wiki-style links that resolve
    inside the published wiki (where every page is flat at the root).
    """
    slug_map: dict[Path, str] = {}
    for page in manifest.get("pages", []):
        try:
            src = (REPO_ROOT / page["source"]).resolve()
        except (OSError, RuntimeError):
            # Source file may be missing on disk; let publish_page report it
            # later when it actually tries to read the file.
            src = (REPO_ROOT / page["source"])
        slug_map[src] = page["wiki_page"]
    return slug_map


def rewrite_md_links(markdown: str, source_path: Path,
                     slug_map: dict[Path, str]) -> str:
    """Rewrite relative ``.md`` cross-document links to wiki page slugs.

    A link target like ``../../FlightDesign/StandardFlight/Standard_Flight.md``
    (optionally with a ``#anchor``) is resolved relative to ``source_path``
    and looked up in ``slug_map``. On a hit, the target is replaced with
    ``<wiki_page>[#anchor]`` so the link works on the GitHub wiki, where
    every published page lives flat at the wiki root.

    External links (``http://``, ``https://``, ``mailto:``, etc.), absolute
    paths, and ``.md`` targets that are not in the manifest are left
    untouched; the latter case prints a warning so missing manifest entries
    are easy to spot during a publish run.
    """
    source_dir = source_path.parent

    def _sub(m: re.Match[str]) -> str:
        prefix, target, anchor, suffix = m.group(1), m.group(2), m.group(3) or "", m.group(4)
        # Skip anything that looks like an external URL or absolute path.
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("/"):
            return m.group(0)
        try:
            resolved = (source_dir / target).resolve()
        except (OSError, RuntimeError):
            return m.group(0)
        wiki_page = slug_map.get(resolved)
        if wiki_page is None:
            try:
                rel = resolved.relative_to(REPO_ROOT)
            except ValueError:
                rel = resolved
            print(
                f"    warn: unmapped .md link in {source_path.relative_to(REPO_ROOT)}: "
                f"{target}{anchor} -> {rel} (not in publish.yaml)",
                file=sys.stderr,
            )
            return m.group(0)
        return f"{prefix}{wiki_page}{anchor}{suffix}"

    return _MD_LINK_RE.sub(_sub, markdown)


def inject_banner(markdown: str, banner: str) -> str:
    """Insert ``banner`` after the first H1; if no H1, prepend it."""
    lines = markdown.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            # Insert blank line + banner + blank line after the H1.
            insert_at = i + 1
            new_block = ["", banner, ""]
            return "\n".join(lines[:insert_at] + new_block + lines[insert_at:]) + (
                "\n" if markdown.endswith("\n") else ""
            )
    return banner + "\n\n" + markdown


def make_banner(page: dict[str, Any], manifest: dict[str, Any], date: str) -> str:
    revision = manifest["revision"]
    repo_url = manifest.get("repo_url", "").rstrip("/")
    branch = manifest.get("default_branch", "main")
    source = page["source"]
    if repo_url:
        link = f"[main repository]({repo_url}/blob/{branch}/{source})"
    else:
        link = f"`{source}` in the main repository"
    lines = [
        f"> **Locked revision {revision}** — published {date}. "
        f"Edit the working draft in the {link}.",
        ">",
        f"> **This document last changed in revision {page_last_revised(page, manifest)}.**",
        ">",
        f"> **Field EWG review status:** {status_summary(page)} "
        f"&nbsp;·&nbsp; [Full tracker]({STATUS_WIKI_PAGE})",
    ]
    badges = render_nav_badges(manifest, current_wiki_page=page["wiki_page"])
    sbadge = status_badge(page)
    if badges or sbadge:
        lines.append("")
        # Status badge sits on its own centred line above the sensor nav
        # strip so it's immediately visible at the top of the page.
        if sbadge:
            lines.append(f'<p align="center">{sbadge}</p>')
        if badges:
            lines.append(badges)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Page publishing
# ---------------------------------------------------------------------------


def publish_page(page: dict[str, Any], manifest: dict[str, Any], wiki_root: Path,
                 date: str, dry_run: bool,
                 slug_map: dict[Path, str] | None = None) -> None:
    source = REPO_ROOT / page["source"]
    if not source.is_file():
        sys.exit(f"source markdown missing: {source}")

    wiki_page = page["wiki_page"]
    target_md = wiki_root / f"{wiki_page}.md"
    target_media = wiki_root / "media" / wiki_page

    src_media = source.parent / f"{source.stem}_media"

    print(f"  page: {page['source']}  ->  {target_md.relative_to(wiki_root.parent)}")

    text = source.read_text(encoding="utf-8")
    if slug_map is None:
        slug_map = build_slug_map(manifest)
    text = rewrite_md_links(text, source.resolve(), slug_map)
    text = rewrite_media(text, wiki_page)
    text = inject_banner(text, make_banner(page, manifest, date))

    if dry_run:
        if src_media.is_dir():
            count = sum(1 for _ in src_media.iterdir())
            print(f"    media: {src_media.relative_to(REPO_ROOT)} "
                  f"-> media/{wiki_page}/  ({count} files)")
        return

    target_md.parent.mkdir(parents=True, exist_ok=True)
    target_md.write_text(text, encoding="utf-8")

    # Refresh the per-page media folder so removed images don't linger.
    if target_media.exists():
        shutil.rmtree(target_media)
    if src_media.is_dir():
        shutil.copytree(src_media, target_media)


# ---------------------------------------------------------------------------
# Navigation regeneration
# ---------------------------------------------------------------------------


def render_sidebar(manifest: dict[str, Any], date: str) -> str:
    cats = {c["id"]: c for c in manifest.get("categories", [])}
    by_cat: dict[str, list[dict[str, Any]]] = {}
    for page in manifest["pages"]:
        by_cat.setdefault(page["category"], []).append(page)

    lines = ["## APPN Aerial SOP", "", "- [Home](Home)",
             f"- [Document status]({STATUS_WIKI_PAGE})",
             f"- [Changelog]({CHANGELOG_WIKI_PAGE})", ""]
    # Preserve manifest category order; append any unknown categories at the end.
    ordered = [c for c in cats] + [c for c in by_cat if c not in cats]
    for cat_id in ordered:
        if cat_id not in by_cat:
            continue
        title = cats.get(cat_id, {}).get("title", cat_id)
        lines.append(f"### {title}")
        for page in by_cat[cat_id]:
            lines.append(f"- [{page['title']}]({page['wiki_page']})")
        lines.append("")
    repo_url = manifest.get("repo_url", "").rstrip("/")
    external: list[tuple[str, str]] = []
    if repo_url:
        external.append(("Main repository", repo_url))
    for link in manifest.get("external_links", []) or []:
        label = link.get("label")
        url = link.get("url")
        if label and url:
            external.append((label, url))
    if external:
        lines.append("### External")
        for label, url in external:
            lines.append(f"- [{label}]({url})")
        lines.append("")
    lines.append(f"_Locked revision {manifest['revision']} — {date}_")
    return "\n".join(lines) + "\n"


def render_home(manifest: dict[str, Any], date: str) -> str:
    cats = {c["id"]: c for c in manifest.get("categories", [])}
    by_cat: dict[str, list[dict[str, Any]]] = {}
    for page in manifest["pages"]:
        by_cat.setdefault(page["category"], []).append(page)

    repo_url = manifest.get("repo_url", "").rstrip("/")
    repo_link = repo_url or "the main repository"
    lines = [
        "# APPN Standard Operating Procedures",
        "",
    ]
    badges = render_nav_badges(manifest)
    if badges:
        lines += [badges, ""]
    lines += [
        f"This wiki publishes the **locked revision {manifest['revision']}** "
        f"({date}) of the APPN field SOPs. Working drafts live in the "
        f"[main repository]({repo_link}); pages here are regenerated by "
        "`Scripts/publish_to_wiki.py` whenever a new revision is cut.",
        "",
    ]

    # Optional static intro block (purpose, scope, governance, licensing).
    if HOME_INTRO_FILE.is_file():
        intro = HOME_INTRO_FILE.read_text(encoding="utf-8").rstrip()
        if intro:
            lines.append(intro)
            lines.append("")

    lines.append("## Index")
    lines.append("")
    lines.append(f"- 📋 **[Document review status]({STATUS_WIKI_PAGE})** — "
                 "Field EWG progress tracker for every protocol.")
    lines.append(f"- 📝 **[Changelog]({CHANGELOG_WIKI_PAGE})** — "
                 "notable changes in each revision of the suite.")
    lines.append("")
    ordered = [c for c in cats] + [c for c in by_cat if c not in cats]
    for cat_id in ordered:
        if cat_id not in by_cat:
            continue
        title = cats.get(cat_id, {}).get("title", cat_id)
        lines.append(f"### {title}")
        lines.append("")
        for page in by_cat[cat_id]:
            lines.append(f"- **[{page['title']}]({page['wiki_page']})**")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_navigation(manifest: dict[str, Any], wiki_root: Path, date: str,
                     dry_run: bool) -> None:
    sidebar = render_sidebar(manifest, date)
    home = render_home(manifest, date)
    status_md = render_status(manifest, date, for_wiki=True)
    has_footer = FOOTER_FILE.is_file()
    has_changelog = CHANGELOG_FILE.is_file()
    nav_files = f"Home.md, _Sidebar.md, {STATUS_WIKI_PAGE}.md"
    if has_changelog:
        nav_files += f", {CHANGELOG_WIKI_PAGE}.md"
    if has_footer:
        nav_files += ", _Footer.md"
    print(f"  nav:  {nav_files}")
    print(f"  tracker (repo): {STATUS_FILE.relative_to(REPO_ROOT)}")
    if dry_run:
        return
    (wiki_root / "_Sidebar.md").write_text(sidebar, encoding="utf-8")
    (wiki_root / "Home.md").write_text(home, encoding="utf-8")
    (wiki_root / f"{STATUS_WIKI_PAGE}.md").write_text(status_md, encoding="utf-8")
    if has_changelog:
        changelog = CHANGELOG_FILE.read_text(encoding="utf-8")
        (wiki_root / f"{CHANGELOG_WIKI_PAGE}.md").write_text(
            changelog, encoding="utf-8")
    if has_footer:
        shutil.copyfile(FOOTER_FILE, wiki_root / "_Footer.md")
    # Also refresh the in-repo tracker (without the wiki banner/links).
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.write_text(render_status(manifest, date, for_wiki=False),
                           encoding="utf-8")


def render_status(manifest: dict[str, Any], date: str, *, for_wiki: bool) -> str:
    """Render the Field EWG review-status tracker as a markdown page.

    ``for_wiki=True`` produces the wiki version (links to wiki page names);
    ``for_wiki=False`` produces the in-repo tracker (links to source paths
    relative to the repo root).
    """
    cats = {c["id"]: c for c in manifest.get("categories", [])}
    by_cat: dict[str, list[dict[str, Any]]] = {}
    for page in manifest["pages"]:
        by_cat.setdefault(page["category"], []).append(page)

    lines: list[str] = []
    if for_wiki:
        lines += [
            "# Document Status",
            "",
        ]
        badges = render_nav_badges(manifest)
        if badges:
            lines += [badges, ""]
        lines += [
            f"_Generated from `publish.yaml` on {date} for revision "
            f"{manifest['revision']}._",
            "",
        ]
    else:
        lines += [
            "# Protocol Document Status Tracker",
            "",
            "<!-- AUTO-GENERATED by Scripts/publish_to_wiki.py from publish.yaml. "
            "Do not edit by hand: update each page's `status:` list in "
            "publish.yaml and re-run the publish script. -->",
            "",
            f"_Last regenerated {date} for revision {manifest['revision']}._",
            "",
        ]

    lines += [
        "**Stages**",
        "",
    ]
    for sid, label in REVIEW_STAGES:
        lines.append(f"- **{label}** (`{sid}`)")
    lines += [
        "",
        "Tick = stage complete. Update each page's `status:` list in "
        "[`publish.yaml`](" +
        ("../publish.yaml" if not for_wiki else
         (manifest.get("repo_url", "").rstrip("/") + "/blob/" +
          manifest.get("default_branch", "main") + "/publish.yaml")) +
        ") to advance.",
        "",
    ]

    # Header row.
    headers = ["Document", "Category", "Last revised"]
    if for_wiki:
        headers.append("Status")
    headers += [label for _, label in REVIEW_STAGES] + ["Notes"]
    aligns = ["---", "---", ":---:"]
    if for_wiki:
        aligns.append(":---:")
    aligns += [":---:" for _ in REVIEW_STAGES] + ["---"]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(aligns) + " |")

    ordered_cats = [c for c in cats] + [c for c in by_cat if c not in cats]
    for cat_id in ordered_cats:
        if cat_id not in by_cat:
            continue
        cat_title = cats.get(cat_id, {}).get("title", cat_id)
        for page in by_cat[cat_id]:
            completed = set(page_status(page))
            if for_wiki:
                doc_link = f"[{page['title']}]({page['wiki_page']})"
            else:
                # Path is repo-relative; the tracker lives in Protocols/, so
                # link relative to that.
                rel = page["source"]
                if rel.startswith("Protocols/"):
                    rel = rel[len("Protocols/"):]
                else:
                    rel = "../" + rel
                doc_link = f"[{page['title']}]({rel})"
            row = [doc_link, cat_title, f"`{page_last_revised(page, manifest)}`"]
            if for_wiki:
                row.append(status_badge(page))
            for sid, _ in REVIEW_STAGES:
                row.append("✅" if sid in completed else "⬜")
            row.append(str(page.get("notes", "") or ""))
            lines.append("| " + " | ".join(row) + " |")

    # Summary counts.
    total = len(manifest["pages"])
    counts = {sid: sum(1 for p in manifest["pages"] if sid in page_status(p))
              for sid, _ in REVIEW_STAGES}
    lines += [
        "",
        "## Summary",
        "",
        f"- Documents tracked: **{total}**",
    ]
    for sid, label in REVIEW_STAGES:
        lines.append(f"- {label}: **{counts[sid]} / {total}**")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# PDF rendering (optional)
# ---------------------------------------------------------------------------


# PDF engines pandoc can use, in preference order. The first one available on
# PATH wins; override with --pdf-engine. LaTeX engines come first because they
# give the most polished output (typography, tables, page breaks); HTML-based
# engines are kept as lighter-weight fallbacks.
PDF_ENGINES = ("tectonic", "xelatex", "lualatex", "pdflatex",
               "weasyprint", "wkhtmltopdf", "prince")

# H2 sections whose title matches this regex are also exported as standalone
# checklist PDFs (printable). Case-insensitive.
_CHECKLIST_HEADING_RE = re.compile(r"^##\s+(.*checklists?)\s*$",
                                   re.IGNORECASE | re.MULTILINE)

# Emoji / pictograph codepoint ranges that are not present in the LaTeX
# default fonts (lmroman). We strip them from the markdown before feeding it
# to pandoc for PDF rendering to avoid noisy "Missing character" warnings
# from the TeX engine. The wiki output is left untouched.
_EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"   # Misc symbols & pictographs, emoticons, etc.
    "\U00002600-\U000027BF"   # Misc symbols, dingbats
    "\U0001F000-\U0001F02F"   # Mahjong tiles
    "\U0001F0A0-\U0001F0FF"   # Playing cards
    "\U0001F100-\U0001F1FF"   # Enclosed alphanumerics suppl.
    "\U0001F200-\U0001F2FF"   # Enclosed ideographic suppl.
    "\U0000FE0F"              # Variation selector-16
    "\U0000200D"              # Zero-width joiner
    "]"
)


def _strip_emoji(text: str) -> str:
    """Remove emoji / pictograph characters not covered by LaTeX's default
    fonts. Keeps the surrounding text intact (with any leading whitespace
    collapsed to a single space).
    """
    cleaned = _EMOJI_RE.sub("", text)
    # Collapse any double spaces left behind by removed emoji.
    cleaned = re.sub(r"[ \t]{2,}", " ", cleaned)
    return cleaned


# Tectonic emits a number of chatty but benign warnings on every run that we
# can't reasonably fix in upstream content (PDF version mismatches in embedded
# images, absolute resource paths from pandoc's temp dir, lineno.sty's own
# UTF-8 self-comment, and the trailing "warnings were issued" summary). We
# filter them out of the engine's stderr so the publish output is readable.
_BENIGN_PANDOC_STDERR_RE = re.compile(
    r"^warning: ("
    r"Trying to include PDF file with version"
    r"|accessing absolute path"
    r"|lineno\.sty:296: Invalid UTF-8"
    r"|warnings were issued by the TeX engine"
    r")"
)


def _run_pandoc(cmd: list[str], *, input_text: str | None = None) -> None:
    """Run pandoc and forward its stderr, dropping known-benign tectonic
    warnings. Raises ``subprocess.CalledProcessError`` on non-zero exit.
    """
    proc = subprocess.run(
        cmd,
        input=input_text,
        text=True,
        capture_output=True,
    )
    if proc.stdout:
        sys.stdout.write(proc.stdout)
    for line in proc.stderr.splitlines():
        if _BENIGN_PANDOC_STDERR_RE.match(line):
            continue
        print(line, file=sys.stderr)
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, cmd,
                                            output=proc.stdout,
                                            stderr=proc.stderr)


def detect_pdf_engine() -> str | None:
    for engine in PDF_ENGINES:
        if shutil.which(engine):
            return engine
    return None


def _slugify(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")
    return slug or "section"


def extract_checklist_sections(markdown: str) -> list[tuple[str, str]]:
    """Return a list of (heading_text, section_markdown) pairs for every
    ``## *Checklist*`` H2 in the document. ``section_markdown`` includes the
    H2 line itself and stops at the next H2 (or end of file).
    """
    matches = list(_CHECKLIST_HEADING_RE.finditer(markdown))
    if not matches:
        return []

    sections: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        start = m.start()
        # Find the next H2 (any H2, not just checklist ones) to bound the section.
        next_h2 = re.search(r"^##\s", markdown[m.end():], re.MULTILINE)
        end = m.end() + next_h2.start() if next_h2 else len(markdown)
        sections.append((m.group(1).strip(), markdown[start:end].rstrip() + "\n"))
    return sections


def _pandoc_pdf_cmd(source_arg: str | Path, pdf_path: Path,
                    resource_path: Path, engine: str, title: str,
                    subtitle: str, *, compact_title: bool = False) -> list[str]:
    cmd = [
        "pandoc", str(source_arg),
        "-o", str(pdf_path),
        "--resource-path", str(resource_path),
        "--from=gfm+yaml_metadata_block",
        f"--pdf-engine={engine}",
        "-M", f"title={title}",
        "-M", f"subtitle={subtitle}",
    ]
    if GFM_ALERTS_FILTER.is_file():
        cmd += ["--lua-filter", str(GFM_ALERTS_FILTER)]
    if TABLE_WIDTHS_FILTER.is_file():
        cmd += ["--lua-filter", str(TABLE_WIDTHS_FILTER)]
    # LaTeX engines accept geometry; HTML-based engines ignore it.
    if engine in {"xelatex", "lualatex", "pdflatex", "tectonic"}:
        cmd += ["-V", "geometry:margin=2cm"]
        if LATEX_HEADER.is_file():
            cmd += ["--include-in-header", str(LATEX_HEADER)]
        if compact_title and LATEX_CHECKLIST_HEADER.is_file():
            cmd += ["--include-in-header", str(LATEX_CHECKLIST_HEADER)]
    # Quiet down tectonic's per-page chatter (PDF version notices, absolute
    # path warnings, overfull/underfull \hbox notices that we can't easily
    # fix in upstream content). Errors are still printed.
    if engine == "tectonic":
        cmd += ["--pdf-engine-opt=--chatter=minimal"]
    return cmd


def render_pdfs(manifest: dict[str, Any], dry_run: bool,
                engine: str | None) -> int:
    if not shutil.which("pandoc"):
        print("error: --pdf requires pandoc on PATH", file=sys.stderr)
        return 2

    if engine is None:
        engine = detect_pdf_engine()
    elif not shutil.which(engine):
        print(f"error: --pdf-engine '{engine}' not found on PATH",
              file=sys.stderr)
        return 2

    if engine is None:
        print("error: no PDF engine found. Install one of: "
              + ", ".join(PDF_ENGINES), file=sys.stderr)
        print("       e.g. `pip install weasyprint` (lightest, pure-Python)",
              file=sys.stderr)
        return 2

    revision = manifest["revision"]
    out_dir = REPO_ROOT / "releases" / f"Rev{revision}"
    checklists_dir = out_dir / "checklists"
    print(f"PDF output: {out_dir.relative_to(REPO_ROOT)}/  (engine: {engine})")
    if not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)

    failures = 0
    for page in manifest["pages"]:
        source = REPO_ROOT / page["source"]
        source_md = source.read_text(encoding="utf-8")
        pdf_path = out_dir / f"{page['wiki_page']}.pdf"
        print(f"  pdf:  {page['source']}  ->  {pdf_path.relative_to(REPO_ROOT)}")
        if not dry_run:
            # Pipe the source via stdin (after stripping emoji) instead of
            # passing the file path, so we avoid "Missing character" warnings
            # for codepoints not covered by the default LaTeX fonts.
            cmd = _pandoc_pdf_cmd(
                "-", pdf_path, source.parent, engine,
                title=page["title"],
                subtitle=f"APPN Aerial SOP — Locked revision {revision}",
            )
            try:
                _run_pandoc(cmd, input_text=_strip_emoji(source_md))
            except subprocess.CalledProcessError as exc:
                failures += 1
                print(f"    pandoc failed (exit {exc.returncode})",
                      file=sys.stderr)

        # Split out any "Equipment Checklist"-style sections into standalone
        # printable PDFs alongside the main one.
        sections = extract_checklist_sections(source_md)
        for heading, body in sections:
            slug = _slugify(heading)
            checklist_pdf = checklists_dir / f"{page['wiki_page']}-{slug}.pdf"
            print(f"  pdf:  {page['source']} [{heading}]  ->  "
                  f"{checklist_pdf.relative_to(REPO_ROOT)}")
            if dry_run:
                continue
            checklists_dir.mkdir(parents=True, exist_ok=True)
            # Demote the H2 to H1 so the standalone document has a sensible
            # top-level title.
            body_md = re.sub(r"^##\s+", "# ", body, count=1, flags=re.MULTILINE)
            # Pipe via stdin so we don't have to write a temp file. Pandoc
            # still resolves relative image paths via --resource-path.
            cmd = _pandoc_pdf_cmd(
                "-", checklist_pdf, source.parent, engine,
                title=f"{page['title']} — {heading}",
                subtitle=f"APPN Aerial SOP — Locked revision {revision}",
                compact_title=True,
            )
            try:
                _run_pandoc(cmd, input_text=_strip_emoji(body_md))
            except subprocess.CalledProcessError as exc:
                failures += 1
                print(f"    pandoc failed (exit {exc.returncode})",
                      file=sys.stderr)
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST,
                        help=f"manifest file (default: {DEFAULT_MANIFEST.name})")
    parser.add_argument("--wiki-path", type=Path, default=DEFAULT_WIKI_PATH,
                        help="path to the .wiki working copy "
                             f"(default: {DEFAULT_WIKI_PATH})")
    parser.add_argument("--pdf", action="store_true",
                        help="also render PDFs to releases/Rev<rev>/ via pandoc")
    parser.add_argument("--pdf-engine", default=None,
                        help="override the auto-detected pandoc PDF engine "
                             f"(tries: {', '.join(PDF_ENGINES)})")
    parser.add_argument("--dry-run", action="store_true",
                        help="print planned actions without writing")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)
    wiki_root = args.wiki_path.resolve()
    if not args.dry_run and not wiki_root.is_dir():
        sys.exit(f"wiki path is not a directory: {wiki_root}\n"
                 "Clone the wiki repo next to this one or pass --wiki-path.")

    date = manifest.get("revision_date") or _dt.date.today().isoformat()

    print(f"Manifest: {args.manifest}")
    print(f"Wiki:     {wiki_root}")
    print(f"Revision: {manifest['revision']}  ({date})")
    if args.dry_run:
        print("(dry-run — no files will be written)")
    print()

    print("Pages:")
    slug_map = build_slug_map(manifest)
    for page in manifest["pages"]:
        publish_page(page, manifest, wiki_root, date, args.dry_run, slug_map)

    print()
    print("Navigation:")
    write_navigation(manifest, wiki_root, date, args.dry_run)

    pdf_status = 0
    if args.pdf:
        print()
        pdf_status = render_pdfs(manifest, args.dry_run, args.pdf_engine)

    print()
    print("Done." if pdf_status == 0 else "Done (with PDF errors).")
    return pdf_status


if __name__ == "__main__":
    raise SystemExit(main())
