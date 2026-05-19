# APPN Aerial SOP — Outstanding Work

This document tracks outstanding work across the protocol `.md` files in this
repository. Items are grouped per source document. Each entry links to the
relevant line in the source file. A separate **Pending Field EWG approval**
section at the end summarises everything that explicitly requires APPN Field
EWG ratification before it can be treated as the APPN standard.

Document status across the SOP is tracked in
[Protocols/STATUS.md](Protocols/STATUS.md) (auto-generated from
[publish.yaml](publish.yaml)). The image / figure backlog is tracked
separately in [IMAGE_TODO.md](IMAGE_TODO.md).

Last refreshed by reviewing all `.md` files under `Protocols/` plus the
top-level `README.md` and `Scripts/README.md`.

---

## Plot Delineation — [Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md)

Document-wide status: **Draft**. Major decisions ratified at the APPN Field
EWG plot-delineation meeting (GeoJSON file format, storage location,
minimum attribute set `fid`/`plot_id`/`row`/`range`/`crop`, sensor
identifier in filename). Follow-ups captured at
[lines 30–105](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L30-L105).

**Recommended buffer** ([line 58](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L58))

- [ ] Decide whether the buffer should be a **percentage** or a
  **"ditch a row"** rule (likely species-specific).
- [ ] Arden to write up the revised buffer guidance (real-world plot
  examples, minimum-vs-target framing, species-specific notes), replacing
  the placeholder examples with realistic plot sizes (6 × 2, 10 × 3,
  6 × 1.5 — DPIRD, 4 × 1.5 — UOA OzBarley).

**Required attributes** ([line 64](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L64))

- [ ] Decide how to handle **optional columns** — carry as empty /
  placeholder columns, or omit entirely when no data is available.
- [ ] Confirm which metadata-capture approach (or harmonised superset)
  across the two delineation tools is the APPN standard.

**File naming convention** ([line 71](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L71))

- [ ] Arden to propose a naming convention that includes the sensor
  identifier (`VNIR_RGB`, `LiDAR`, `RGB`), clear handling of special
  cases (e.g. all-of-plot biomass collection at UOA), and per-sensor
  variants only when the geometries actually differ.
- [ ] Set the hard rule: if shapefile differences **within a single
  sensor** exceed ~**5 cm**, escalate and fix the root cause rather
  than producing extra files.

**Joining trial information** ([line 84](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L84))

- [ ] Define the **trial-information spreadsheet specification** —
  mandatory columns, format (`.csv` vs `.xlsx`), naming, and storage
  location.
- [ ] Decide whether the join is performed **once at trial setup** or
  **re-applied** each time the shapefile is regenerated, and whether the
  joined output overwrites or is saved as a separate file.
- [ ] Encourage researchers / clients to provide better plot information
  up front (trial design + plot dimensions).

**Methods** ([line 96](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L96))

- [ ] **Mickey to write the GPT plot-creation tool** section (becomes
  Method 3, replacing the previous "GRYFN plot tool" placeholder) —
  see also [line 813](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L813).
- [ ] **FIELDimageR meeting with Bipul and Mickey** — outcomes to be
  folded back into
  [Method 1](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L495).
- [ ] For the **Omega** platform, capture **vegetation width** in trial
  metadata so it can be used to set track width.
- [ ] Improve the FIELDimageR corner-coordinate fitting workflow
  (currently iterative)
  ([line 590](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L590)).

---

## Standard Flight — [Protocols/FlightDesign/StandardFlight/Standard_Flight.md](Protocols/FlightDesign/StandardFlight/Standard_Flight.md)

