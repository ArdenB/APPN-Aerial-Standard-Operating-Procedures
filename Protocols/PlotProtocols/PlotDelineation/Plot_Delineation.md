# APPN – Plot Delineation

> [!WARNING]
> **Draft document — most major decisions ratified, some follow-ups
> still pending with the APPN Field EWG.** The Field EWG
> plot-delineation meeting ratified the file format (GeoJSON), the
> minimum required attribute set, the storage location, and the
> general approach to buffers. Outstanding follow-ups (the final
> buffer rule, optional-column handling, the file naming convention,
> and the trial-information spreadsheet specification) are listed in
> the [Outstanding TODOs](#document-status--work-in-progress) below.

This protocol defines the APPN standard for plot delineation shapefiles —
their structure, attributes, and storage location within the APPN folder
hierarchy — and documents the supported methods for producing them from
APPN aerial imagery (typically RGB orthomosaics captured by GRYFN UAV
systems). Consistent plot delineation underpins repeatable phenotypic
analysis across APPN trials.

> [!IMPORTANT]
> The APPN plot shapefile specification below must be followed for all
> trials, regardless of which method is used to generate the shapefile.
> For any deviations from this specification or these methods (e.g.
> alternative tools, non-standard plot layouts), keep detailed records of
> the changes made, the rationale, and any implications for downstream
> analysis.

---

> [!IMPORTANT]
> **Document status — work in progress.**
> This protocol is a draft and requires further revision before it can
> be considered final. The points below capture the state of each
> section after the **APPN Field EWG plot-delineation meeting**.
>
> **✅ Resolved at the Field EWG meeting:**
>
> - **File format — GeoJSON ratified as the primary format** (Arden,
>   Bipul agreed). Shapefile remains accepted only as a legacy /
>   companion format.
> - **Storage location — current `Documentation/Plot_Layout/` path is
>   confirmed**, no changes required (see
>   [Storage location](#storage-location)).
> - **Buffer table approach is endorsed** (Lleyton): values in the
>   table represent **minimum** buffers; Arden to replace the
>   placeholder examples with realistic plot sizes (6 × 2, 10 × 3,
>   6 × 1.5 — DPIRD, 4 × 1.5 — UOA OzBarley) and note that plot
>   widths can vary substantially (Ingrid).
> - **Minimum required attribute set agreed:** `fid`, `plot_id`,
>   `row`, `range`, `crop`. `is_buffer` and `block` are **optional**
>   (carried when the trial design defines them).
> - **Sensor identifier belongs in the file name** (Ingrid) —
>   different sensors can produce different geometries (UOA: RGB vs
>   LiDAR vs VNIR all differ). Use `VNIR_RGB` as the sensor tag for
>   both CALViS and GOBI products.
>
> **⚠️ Still outstanding — Field EWG follow-ups:**
>
> **Recommended buffer** (see [Recommended Buffer](#recommended-buffer))
> - [ ] Decide whether the buffer should be a **percentage** or a
>       **"ditch a row"** rule — may end up being species-specific.
>       Goal is simply to stop edge effects.
> - [ ] Arden to write up the revised buffer guidance (real-life plot
>       examples, minimum-vs-target framing, species-specific notes).
>
> **Required attributes** (see [Required attributes](#required-attributes))
> - [ ] Decide how to handle **optional columns** — carry as empty /
>       placeholder columns, or omit entirely when no data is
>       available.
> - [ ] Both delineation tools have metadata-capture approaches —
>       confirm which approach (or harmonised superset) is the APPN
>       standard.
>
> **File naming convention** (see [File naming convention](#file-naming-convention))
> - [ ] Arden to report back with a proposed naming convention that
>       includes:
>   - The **sensor identifier** (e.g. `VNIR_RGB`, `LiDAR`, `RGB`).
>   - Clear handling of **special cases** (e.g. all-of-plot biomass
>       collection at UOA).
>   - Per-sensor variants only when the geometries actually differ.
> - [ ] Set a hard rule: if shapefile differences **within a single
>       sensor** exceed ~**5 cm**, do **not** hack around them with
>       extra files — escalate and address the root cause.
>
> **Joining trial information** (see [Joining Trial Information](#joining-trial-information))
> - [ ] Define the **trial-information spreadsheet specification** —
>       mandatory columns, format (`.csv` vs `.xlsx`), naming, and
>       storage location.
> - [ ] Decide whether the join is performed **once at trial setup**
>       or **re-applied each time** the shapefile is regenerated, and
>       whether the joined output overwrites or is saved as a separate
>       file.
> - [ ] Encourage researchers / clients to **provide better plot
>       information** up front (trial design + plot dimensions).
>
> **Methods** (see [Methods](#methods))
> - [ ] **Mickey to write the GPT plot-creation tool** (becomes
>       Method 3, replacing the previous "GRYFN plot tool" placeholder).
> - [ ] **FIELDimageR meeting with Bipul and Mickey** — still TBC;
>       outcomes to be folded back into
>       [Method 1](#method-1-fieldimager-qgis).
> - [ ] For the **Omega** platform, capture **vegetation width** in
>       trial metadata so it can be used to set track width.

---

## Document Structure

This protocol is organised so you can read it top-to-bottom for the full
APPN plot delineation standard, or jump straight to the section you need.
Decisions made at the **APPN Field EWG plot-delineation meeting** are
reflected inline; outstanding follow-ups are flagged in the
[Outstanding TODOs](#document-status--work-in-progress) at the top.

- [APPN Plot Delineation](#appn-plot-delineation) — rationale and the
  competing sources of error a standard delineation approach must manage.
  - [Recommended Buffer](#recommended-buffer) — minimum inward buffer
    values, real-world worked examples, and when to deviate.
- [APPN Plot Shapefile Standard](#appn-plot-shapefile-standard) — the
  mandatory file format, attributes, storage location, and naming
  convention every plot layout file must follow.
  - [File format](#file-format) — **GeoJSON ratified as the primary
    format**; shapefile retained as legacy / companion only.
  - [Required attributes](#required-attributes) — the ratified minimum
    set (`fid`, `plot_id`, `row`, `range`, `crop`) plus optional
    columns (`is_buffer`, `block`, etc.).
  - [Storage location](#storage-location) — confirmed as
    `Documentation/Plot_Layout/`.
  - [File naming convention](#file-naming-convention) — sensor tag in
    the file name (e.g. `VNIR_RGB`); revision being finalised by Arden.
- [Joining Trial Information](#joining-trial-information) — how trial
  metadata is attached to the plot geometry via `plot_id`. Spreadsheet
  spec still pending EWG.
- [Methods](#methods) — supported procedures for generating an
  APPN-compliant plot layout file.
  - [Method 1: FIELDimageR (QGIS)](#method-1-fieldimager-qgis)
  - [Method 2: DPIRD Field Mapping Tool](#method-2-dpird-field-mapping-tool)
  - [Method 3: GPT plot creation tool](#method-3-gpt-plot-creation-tool)
    — to be written by Mickey.

---

## APPN Plot Delineation

A standard APPN plot delineation approach ensures that comparable trials can
be analysed consistently across nodes. The goal is to maximise the usable
plot area sampled by the aerial data while minimising two competing sources
of error:

- **Edge effects** — agronomic and radiometric contamination from
  neighbouring plots, alleys, and bare soil at plot boundaries.
- **Positional uncertainty** — small misalignments between the plot
  shapefile and the orthomosaic caused by GNSS/RTK error, orthorectification
  residuals, and sowing/layout drift (rows bowing or skewing relative to
  the design grid as the seeder tracks across the trial).

In practice, this is achieved by applying a consistent inward **buffer** to
each plot polygon so the analysed region sits comfortably inside the true
plot extent, regardless of which method is used to generate the shapefile.

### Recommended Buffer

> [!IMPORTANT]
> The Field EWG endorsed the **table-based buffer approach** (Lleyton).
> The values in the table are **minimum buffers** — trials should
> apply at least these buffers, and may apply more if site / canopy
> conditions warrant. Arden is updating the table with realistic plot
> sizes (6 × 2, 10 × 3, 6 × 1.5 — DPIRD, 4 × 1.5 — UOA OzBarley) to
> replace the original placeholders.
>
> **Still open:** whether the rule should be expressed as a
> **percentage of plot dimension** or as a **"ditch a row"** rule
> (likely species-specific). The agreed objective is simply to
> eliminate edge effects — see the
> [Outstanding TODOs](#document-status--work-in-progress) at the top.

To keep results comparable across nodes, APPN trials should apply at
least the inward buffer specified in the table below to every plot
polygon. The current working rule is:

> [!NOTE]
> **APPN minimum buffer (working rule):** 0.3 m from each plot end and
> 0.2 m from each plot side (across the drill direction), **or** 15 %
> of the corresponding plot dimension — whichever is larger. Final
> rule (% vs ditch-a-row) is still under EWG discussion.

The buffer used must be recorded in the tool-specific configuration saved
alongside the shapefile (e.g. the FIELDimageR JSON) so the layout can be
reproduced.

#### Worked examples (real-world APPN plot sizes)

| Plot size (L × W)                       | Min. buffer (end / side) | Analysis area (L × W) | % of plot |
| --------------------------------------- | ------------------------ | --------------------- | --------- |
| 6 m × 2 m   (common cereal yield plot)  | 0.5 m / 0.25 m           | 5.0 m × 1.5 m         | ~63 %     |
| 6 m × 1.5 m (DPIRD standard)            | 0.5 m / 0.2 m            | 5.0 m × 1.1 m         | ~61 %     |
| 4 m × 1.5 m (UOA OzBarley)              | 0.3 m / 0.2 m            | 3.4 m × 1.1 m         | ~62 %     |
| 10 m × 3 m (common agronomy strip)      | 1.0 m / 0.5 m            | 8.0 m × 2.0 m         | ~53 %     |

> [!NOTE]
> Plot widths can vary substantially between trials (Ingrid — UOA),
> so the table is **illustrative**, not exhaustive. Apply the working
> rule above to any plot size not listed.

> [!NOTE]
> **Sorghum and other widely-spaced crops** can require a different
> buffer logic — flagged for the species-specific decision still
> pending with the EWG.

#### When to increase the buffer

- Coarser GSD (e.g. hyperspectral at ~5 cm vs RGB at ~1 cm).
- Tall or lodging-prone canopies where canopy lean shifts the visible plot
  off its sown footprint.
- Narrow alleys (<0.5 m) where neighbouring canopies merge.
- Trials without RTK GNSS or without ground control points (GCPs) in the
  orthomosaic.

#### When a smaller buffer may be acceptable

- RTK-georeferenced GCPs present in the orthomosaic.
- Wide alleys with bare inter-row visible between plots.

> [!NOTE]
> Any deviation from the default buffer must be recorded with the trial's
> plot layout files and justified in the trial notes.

---

## APPN Plot Shapefile Standard

All APPN plot shapefiles must conform to the following standard so that
downstream pipelines can ingest them without trial-specific configuration.

### File format

> [!IMPORTANT]
> **Field EWG decision:** **GeoJSON is the ratified primary format**
> for all new APPN plot layout files (Arden, Bipul agreed). Shapefile
> is retained only as a legacy / companion format.

- **Primary format:** **GeoJSON** (`.geojson`) — a single, plain-text,
  self-contained file. See
  [File Format — GeoJSON vs Shapefile](../../QA/QAprocess/AerialDataQC.md#file-format--geojson-vs-shapefile)
  in the Aerial Data QC protocol for the full rationale (single-file
  packaging, version-control friendliness, no field-name length or file
  size caps, open web-native standard).
- **Legacy / companion format:** ESRI Shapefile (`.shp` plus its
  sidecar files `.shx`, `.dbf`, `.prj`, `.cpg`). All sidecar files
  must be kept together with the `.shp`. Existing shapefiles do **not**
  need to be re-created, but **all new APPN files must be saved as
  `.geojson`**.
- **CRS:** the CRS of the source orthomosaic (typically the correct zone
  of GDA2020). For GeoJSON, keep the file in the projected CRS of the
  orthomosaic rather than reprojecting to WGS84 (see the linked rationale
  above). For shapefiles, the `.prj` file must be present and correct.
- **Geometry:** one polygon per plot. Polygons should be rectangular and
  aligned to the trial layout, sized to the plot dimensions minus the
  inward buffer applied to mitigate edge effects.
- **Optional companion copy:** a second copy of the same layer in
  shapefile form may be saved alongside the primary GeoJSON using the
  **same base file name** (e.g. `MyTrial_plots.geojson` →
  `MyTrial_plots.shp`). This is useful for tools that only consume
  shapefiles, but is not required.

### Required attributes

> [!IMPORTANT]
> **Field EWG decision:** the **mandatory attribute set is now
> ratified** — see the table below. `species` has been **removed**.
> Treatment of optional columns (placeholder columns vs omit when
> empty) is still under discussion.

Every APPN plot polygon **must** carry the following attributes:

| Column          | Required?                       | Description |
| --------------- | ------------------------------- | ----------- |
| `fid`           | Mandatory                       | Unique polygon identifier assigned by the delineation tool. Identifies the *geometry* only and may not match the trial's plot numbering. |
| `plot_id`       | Mandatory                       | Plot number from the trial design / sowing plan. **Join key** for trial metadata (see [Joining Trial Information](#joining-trial-information)). |
| `row`           | Mandatory                       | Row index in the trial design. |
| `range`         | Mandatory                       | Range (column) index in the trial design. |
| `crop`          | Mandatory                       | Crop type (e.g. *Wheat*). |

> [!NOTE]
> `fid` and `plot_id` must be kept as **separate columns**. `fid` is
> the tool's internal polygon ID; `plot_id` is the agronomic plot
> number from the trial design. Conflating the two breaks
> reproducibility when the shapefile is regenerated and `fid` values
> shift. **`plot_id` (not `fid`) is the join key for trial metadata.**

#### Optional attributes

The following columns are **optional**. If the data is no availble
they should be **omitted entirely**. 

Trial design:

- `is_buffer` — Boolean (`True`/`False`) flag marking *buffer plots*
  (filler / border plots that absorb edge effects and carry no
  experimental treatment). Not to be confused with the inward analysis
  **buffer** applied to every plot polygon (see
  [Recommended Buffer](#recommended-buffer)).
- `block` — replication block / replicate identifier from the trial
  design. Include whenever the trial design defines blocks.

Biological / treatment:

- `genotype` / `entry` — variety, line, or accession code. If this
  information is proprietary, an anonymised code may be used instead.
- `treatment` — agronomic or experimental treatment applied to the plot.



Provenance (used to trace how the polygon was produced):

- `method` — delineation method (e.g. `FIELDimageR`, `DPIRD`, `GPT`).
- `buffer_end_m`, `buffer_side_m` — buffer values applied (in metres).
- `source_ortho` — filename or ID of the orthomosaic the polygon was
  fit to.
- `created` — ISO date the file was generated.

> [!NOTE]
> Both Method 1 (FIELDimageR) and Method 2 (DPIRD Field Mapping Tool)
> have their own metadata-capture conventions. Harmonising these into 
> a single standard is still outstanding. Metadata should be saved
> alongside the current file.

> [!NOTE]
> The columns required to **join trial information** from the trial
> spreadsheet are still to be defined. At a minimum, the shapefile and
> the spreadsheet must share `plot_id` so that the join described in
> [Joining Trial Information](#joining-trial-information) can be
> performed reliably. `fid` should not be used as the join key — it is
> tool-assigned and may change when the shapefile is regenerated. 

### Storage location

Save the plot layout file (GeoJSON, or shapefile with all its sidecar
files) in the site-level `Documentation/Plot_Layout/` directory under the
APPN folder structure (see the
[APPN folder structure wiki](https://github.com/ArdenB/APPN_GenricFileStorage/wiki/Folder-Structure)
for the full naming convention).

Formal path:

```
{Node}/
  {YYYY_ProjectDesc[_I|E][_Researcher][_org]}/
  {YYYYSiteName[_F|C]}/Documentation/Plot_Layout/
```

Example:

```
USYD_Narrabri/2025_SIFOzBarley/2025IAWatson_F/Documentation/Plot_Layout/
```

Also save the tool-specific configuration used to generate the layout
file (e.g. the FIELDimageR JSON settings) alongside it so the layout can
be reproduced.

### File naming convention

> [!IMPORTANT]
> **Field EWG meeting outcome:** the convention below is being
> revised by Arden following the meeting and is **not yet ratified**.
> Key decisions captured at the meeting:
>
> - The **sensor identifier belongs in the file name** (Ingrid). Use
>   `VNIR_RGB` as the sensor tag for **both CALViS and GOBI** products.
>   Other expected tags: `RGB` (HiRes), `LiDAR`, etc.
> - Sensor-specific shapefile variants are only justified when the
>   different sensors **actually produce different geometries**
>   (UOA reports RGB vs LiDAR vs VNIR can all differ).
> - **Hard rule:** if shapefile differences **within a single sensor**
>   exceed ~**5 cm**, do **not** create extra files to work around
>   them — escalate and address the root cause.
> - The convention must clearly handle **special cases** — e.g.
>   all-of-plot biomass collection at UOA — with role tags or
>   exclusion layers.
>
> Arden to report back with the revised convention.

A site's `Plot_Layout/` directory may contain more than one plot
shapefile — for example, the main analysis layout, sensor-specific
variants where geometries genuinely differ, and exclusion layers
covering areas affected by destructive field interventions (biomass
cuts, manual sampling quadrats, damaged plots, etc.). A consistent
naming convention keeps these distinguishable.

Working format (subject to revision per the EWG decisions above):

```
{YYYYSiteName}_{role}[_{sensor}][_v{NN}].{ext}
```

| Field | Notes |
| --- | --- |
| `{YYYYSiteName}` | Site identifier (year + site name), matching the parent folder name with the `_F` suffix dropped. Plot layouts only apply to field sites. |
| `{role}` | Short role tag describing what the layer represents (see below). |
| `{sensor}` | **Optional sensor tag**, included when sensor-specific geometries are needed (e.g. `VNIR_RGB`, `RGB`, `LiDAR`). Use `VNIR_RGB` for both CALViS and GOBI. Only add a sensor-specific file when the geometry genuinely differs — see the 5 cm rule above. |
| `_v{NN}` | Optional zero-padded revision (`_v01`, `_v02`, …). Bump on any change to geometry or attributes. |
| `{ext}` | `geojson` (mandated primary). `shp` (with sidecars) is also accepted as a legacy / companion file. |

Working role tags:

- `plots` — the primary analysis layout (one polygon per plot, buffer
  applied per the [APPN Plot Shapefile Standard](#appn-plot-shapefile-standard)).
- `plots_raw` — unbuffered or pre-buffer plot footprints, if retained.
- `exclude_biomass` — areas removed for biomass cuts.
- `exclude_biomass_full` — plots **entirely** removed for biomass
  collection (e.g. UOA all-of-plot biomass workflow).
- `exclude_sampling` — areas removed for other destructive sampling
  (manual quadrats, soil cores, etc.).
- `exclude_damage` — plots or sub-areas excluded due to damage,
  lodging, weed pressure, or other quality issues.
- `gcp` — ground control point locations, if stored alongside the
  layout.

Examples (within
`USYD_Narrabri/2025_SIFOzBarley/2025IAWatson_F/Documentation/Plot_Layout/`):

```
2025IAWatson_plots_v01.geojson                 (primary file — GeoJSON)
2025IAWatson_plots_VNIR_RGB_v01.geojson        (CALViS / GOBI variant, only if geometry differs)
2025IAWatson_plots_LiDAR_v01.geojson           (LiDAR variant, only if geometry differs)
2025IAWatson_plots_v01.shp                     (+ .shx .dbf .prj .cpg — optional companion)
2025IAWatson_plots_v01.json                    (FIELDimageR settings)
2025IAWatson_exclude_biomass_v01.geojson
2025IAWatson_exclude_biomass_full_v01.geojson  (all-of-plot biomass collection)
```

> [!NOTE]
> Exclusion layers should use the **same CRS and `plot_id` scheme** as
> the primary `plots` layer so that downstream pipelines can spatially
> subtract or flag affected plots without additional configuration.

---

## Joining Trial Information

> [!IMPORTANT]
> **Field EWG status:** the trial-information spreadsheet specification
> (mandatory columns, file format, naming convention, storage location)
> and the end-to-end procedure for joining it onto the plot shapefile
> are still **to be defined**. The placeholder workflow below uses
> `plot_id` as the join key (which is ratified) but the spreadsheet
> spec itself is **not yet the APPN standard**.
>
> Encourage researchers and clients to **provide better plot
> information up front** (trial design + plot dimensions) so the
> spreadsheet can be assembled reliably.
>
> Open EWG questions:
>
> - Required vs. optional columns in the trial spreadsheet (e.g.
>   `plot_id`, `row`, `range`, `block` / `replicate`, `crop`,
>   `genotype`, `treatment`).
> - Preferred file format (`.csv` vs `.xlsx`) and naming convention.
> - Where the trial spreadsheet lives in the APPN folder structure
>   (likely under `Documentation/`).
> - Whether the join is performed once at trial setup, or re-applied
>   each time the shapefile is regenerated.
> - Whether the joined output overwrites the source file or is saved
>   as a separate `*_joined` file.

Most delineation tools produce a shapefile whose plots are identified
by a tool-assigned `fid` plus the design's `plot_id`. Trial metadata is
attached as a separate step using `plot_id` as the join key:

1. Prepare a spreadsheet (CSV or XLSX) of trial information with one row
   per plot and a `plot_id` column whose values match the shapefile's
   `plot_id`.
2. In QGIS, load both layers and use **Properties → Joins** on the
   shapefile to join the spreadsheet on the `plot_id` field. Do not use
   `fid` as the join key — it is tool-assigned and may change when the
   shapefile is regenerated.
3. Export the joined layer back to a shapefile in the same `Plot_Layout`
   directory so the trial metadata is persisted in the `.dbf`.

---

## Methods

The following methods are supported for generating an APPN-compliant plot
shapefile. Choose the method that best matches your imagery and tooling;
the resulting shapefile must satisfy the
[APPN Plot Shapefile Standard](#appn-plot-shapefile-standard) above.

- [Method 1: FIELDimageR (QGIS)](#method-1-fieldimager-qgis)
  — follow-up meeting with **Bipul and Mickey** is still TBC; outcomes
  to be folded back into this section.
- [Method 2: DPIRD Field Mapping Tool](#method-2-dpird-field-mapping-tool)
- [Method 3: GPT plot creation tool](#method-3-gpt-plot-creation-tool)
  — **to be written by Mickey** (replaces the previous "GRYFN plot
  tool" placeholder).

---

## Method 1: FIELDimageR (QGIS)

FIELDimageR is an R-based plugin run from within QGIS that builds plot
polygons from a georeferenced orthomosaic.

### Software Installation

Install the following software to start the pipeline:

1. [R](https://www.r-project.org/)
2. [QGIS](https://qgis.org/en/site/)

> [!NOTE]
> The first time you run FIELDimageR-QGIS it may take some time to install
> all required R packages.

#### Enable the Processing Toolbox in QGIS

Make sure the **Processing Toolbox** panel is visible in QGIS:

1. Open the **View** menu.
2. Select **Panels**.
3. Enable **Processing Toolbox**.
4. Confirm the Processing Toolbox is now showing on the right-hand side.

![Enabling the Processing Toolbox in QGIS](Plot_Delineation_media/image_ba05c006aa1d.jpg)

#### Install the Processing R Provider plugin

Install the **Processing R Provider** plugin in QGIS:

1. Open the **Plugins** menu.
2. Select **Manage and Install Plugins**.
3. Switch to the **All** tab.
4. Search for *Processing R Provider*.
5. Click **Install Plugin**.
6. Verify that **R** now appears in the Processing Toolbox.

![Installing the Processing R Provider plugin](Plot_Delineation_media/image_c5873abf8c31.jpg)

#### Install FIELDimageR

1. Go to the FIELDimageR-QGIS GitHub repository:
   [https://github.com/filipematias23/FIELDimageR-QGIS](https://github.com/filipematias23/FIELDimageR-QGIS).
2. Click **Code**.
3. Select **Download ZIP**.
4. Unzip the archive and copy the functions from the `rscripts` folder
   into your **QGIS R scripts** folder.
5. To locate the QGIS R scripts folder, go to
   **QGIS → Processing Toolbox → Options** (the wrench icon).
6. Under **Providers**, click **R**.
7. Copy the path shown for **R scripts folder** and open it in your file
   explorer.
8. Paste the FIELDimageR functions downloaded from GitHub into the
   `rscripts` folder.

![Locating the R scripts folder in QGIS](Plot_Delineation_media/image_5b4a63593e15.png)

![FIELDimageR functions installed in the R scripts folder](Plot_Delineation_media/image_37f8400f36f7.jpg)

### Generating the Plot Shapefile

With FIELDimageR set up, you can now generate plot shapefiles from your
aerial imagery.

1. Load an image into QGIS. An RGB orthomosaic from a GRYFN drone is the
   easiest starting point.

   ![Loaded RGB orthomosaic in QGIS](Plot_Delineation_media/image_d29caa3b45af.png)

2. Open the **fieldShape** module from the Processing Toolbox.

   ![Opening the fieldShape module](Plot_Delineation_media/image_c9dce09dde41.png)

3. Fill in the module parameters:
   - Number of **rows** and **columns**.
   - The **corners** of the trial area (most critical for an accurate
     fit).
   - **Plot size**.
   - **Buffer** — essential for establishing a common analysis area by
     mitigating edge effects.

4. Click **Run**.

   ![Run button in the fieldShape module](Plot_Delineation_media/image_866350342e31.png)

5. The plot shapefile will be generated.

> [!NOTE]
> Achieving a perfect fit usually takes some iteration on the corner
> coordinates. (_TODO: improve this workflow._)

#### Save your settings

Save your fieldShape settings before closing the tool — inputs will be
wiped if FIELDimageR is closed.

![Saving fieldShape settings as JSON](Plot_Delineation_media/image_c93a421b9c73.png)

Use **Copy as JSON** and save the contents as a text file alongside the
shapefile in the trial's `Plot_Layout` directory.

### Output

The shapefile produced by FIELDimageR contains plots identified only by
`fid`.

![Plots identified by fid in the shapefile attribute table](Plot_Delineation_media/image_6bacd8c6405f.png)

Attach trial metadata as described in
[Joining Trial Information](#joining-trial-information), then save the
final shapefile to the trial's `Plot_Layout` directory per the
[APPN Plot Shapefile Standard](#appn-plot-shapefile-standard).

---

## Method 2: DPIRD Field Mapping Tool

The DPIRD Field Mapping Tool is a desktop application for digitising and
managing agricultural field trial plot boundaries over drone orthomosaic
imagery. Built with [Streamlit](https://streamlit.io/) and Python
geospatial libraries, it runs locally in your web browser with no cloud
dependency.

Developed at the
[Department of Primary Industries and Regional Development (DPIRD)](https://www.dpird.wa.gov.au/),
Western Australia, as part of the
[Australian Plant Phenomics Network (APPN)](https://www.plantphenomics.org.au/).

### Features

- **Generate Grid** — Create regular plot grids over drone orthomosaics
  by drawing a trial boundary and specifying banks, rows, buffer, and
  plot dimensions. 
- **Edit Grid** — Interactive browser-based polygon editor with drag,
  vertex editing, multi-select, copy/paste, measurements, undo, and
  keyboard shortcuts.
- **Convert File** — Convert between Shapefile, GeoJSON, GeoPackage,
  and KML formats with optional CRS reprojection (GDA2020, GDA94,
  WGS 84, or custom EPSG).
- **Cropping Tool** — Crop rasters (orthophotos, DSMs, GeoTIFFs) to
  individual plot polygon boundaries, producing one file per plot.

All data is processed locally. No internet connection is required after
installation.

**Detailed installation instruction and documentation is provided in the [DPIRD Field Mapping Tool Documentation](https://github.com/appndpird/DPIRDFieldMappingTool/blob/main/DPIRD_Field_Mapping_Tool_Documentation.pdf) within the GitHub repository. Basic guidelines are provided below.**

### Software Installation

Go to the GitHub repository
[appndpird/DPIRDFieldMappingTool](https://github.com/appndpird/DPIRDFieldMappingTool)
and download the repository (click **Code → Download ZIP**, or
`git clone`). The repository contains two platform-specific
distributions — choose the one that matches your operating system.

#### Requirements

| | Windows | Linux / macOS |
|---|---|---|
| **OS** | Windows 10+ (64-bit) | Ubuntu 20.04+, Fedora, macOS 11+ |
| **Python** | Bundled via Miniconda | User-installed Anaconda/Miniconda |
| **Disk space** | ~2 GB | ~2 GB |
| **Internet** | First-time setup only | First-time setup only |

#### Windows

1. Extract `DPIRD_Field_Mapping_Tool_windows_v1.6.0`.
2. Place
   [`Miniconda3-latest-Windows-x86_64.exe`](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
   in the folder.
3. Double-click `Install_DPIRD_Tool.bat` and press `Y`.
4. Double-click `Run_DPIRD_Tool.bat` to launch.

#### Linux / macOS

1. Extract `DPIRD_Field_Mapping_Tool_linux_v1.6.0`.
2. Ensure [Anaconda or Miniconda](https://docs.anaconda.com/miniconda/)
   is installed.
3. Run:

   ```bash
   chmod +x install_dpird_tool.sh run_dpird_tool.sh
   ./install_dpird_tool.sh
   ./run_dpird_tool.sh
   ```

The tool opens in your browser at
[http://localhost:8501](http://localhost:8501).

### Generating the Plot Shapefile

1. Open the tool and navigate to the **Generate Grid** tab.

2. Enter your project folder path (the folder containing the
   orthomosaic `.tif` file). Click **Browse** or paste the path
   directly.

3. Select the orthomosaic file from the dropdown. Optionally select a
   CSV file to attach additional plot metadata.

4. Set the grid parameters:

   | Parameter | Description |
   |---|---|
   | **Banks** | Number of banks (columns) in the X direction. |
   | **Rows** | Number of rows in the Y direction within each bank. |
   | **Buffer (m)** | Gap between adjacent plots in metres. |
   | **Plot Size (W,H)** | Width and height of each plot in metres, comma-separated (e.g. `4,1`). |

5. Draw a boundary polygon on the map by clicking the four corners of
   the trial area in this order:

   **Top-left (B1R1) → Top-right (BXR1) → Bottom-right (BXRY) →
   Bottom-left (B1RY)**

   The first point defines the origin of the grid (plot B1R1). The
   orientation of the boundary polygon determines the rotation of the
   generated grid.

6. Click **Generate Grid**. Review the generated grid on the map and in
   the data table.

7. Fine-tune if needed — changing any grid parameter after generation
   automatically regenerates the grid using the same boundary.

8. Click **Save Initial Grid** to save as a shapefile.

#### Plot ID Convention

Plots are assigned IDs automatically:

| Field | Formula | Examples |
|---|---|---|
| `Plot_ID` | Bank × 1000 + Row | B1R1 = 1001, B2R3 = 2003 |
| `B/R` | Bank-Row label | B1R1, B2R3, B12R6 |
| `Bank` | Bank number | 1, 2, 3, … |
| `Row` | Row number | 1, 2, 3, … |

### Editing the Plot Shapefile

After generating (or loading an existing grid via the **Edit Grid**
tab), click **Edit Grid** to open the interactive browser-based polygon
editor in a new tab. The editor provides:

| Tool | Shortcut | Description |
|---|---|---|
| Navigate | `Esc` | Pan and zoom. Click a polygon to select it. |
| Drag Plots | `D` | Drag polygons to reposition. Ctrl/Cmd+Click to multi-select. |
| Edit Vertices | `V` | Drag individual corner vertices to reshape polygons. |
| Delete | `X` | Click a polygon to remove it. |
| Draw New | `N` | Click to place vertices; double-click to close. |
| Measurements | `M` | Toggle edge length labels (metres) on all polygons. |
| Copy / Paste | `Ctrl+C` / `Ctrl+V` | Duplicate selected polygons. |
| Undo | `Ctrl+Z` | Revert the last action (up to 50 steps). |
| Select All | `Ctrl+A` | Select all polygons. |

> [!NOTE]
> On macOS, use **Cmd** instead of **Ctrl** for all keyboard shortcuts.

Click **Save Shapefile** in the editor to write the edited grid to disk,
or **Export GeoJSON** to download a GeoJSON file.

### Converting Vector Data File Formats

Use the **Convert File** tab to convert the output shapefile to GeoJSON or reproject to a different CRS:

1. Load the shapefile via **Browse Input File**.
2. Set the output format to **GeoJSON**.
3. Select the target CRS (typically the CRS of the source orthomosaic,
   e.g. GDA2020 / MGA Zone 50).
4. Click **Convert & Save**.

### Cropping Rasters to Plots

Use the **Cropping Tool** tab to crop the orthomosaic (or DSM) to
individual plot boundaries:

1. Load the plot shapefile and the raster file.
2. Choose a save folder and base filename.
3. Click **Crop and Save**.

For a grid with multiple polygons, one raster is saved per plot (e.g.
`cropped_1001.tif`, `cropped_2003.tif`). The tool automatically
reprojects the vector to match the raster's CRS if they differ.

### Output

The shapefile produced by the DPIRD Field Mapping Tool contains plots
identified by `Plot_ID` (Bank × 1000 + Row), `B/R`, `Bank`, and `Row`.
To produce an APPN-compliant plot shapefile:

1. **Rename** `Plot_ID` to `plot_id` (or add a `plot_id` column mapped
   from `Plot_ID`) to match the
   [Required attributes](#required-attributes) specification.
2. **Add** an `fid` column if not already present (sequential polygon
   identifier).
3. **Convert** to GeoJSON using the Convert File tab if the primary
   deliverable should be `.geojson`.
4. Attach trial metadata as described in
[Joining Trial Information](#joining-trial-information), then save the
final file to the trial's `Plot_Layout` directory per the
[APPN Plot Shapefile Standard](#appn-plot-shapefile-standard).

### Further Documentation

Detailed installation instruction and documentation: [DPIRD Field Mapping Tool Documentation](https://github.com/appndpird/DPIRDFieldMappingTool/blob/main/DPIRD_Field_Mapping_Tool_Documentation.pdf).

---

## Method 3: GPT plot creation tool

> [!IMPORTANT]
> **TODO — Mickey to write.** This section will document the
> GRYFN Processing Tool (GPT) plot-creation workflow as the third
> supported APPN method. Replaces the previous placeholder
> *"GRYFN plot tool — TODO"*.

> [!NOTE]
> Additional plot delineation methods will be documented here as they
> are adopted by APPN.

---
