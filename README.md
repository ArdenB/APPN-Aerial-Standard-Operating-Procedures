> [!CAUTION]
> **This repository is deprecated.** It has been superseded by the official APPN repository: **[APPN-Field-Protocols-and-Pipelines](https://github.com/aus-plant-phenomics-network/APPN-Field-Protocols-and-Pipelines)**. All changes must be made there — this repository is no longer maintained and its content may be out of date.

# APPN Feild Standard Operating Procedures and Pipelines

> [!IMPORTANT]
> **This repository location is temporary.** It is currently hosted under a
> personal GitHub account to support active drafting and review. As individual
> SOPs are finalised and ready for release, they will be migrated to the
> official APPN organisation repository. Please treat URLs, links, and clone
> paths here as **non-permanent** and expect them to change once the migration
> occurs.

Working drafts of the APPN Aerial Standard Operating Procedures (SOPs).

This repository holds the **in-progress** versions of every SOP. The
**locked, published** version of each SOP lives on the
[GitHub Wiki](https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures/wiki).
Edits and revisions happen here; the wiki is regenerated from this repo by a
publish script when a new revision is cut.

## Versioning

The SOPs are versioned as a **single set**. The version combines a **numeric**
major and minor with a **letter** patch suffix, written `MAJOR.YYx` — for
example `1.00`, `1.00a`, `1.01`. One version applies to the whole protocol
suite rather than to individual pages; the current value is recorded in
[`publish.yaml`](publish.yaml) (`revision:`) and stamped on every published
wiki page and PDF.

- **MAJOR** and **MINOR** are **numbers**. The minor is always written as two
  digits with a leading zero (`YY`): `00`, `01`, …, `10`.
- **PATCH** is a **letter** appended directly to the minor with no separator:
  `a`, `b`, `c`, … No letter means no patch (e.g. `1.01` is the base of that
  minor; `1.01a` is its first patch).

| Part | Type | When it changes | Examples |
| ---- | ---- | --------------- | -------- |
| **MAJOR** (`X`) | number | Once per year, **locked at the start of the season**. Establishes the stable, citable baseline that field teams follow for that season. Bumping the major resets the minor to `00` and drops any patch letter. | First release = `1.00`; next season's lock = `2.00`. |
| **MINOR** (`.YY`) | number (two digits, leading zero) | A change that alters **what you do** or **adds new scope** during the season. Bumping the minor drops any patch letter. | A stub is replaced with real content; a new page/protocol is added; an APEx result confirms or changes a parameter that was flagged "to be confirmed" (e.g. the positional thresholds, the solar-noon window); an identified issue forces a procedural change. `1.00` → `1.01`. |
| **PATCH** (`x`) | letter | A change that does **not** alter the procedure. Safe to adopt without re-checking already-collected data. | Spelling/grammar/formatting fixes; clarifying wording that explains existing intent without changing it; adding or replacing an illustrative photo or diagram. `1.01` → `1.01a` → `1.01b`. |

### Minor vs patch — the deciding question

Ask: *"Would someone who already followed the previous version need to do
anything differently, or re-check data they have already collected?"*

- **Yes → MINOR.** The procedure, scope, or an operational parameter changed.
- **No → PATCH.** The change only improves how the existing procedure is
  explained or presented.

A clarification is the common grey area: if it changes the instruction it is a
**minor** change; if it only makes the existing instruction easier to
understand it is a **patch**.

### What changes within a season

The major version is locked at the start of the season, so the suite is meant
to stay **stable** while teams are in the field. In-season **minor** releases
are therefore limited to:

- finishing a stub or adding a new page (adds scope without changing an
  existing procedure);
- resolving an item that was explicitly flagged as provisional — the
  *Adopted — with potential APEx revisions* and *Completion depending on APEx
  results* documents listed under [Document status](#document-status);
- correcting a procedure that was found to be wrong.

The last case is the only one that changes an already-stable procedure
mid-season; when it happens the release notes must call it out clearly so
teams know to adjust. Larger reworks are held for the next annual **major**
revision.

> [!IMPORTANT]
> Every **minor** release must be announced at a Field EWG meeting so all
> nodes are aware of the change in scope or procedure. Patch releases do not
> require an announcement. Minor releases are also documented on the wiki
> Home page, in this README, and in a note at the top of each impacted page.

Every release is recorded in the protocols changelog
([Protocols/CHANGELOG.md](Protocols/CHANGELOG.md)), which is also published to
the wiki as the **Changelog** page.

## Document status

The tables below list every protocol document (background reference documents
are excluded). The **Last revised** column records the revision in which each
document last changed — at the `1.00` release every document is `1.00`, and a
document only moves to `1.01`, `1.02`, … (or a patch letter) in the revision
that actually changes it. See [Protocols/STATUS.md](Protocols/STATUS.md) for
the full auto-generated status tracker.

> [!NOTE]
> The authoritative source for each document's revision is its `last_revised`
> field in [publish.yaml](publish.yaml), which the publish script renders into
> the per-page banner and the auto-generated
> [Protocols/STATUS.md](Protocols/STATUS.md) tracker. The tables below are
> maintained by hand for convenience; if they ever disagree with the tracker,
> the tracker is correct.

### Adopted

> [!NOTE]
> Reviewed, approved by the Field EWG, and locked for the current revision.

| Document | Last revised |
| -------- | ------------ |
| [GOBI M350 Fieldbook](Protocols/Sensors/GOBI/GOBI_M350_FieldBook.md) | `1.00` |
| [GOBI IF1200 Fieldbook](Protocols/Sensors/GOBI/GOBI_IF1200_FieldBook.md) | `1.00` |
| [HiRes Fieldbook](Protocols/Sensors/HIRES/HIRES_FieldBook.md) | `1.00` |
| [CALViS Fieldbook](Protocols/Sensors/CALVIS/CALViS_FieldBook.md) | `1.00` |
| [Standard Flight Procedure](Protocols/FlightDesign/StandardFlight/Standard_Flight.md) | `1.00` |
| [Data Folder Structure](Protocols/DataManagement/DataFolderStructure/DataFolderStructure.md) | `1.00` |
| [Processing Pipelines](Protocols/Pipelines/GryfnProcessingPipeline/Gryfn_Processing_Pipeline.md) | `1.00` |

### Adopted — with potential APEx revisions

> [!NOTE]
> Adopted and usable now, but specific parameters or sections may be revised
> once the APEx flights provide the data needed to confirm them.

| Document | Last revised | Notes |
| -------- | ------------ | ----- |
| [QA Process](Protocols/QA/QAprocess/AerialDataQC.md) | `1.00` | Positional thresholds and the spectral/LiDAR accuracy baselines are still being developed against APEx data. |
| [Plot Delineation](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md) | `1.00` | The three delineation methods are still being cross-validated. |

### Completion depending on APEx results

> [!NOTE]
> Not yet complete; these documents will be finalised using the outcomes of
> the APEx flights.

| Document | Last revised | Notes |
| -------- | ------------ | ----- |
| [Validation Flight](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md) | `1.00` | Being restructured as part of early-season APEx work. |

### Stubs — draft being written

| Document | Last revised |
| -------- | ------------ |
| [M3M Fieldbook](Protocols/Sensors/M3M/M3M_FieldBook.md) | `1.00` |
| [Spectral Panel Cleaning and Calibration](Protocols/QA/SpectralPanel/Spectral_Panel_Cleaning_and_Calibration.md) | `1.00` |
| [M3M Processing Pipeline](Protocols/Pipelines/M3MPipeline/M3M_Processing_Pipeline.md) | `1.00` |
| [HiRes Processing Pipeline](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md) | `1.00` |

## Repository layout

```
Protocols/
├── Home/
│   └── Home_Intro.md                 Static intro injected into the wiki Home page
├── Sensors/
│   ├── PlatformsOverview/            High-level description of APPN platforms
│   ├── CALVIS/                       Headwall CoAligned HP + LiDAR + GNSS-INS (IF1200)
│   ├── GOBI/                         GOBI sensor platform (separate M350 and IF1200 fieldbooks)
│   ├── M3M/                          DJI M3M multispectral platform (stub)
│   └── HIRES/                        HiRes Phase One RGB platform
├── FlightDesign/
│   ├── StandardFlight/               Standard flight procedure
│   └── ValidationFlight/             Validation flight procedure
├── QA/
│   └── QAprocess/                    Aerial data QC procedure (operator workflow)
├── PlotProtocols/
│   └── PlotDelineation/             Plot delineation shapefile spec + methods
├── DataManagement/
│   └── DataFolderStructure/          Standard storage layout for raw/processed data
├── Pipelines/
│   ├── GryfnProcessingPipeline/          GRYFN standard processing pipeline outputs
│   └── StandardDataProducts/         Tabular summary of standard data products
└── Background/
    ├── QCandReporting/               User-facing QC philosophy & reporting guidance
    └── PhenotypingAndEnvironmental/  Ground-based phenotyping & env. instruments
Protocols/CHANGELOG.md                Protocols changelog (published to the wiki)

OriginalDocuments/                    Source .docx files (input to docx_to_markdown.py)
└── FieldProtocolsAndPipelinesWiki/   Verbatim archive of imported wiki originals
Scripts/
├── docx_to_markdown.py               Convert .docx -> .md (+ media) into Protocols/
├── publish_to_wiki.py                Publish locked revision to the wiki + optional PDFs
└── wiki_assets/                      Static _Footer copied to the wiki
publish.yaml                          Manifest: revision number + page mapping
releases/Rev<MAJOR.YYx>/              PDF snapshots, written by `publish_to_wiki.py --pdf`
```

Each SOP folder contains a single `*.md` file plus a `*_media/` folder with
its embedded images. Filenames do **not** carry a revision suffix — the
revision is tracked centrally in `publish.yaml` and via git tags.

## Working draft vs locked revision

| Where           | What it holds                                         | How it changes                       |
| --------------- | ----------------------------------------------------- | ------------------------------------ |
| This repo       | Drafts in progress for the next revision              | Pull requests / direct commits       |
| GitHub Wiki     | The current locked revision (read-only for end users) | Regenerated by `publish_to_wiki.py`  |

## Contributing changes

External contributions are made via the standard GitHub **fork → branch →
pull request** workflow. You do not need write access to this repository.

### 1. Fork the repository

1. Open the repo on GitHub:
   <https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures>.
2. Click **Fork** (top-right) and create the fork under your own GitHub
   account. Keep the default repository name.

### 2. Clone your fork locally

```bash
git clone https://github.com/<your-username>/APPN-Aerial-Standard-Operating-Procedures.git
cd APPN-Aerial-Standard-Operating-Procedures

# Add the upstream repo so you can pull in future updates
git remote add upstream https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures.git
git fetch upstream
```

### 3. Create a branch for your change

```bash
git checkout -b my-edit-description
```

Use a short, descriptive branch name (e.g. `fix-hires-typo`,
`update-plot-delineation-trial-info`).

### 4. Make and commit your edits

Edit the relevant `Protocols/.../*.md` file(s). Keep changes focused — one
logical change per pull request makes review much easier.

```bash
git add Protocols/<path>/<file>.md
git commit -m "Short description of the change"
git push -u origin my-edit-description
```

> [!NOTE]
> Edit the draft Markdown under `Protocols/`, **not** the rendered files in
> the wiki repo — the wiki is regenerated by `publish_to_wiki.py` when a new
> revision is cut.

### 5. Open a pull request via GitHub's "Contribute"

After pushing, GitHub shows a yellow banner on both your fork and the
upstream repo with a **Compare & pull request** button — the fastest path:

1. Go to your fork on GitHub.
2. Click **Contribute → Open pull request** (or the **Compare & pull
   request** banner if it appears).
3. Confirm the base is
   `ArdenB/APPN-Aerial-Standard-Operating-Procedures:main` and the compare
   is `<your-username>/...:my-edit-description`.
4. Give the PR a clear title and a short description explaining **what**
   changed and **why**. Reference any related issue (`Fixes #123`).
5. Click **Create pull request**.

A maintainer will review the PR, request changes if needed, and merge it
once approved. Any further commits you push to the same branch are
automatically added to the open PR.

### 6. Keep your fork up to date

Before starting your next change, sync your fork with upstream:

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

## Workflows

### Convert a new `.docx` source

```bash
pip install mammoth
python Scripts/docx_to_markdown.py             # converts everything in OriginalDocuments/
```

Known SOP `.docx` files are routed automatically into the matching
`Protocols/.../` folder with the canonical (revision-less) basename. Use
`-o <dir>` to override the destination.

### Publish a new revision to the wiki

1. Make sure the wiki repo is cloned next to this repo:

   ```bash
   git clone https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures.wiki.git \
       ../APPN-Aerial-Standard-Operating-Procedures.wiki
   ```

2. Bump `revision` (and optionally `revision_date`) in
   [`publish.yaml`](publish.yaml).

3. Preview the changes:

   ```bash
   pip install pyyaml
   python Scripts/publish_to_wiki.py --dry-run
   ```

4. Write the changes into the wiki working copy:

   ```bash
   python Scripts/publish_to_wiki.py
   ```

5. Review the diff in the `.wiki` repo and push:

   ```bash
   cd ../APPN-Aerial-Standard-Operating-Procedures.wiki
   git add -A && git commit -m "Publish Rev <MAJOR.YYx>" && git push
   ```

The publish script:

- Copies each manifest page into `<wiki>/<wiki_page>.md`.
- Injects a "Locked revision" banner under the H1.
- Rewrites image links from `*_media/...` to `media/<wiki_page>/...` and
  copies the matching media folder into `<wiki>/media/<wiki_page>/`.
- Regenerates `Home.md` and `_Sidebar.md` from the manifest, grouped by
  category.

### Generate PDF snapshots of the locked revision

```bash
python Scripts/publish_to_wiki.py --pdf
```

Writes one PDF per manifest page into `releases/Rev<revision>/`, rendered
with [`pandoc`](https://pandoc.org/) (must be on `PATH`, with a working
PDF engine such as `xelatex`, `wkhtmltopdf`, or `weasyprint`).

### Cut a GitHub release

Each locked revision is published as a **GitHub release**, so every version of
the suite has a permanent, citable snapshot with the PDFs attached. The release
**tag** is derived from the `revision` in [`publish.yaml`](publish.yaml):
revision `1.00` → tag `v1.00`, revision `1.01a` → tag `v1.01a`.

Do this **after** the wiki has been published and the PDFs generated for the
revision (the steps above).

1. Confirm the revision you are releasing:

   ```bash
   grep '^revision:' publish.yaml          # e.g. revision: "1.00"
   ```

2. Make sure the PDF snapshots for that revision exist:

   ```bash
   python Scripts/publish_to_wiki.py --pdf
   ls releases/Rev1.00/                    # match the revision above
   ```

3. Tag the commit that represents the locked revision and push the tag:

   ```bash
   git tag -a v1.00 -m "Rev 1.00"
   git push origin v1.00
   ```

4. Create the release and attach the PDF snapshots. Using the
   [GitHub CLI](https://cli.github.com/):

   ```bash
   gh release create v1.00 releases/Rev1.00/*.pdf \
       --title "Rev 1.00" \
       --notes "Summary of what changed in this revision."
   ```

   Or, via the web UI: **Releases → Draft a new release**, choose the `v1.00`
   tag, set the title to `Rev 1.00`, write the notes, and upload every PDF
   from `releases/Rev1.00/` as a release asset.

> [!IMPORTANT]
> The release notes are the place to call out any **minor** change that altered
> an already-stable procedure mid-season (see [Versioning](#versioning)), so
> teams know to adjust. Keep the tag (`vMAJOR.YYx`), the wiki banner, and the
> `revision` in `publish.yaml` in step.
>
> Before tagging, add a section for the new revision to the protocols changelog
> ([Protocols/CHANGELOG.md](Protocols/CHANGELOG.md)) and reuse that summary as
> the release notes.

## Licence

This work is licensed under a
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
See [LICENSE](LICENSE) for the full text.