Document-wide status: **Draft** with outstanding TODOs at
[lines 25–95](Protocols/FlightDesign/StandardFlight/Standard_Flight.md#L25-L95).

**Content review**

- [ ] Review and revise all section content for technical accuracy and
  completeness.
- [ ] Cross-check terminology and links against the sensor fieldbooks.
- [ ] Confirm equipment checklists with field operators for all three
  flight designs (Dual ELM, Single ELM, Multi-Flight Capture).

**Figures to produce** (see [IMAGE_TODO.md](IMAGE_TODO.md))

- [ ] **Photo** — Panel set correctly laid out on a folding table.
- [ ] **Photo** — Validation panel table with the elevated GCP and the
  paired ground GCP in the adjacent flight line (finish once the new
  panels arrive).
- [ ] **Photo (suggested)** — Hero/cover photo of a complete,
  correctly-staged standard flight site.

**Cross-links to add**

- [ ] Add cross-link to the processing pipeline page covering dual-panel
  ingestion in GPT
  ([line 65](Protocols/FlightDesign/StandardFlight/Standard_Flight.md#L65)).
- [ ] Cross-link the processing pipeline page once published
  ([line 306](Protocols/FlightDesign/StandardFlight/Standard_Flight.md#L306)).

**Pending APEx / GRYFN decisions** (revise before season start)

- [ ] Confirm or revise the align-with-planting-direction recommendation
  in Flight-line Orientation
  ([line 70](Protocols/FlightDesign/StandardFlight/Standard_Flight.md#L70)).
- [ ] Confirm whether the Dual ELM panel flight is truly **mandatory**
  under variable illumination, or only strongly recommended.
- [ ] Confirm whether the Single ELM panel flight is permitted at all
  under variable illumination.
- [ ] Confirm the season-start parameter set
  ([line 171](Protocols/FlightDesign/StandardFlight/Standard_Flight.md#L171))
  and the "single offload per flight" rule with APEx
  ([line 376](Protocols/FlightDesign/StandardFlight/Standard_Flight.md#L376)).

**Operational parameters still to be defined**
([line 82](Protocols/FlightDesign/StandardFlight/Standard_Flight.md#L82))

- [ ] Maximum permissible wind speed per UAV / sensor combination.
- [ ] Standard exposure-setting procedure (cross-link once finalised in
  the sensor fieldbooks).
- [ ] Minimum acceptable solar elevation for routine surveys.
- [ ] Quantitative definition of the "effective capture area" inset
  (currently ~10%).

---

## Validation Flight — [Protocols/FlightDesign/ValidationFlight/Validation_Flight.md](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md)

Document-wide status: **Draft — currently being restructured**
(see CAUTION banner at
[lines 30–37](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L30-L37)).
TODO list at
[lines 40–95](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L40-L95).

**Content review**

- [ ] Define and confirm the **frequency** of each validation flight type
  (currently `_TODO_`)
  ([line 52](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L52),
  [line 266](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L266),
  [line 427](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L427)).
- [ ] Confirm the **acceptance criteria / pass-fail thresholds** for each
  validation flight type with the Field EWG
  ([line 377](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L377),
  [line 466](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L466)).
- [ ] Cross-check terminology and links against the sensor fieldbooks and
  the Standard Flight Procedure.
- [ ] Confirm equipment checklists with field operators for all three
  validation flight types.
- [ ] Add guidance on minimum site footprint and on documenting site
  selection
  ([line 165](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L165)).
- [ ] Confirm minimum solar elevation and maximum permissible wind for
  validation flights
  ([line 183](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L183)).
- [ ] Link to a standard validation flight log template
  ([line 236](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L236)).
- [ ] Insert the exposure-setting procedure for the spectral validation
  flights (referenced in two procedure blocks at
  [line 334](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L334)
  and
  [line 365](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L365)).
- [ ] Specify required **weather station** and **downwelling radiation
  sensor** models
  ([lines 395–396](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L395-L396)).

**Figures to produce** (see [IMAGE_TODO.md](IMAGE_TODO.md))

- [ ] **Diagram** — Spectral validation flight (panel layout, flight-line
  orientation, GCP distribution)
  ([line 281](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L281),
  [line 313](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L313)).
- [ ] **Diagram** — Spatial validation flight (GCP layout, flight-line
  geometry, check targets)
  ([line 442](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L442)).
- [ ] **Diagram** — APEx experimental flight reference layout.
- [ ] **Photo (suggested)** — Example validation site.
- [ ] **Chart (suggested)** — Sample QC plot showing spectral validation
  metrics annotated as pass vs fail.

**Cross-links to add**

- [ ] Processing pipeline page describing how validation outputs are
  analysed (radiometric drift, geometric error reports).
- [ ] QA process page describing how validation results feed into the
  node-level QA record.

**Pending APEx decisions** (revise before season start)

- [ ] Lock the standard validation flight footprint (area, altitude,
  speed, overlap) once APEx parameter sweeps complete.
- [ ] Confirm minimum solar elevation / time-of-day window for routine
  validation flights.
- [ ] Confirm whether spectral and spatial validation can be combined
  into a single overflight or must be flown separately.

---

## CALViS Fieldbook — [Protocols/Sensors/CALVIS/CALViS_FieldBook.md](Protocols/Sensors/CALVIS/CALViS_FieldBook.md)

- [ ] Add a link / model recommendation for the anemometer (e.g. Kestrel)
  ([line 105](Protocols/Sensors/CALVIS/CALViS_FieldBook.md#L105)).
- [ ] Resolve SWIR low-gain question with Headwall (more granular gain
  settings) and update the related note.
- [ ] Add wiki links for the GPT pipeline / `T1_proc` outputs
  ([line 564](Protocols/Sensors/CALVIS/CALViS_FieldBook.md#L564)).

## GOBI IF1200 Fieldbook — [Protocols/Sensors/GOBI/GOBI_IF1200_FieldBook.md](Protocols/Sensors/GOBI/GOBI_IF1200_FieldBook.md)

- [ ] Add a link / model recommendation for the anemometer (e.g. Kestrel)
  ([line 96](Protocols/Sensors/GOBI/GOBI_IF1200_FieldBook.md#L96)).
- [ ] Add wiki links for the GPT pipeline / `T1_proc` outputs
  ([line 439](Protocols/Sensors/GOBI/GOBI_IF1200_FieldBook.md#L439)).

## GOBI M350 Fieldbook — [Protocols/Sensors/GOBI/GOBI_M350_FieldBook.md](Protocols/Sensors/GOBI/GOBI_M350_FieldBook.md)

- [ ] Add wiki links for the GPT pipeline / `T1_proc` outputs
  ([line 432](Protocols/Sensors/GOBI/GOBI_M350_FieldBook.md#L432)).

## HiRes Fieldbook — [Protocols/Sensors/HIRES/HIRES_FieldBook.md](Protocols/Sensors/HIRES/HIRES_FieldBook.md)

Document-wide status: **Drafted, currently in EWG feedback**
(per [Protocols/STATUS.md](Protocols/STATUS.md)).

- [ ] Address EWG feedback and progress the document to the **Modified**
  stage.

**Season working plan — team responsibilities** (proposed — to be
confirmed by each node; mirrored in
[Season Working Plan](Protocols/Sensors/HIRES/HIRES_FieldBook.md#season-working-plan--team--outstanding-items))

- [ ] **UQ** — lead the photogrammetry pipeline build; contribute time
  and expertise.
- [ ] **Author (technical)** — contribute to the technical side of
  photogrammetry processing and Metashape settings.
- [ ] **James** — support pipeline development.
- [ ] **Dillon** — technical review (proposed).
- [ ] **Richard / Arden (USyd)** — support and advise (proposed).
- [ ] **CSU team** — provide technical input (proposed).
- [ ] **Bipul** — integration of tooling for image conversions, etc.
  (proposed).
- [ ] **Warin & Bipul** — lead non-photogrammetry pipeline; expand team
  as needed.

**Season working plan — critical outstanding items**

- [x] **APPN plot-extraction method** — agreed; see
  [Plot Delineation](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md).
- [ ] **Working team confirmation** — node leads to confirm named
  contributors for the photogrammetry pipeline.
- [ ] **PhaseOne SDK capability** — confirm scope of Image SDK
  functionality and resourcing for GUI / code expertise.
- [ ] **Boresight calibration** — decide whether to pursue as a means of
  improving image geo-location.

## M3M Fieldbook — [Protocols/Sensors/M3M/M3M_FieldBook.md](Protocols/Sensors/M3M/M3M_FieldBook.md)

Document-wide status: **Stub** — content placeholder only.

- [ ] Write the M3M fieldbook (equipment checklist, preflight,
  mission-standard types, camera capture settings, onsite preflight,
  flight ops, in-flight checks, post-flight, data offload, sensor
  configuration reference, GSD vs altitude lookup) — mirror the
  structure used by the HiRes and CALViS fieldbooks.

---

## Aerial Data QC — [Protocols/QA/QAprocess/AerialDataQC.md](Protocols/QA/QAprocess/AerialDataQC.md)

- [ ] Document the GCP-conversion process for each supported GCP type
  (Aeropoint, Trimble, …)
  ([line 188](Protocols/QA/QAprocess/AerialDataQC.md#L188)).
- [ ] Write the **Accuracy reporting** section
  ([line 324](Protocols/QA/QAprocess/AerialDataQC.md#L324)).
- [ ] Richard to check and update the **Create the Vector Layer** section
  ([line 377](Protocols/QA/QAprocess/AerialDataQC.md#L377)).
- [ ] Expand the QC procedure beyond the Cali Week 2026 lead-up so it
  becomes the standing standard for future flights.
- [ ] Extend QC coverage beyond hyperspectral drones.
- [ ] Update the naming-conventions table when panels other than GRYFN
  are sourced.
- [ ] Complete the **Positional QC** and **LiDAR QC** sections.

## Spectral Panel Cleaning and Calibration — [Protocols/QA/SpectralPanel/Spectral_Panel_Cleaning_and_Calibration.md](Protocols/QA/SpectralPanel/Spectral_Panel_Cleaning_and_Calibration.md)

Document-wide status: **Stub** — content placeholder only.

- [ ] Write the protocol covering: safe handling and storage of reference
  panels; routine cleaning procedures and approved consumables; pre- and
  post-flight panel capture workflows; recalibration intervals and
  traceability records; field QA checks and rejection criteria.

---

## Processing Pipelines — [Protocols/Pipelines/ProcessingPipelines/Processing_Pipelines.md](Protocols/Pipelines/ProcessingPipelines/Processing_Pipelines.md)

- [ ] CALViS walkthrough technical review by Richard Harwood
  ([line 36](Protocols/Pipelines/ProcessingPipelines/Processing_Pipelines.md#L36)).
- [ ] Add the **GOBI standard processing walkthrough** (currently outputs
  only; placeholder at
  [line 265](Protocols/Pipelines/ProcessingPipelines/Processing_Pipelines.md#L265)).
- [ ] Automate handling of GNSS `.TO4` files in the raw-data formatting
  step
  ([line 128](Protocols/Pipelines/ProcessingPipelines/Processing_Pipelines.md#L128)).

## HiRes Processing Pipeline — [Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md)

Document-wide status: **Stub / AI-scaffolded** — content not yet
validated (see CAUTION banner at
[lines 13–23](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#L13-L23)).
The current scaffold needs to be replaced with verified, operator-authored
instructions.

**Method 1 — PhaseOne iX Capture (Windows GUI)**
([line 126](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#L126))

- [ ] Document the iX Capture version pinned for APPN processing.
- [ ] Document exact GUI parameter presets and screenshots.
- [ ] Document export settings for handover to the orthomosaic stage.

**Method 2 — PhaseOne Image SDK (Linux CLI / shell scripts)**
([line 177](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#L177))

- [ ] Document the Image SDK version pinned for APPN processing.
- [ ] Add the reference shell pipeline (location in repo, invocation,
  env vars).
- [ ] Document parity checks against Method 1 (numerical equivalence
  tests).
- [ ] Document the container / environment (Conda / Docker) used for runs.

**Method 3 — Display-focused orthomosaic**
([line 234](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#L234))

- [ ] Confirm preferred photogrammetry tool and version.
- [ ] Document filename / folder convention so display products are
  clearly distinguishable from the standard `RGB_Orthomosaic.tif`.
- [ ] Document required watermark / metadata flag marking the product
  as "display only — not for quantitative use".

## M3M Processing Pipeline — [Protocols/Pipelines/M3MPipeline/M3M_Processing_Pipeline.md](Protocols/Pipelines/M3MPipeline/M3M_Processing_Pipeline.md)

Document-wide status: **Stub** — content placeholder only.

- [ ] Write the M3M processing pipeline documentation (toolchain, inputs,
  step sequence, outputs, QA checks).

---

## Background documents

### Ground-Based Phenotyping and Environmental Platforms — [Protocols/Background/PhenotypingAndEnvironmental/Ground_Phenotyping_and_Environmental.md](Protocols/Background/PhenotypingAndEnvironmental/Ground_Phenotyping_and_Environmental.md)

- [ ] Replace the placeholder section with the formal ground phenotyping
  / environmental protocols once they exist (currently intentional
  placeholder at
  [line 87](Protocols/Background/PhenotypingAndEnvironmental/Ground_Phenotyping_and_Environmental.md#L87)).

Other background documents (`Platforms_Overview.md`,
`QC_and_Reporting.md`, `Standard_Data_Products.md`) have no outstanding
inline TODOs.

---

## Top-level — [README.md](README.md) and [Scripts/README.md](Scripts/README.md)

- [ ] Update the `M3M/` and `HIRES/` "(stub)" annotations in the
  repository tree once those sensor fieldbooks are no longer stubs
  ([README.md line 29](README.md#L29)).

---

## Pending Field EWG approval

Items below are explicitly flagged in the source documents as requiring
APPN **Field EWG** review / ratification before they can be treated as
the APPN standard. (Fieldbooks, the Data Folder Structure document, and
the README files do not currently contain explicit Field EWG approval
gates.)

### Plot Delineation — [Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md)

Decisions ratified at the Field EWG plot-delineation meeting (file
format = GeoJSON, storage location, minimum attribute set, sensor in
filename) are captured at
[lines 36–55](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L36-L55).
Remaining EWG follow-ups:

- [ ] **Recommended buffer rule** — percentage vs "ditch a row", and
  associated species-specific guidance
  ([line 58](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L58)).
- [ ] **Optional column handling** in the plot shapefile (carry as
  empty vs omit)
  ([line 65](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L65)).
- [ ] **Metadata-capture approach** across the two delineation tools
  (which to standardise on)
  ([line 68](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L68)).
- [ ] **File naming convention** for plot-layout GeoJSONs (sensor
  identifier, special-case handling, per-sensor variants, ≤5 cm
  intra-sensor rule)
  ([lines 71–82](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L71-L82)).
- [ ] **Trial-information spreadsheet specification** and end-to-end
  join procedure
  ([lines 84–93](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md#L84-L93)).

### Standard Flight — [Protocols/FlightDesign/StandardFlight/Standard_Flight.md](Protocols/FlightDesign/StandardFlight/Standard_Flight.md)

Pending APEx / GRYFN decisions to be revised before season start
([lines 70–80](Protocols/FlightDesign/StandardFlight/Standard_Flight.md#L70-L80)):

- [ ] Flight-line orientation guidance (align-with-planting direction).
- [ ] Whether the Dual ELM panel flight is mandatory under variable
  illumination.
- [ ] Whether the Single ELM panel flight is permitted at all under
  variable illumination.

### Validation Flight — [Protocols/FlightDesign/ValidationFlight/Validation_Flight.md](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md)

Pending Field EWG / APEx decisions
([lines 82–94](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#L82-L94)):

- [ ] Confirm pass-fail / acceptance criteria for each validation
  flight type.
- [ ] Lock the standard validation flight footprint (area, altitude,
  speed, overlap) once APEx parameter sweeps complete.
- [ ] Confirm minimum solar elevation / time-of-day window for routine
  validation flights.
- [ ] Confirm whether spectral and spatial validation can be combined
  into a single overflight.
