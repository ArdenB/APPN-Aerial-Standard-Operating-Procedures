#!/usr/bin/env python3
"""Convert .docx files to Markdown using Mammoth.

Each input .docx produces a .md file plus an adjacent ``<name>_media/``
directory containing any embedded images, which are referenced from the
Markdown using relative paths.

Usage:
    python docx_to_markdown.py [INPUT ...] [-o OUTPUT_DIR]

If no INPUT paths are given, every .docx under ../OriginalDocuments
(relative to this script) is converted. INPUT may be a file or directory.

Requires: mammoth  (pip install mammoth)
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import mammoth
except ImportError:
    sys.exit("mammoth is required. Install with: pip install mammoth")


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DEFAULT_INPUT = REPO_ROOT / "OriginalDocuments"


def collect_docx(paths: list[Path]) -> list[Path]:
    found: list[Path] = []
    for p in paths:
        if p.is_dir():
            found.extend(sorted(p.rglob("*.docx")))
        elif p.suffix.lower() == ".docx" and p.is_file():
            found.append(p)
        else:
            print(f"skip (not a .docx or directory): {p}", file=sys.stderr)
    # Drop Word lock/temp files like ~$foo.docx
    return [p for p in found if not p.name.startswith("~$")]


def make_image_handler(media_dir: Path, md_path: Path):
    """Return a mammoth image converter that writes images to media_dir."""
    media_dir.mkdir(parents=True, exist_ok=True)
    seen: dict[str, str] = {}

    def convert_image(image):
        with image.open() as stream:
            data = stream.read()
        digest = hashlib.sha1(data).hexdigest()[:12]
        if digest in seen:
            rel = seen[digest]
        else:
            ext = (image.content_type or "").split("/")[-1] or "bin"
            ext = {"jpeg": "jpg", "x-emf": "emf", "x-wmf": "wmf"}.get(ext, ext)
            filename = f"image_{digest}.{ext}"
            (media_dir / filename).write_bytes(data)
            rel = f"{media_dir.name}/{filename}"
            # Browsers don't render EMF; convert to SVG if a converter is available.
            if ext == "emf" and shutil.which("emf2svg-conv"):
                svg_name = f"image_{digest}.svg"
                svg_path = media_dir / svg_name
                try:
                    subprocess.run(
                        ["emf2svg-conv", "-i", str(media_dir / filename),
                         "-o", str(svg_path)],
                        check=True, capture_output=True,
                    )
                    rel = f"{media_dir.name}/{svg_name}"
                except subprocess.CalledProcessError as exc:
                    print(f"  emf2svg-conv failed for {filename}: "
                          f"{exc.stderr.decode(errors='replace').strip()}",
                          file=sys.stderr)
            seen[digest] = rel
        alt = image.alt_text or ""
        return {"src": rel, "alt": alt}

    return mammoth.images.img_element(convert_image)


# Punctuation that mammoth likes to backslash-escape but doesn't need to be.
_UNESCAPE_RE = re.compile(r"\\([.()!:#/\-+=,;?'\"])")
# Convert __bold__ runs to **bold** for broader Markdown compatibility.
_BOLD_RE = re.compile(r"__([^_\n]+)__")
# Collapse "*foo *__*bar*__* baz*" mash-ups into "*foo* **bar** *baz*".
_BOLD_INSIDE_ITALIC_RE = re.compile(r"\*__\*([^*]+)\*__\*")


def clean_markdown(text: str) -> str:
    text = _BOLD_INSIDE_ITALIC_RE.sub(r"** \1 **", text)
    text = _BOLD_RE.sub(r"**\1**", text)
    text = _UNESCAPE_RE.sub(r"\1", text)
    # Strip trailing whitespace on each line and collapse 3+ blank lines.
    text = "\n".join(line.rstrip() for line in text.splitlines())
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert_one(docx: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / (docx.stem + ".md")
    media_dir = out_dir / (docx.stem + "_media")

    with docx.open("rb") as f:
        result = mammoth.convert_to_markdown(
            f,
            convert_image=make_image_handler(media_dir, md_path),
        )

    md_path.write_text(clean_markdown(result.value), encoding="utf-8")

    # Remove media dir if nothing was extracted
    if media_dir.exists() and not any(media_dir.iterdir()):
        media_dir.rmdir()

    for msg in result.messages:
        print(f"  [{msg.type}] {msg.message}", file=sys.stderr)

    return md_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0]) # type: ignore
    parser.add_argument(
        "inputs",
        nargs="*",
        type=Path,
        help="docx files or directories to convert (default: OriginalDocuments/)",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="output directory (default: alongside each .docx)",
    )
    args = parser.parse_args()

    inputs = args.inputs or [DEFAULT_INPUT]
    docs = collect_docx(inputs)
    if not docs:
        print("No .docx files found.", file=sys.stderr)
        return 1

    for docx in docs:
        out_dir = args.output if args.output else docx.parent
        print(f"Converting {docx} -> {out_dir}/{docx.stem}.md")
        convert_one(docx, out_dir)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
