# Image TODO — Master List

This document tracks all photos, diagrams, and screenshots that are
either explicitly requested by an existing TODO in the protocols, or
suggested as a useful addition where no current note exists.

**Type legend**
- **Diagram** — annotated map / schematic / line-art (e.g. top-down
  flight-design layout).
- **Photo** — field photograph of real equipment, setup, or site.
- **Screenshot** — capture of a software UI (GPT, iX Capture, DJI
  Pilot 2, QGroundControl, etc.).
- **Chart** — exported plot or QC visualisation (e.g. matplotlib PNG).

Each item is tagged **Explicit** (the document already flags a missing
image) or **Suggested** (no current note in the doc — added here
because an image would clearly help).

---

## Standard Flight — [Protocols/FlightDesign/StandardFlight/Standard_Flight.md](Protocols/FlightDesign/StandardFlight/Standard_Flight.md)

- [ ] **Photo** · *Suggested* — [Standard Flight overview](Protocols/FlightDesign/StandardFlight/Standard_Flight.md): Hero/cover photo of a complete, correctly-staged standard flight site (drone + panel table + GCPs visible) usable as the reference ideal.

## Validation Flight — [Protocols/FlightDesign/ValidationFlight/Validation_Flight.md](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md)

- [ ] **Diagram** · *Explicit* — [Spectral validation flight](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#spectral-validation-flight): Annotated layout with dual ELM panel placements, validation panel position, N–S flight-line orientation, and 5-GCP layout.
- [ ] **Diagram** · *Explicit* — [Spatial validation flight](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#spatial-validation-flight): Annotated layout with extended GCP distribution, paired elevated / ground GCPs, and any independently-surveyed check targets.
- [ ] **Diagram** · *Explicit* — [APEx experimental flight](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#apex-experimental-flight): Annotated reference layout (spectral validation footprint with standard panel/GCP positions) used as the parameter-sweep baseline.
- [ ] **Photo** · *Suggested* — [Site selection](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#site-selection): Example validation site — uniform crop or grass cover, fixed repeatable location, clear of tall obstructions.
- [ ] **Chart** · *Suggested* — [Acceptance criteria](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md#acceptance-criteria): Sample QC plot of spectral validation metrics over time (panel-derived reflectance drift, band-to-band offsets, spectroradiometer–UAV mismatch) annotated as pass vs fail.

## HiRes Field Book — [Protocols/Sensors/HIRES/HIRES_FieldBook.md](Protocols/Sensors/HIRES/HIRES_FieldBook.md)

- [ ] **Photo** · *Explicit* — [Gimbal Balancing](Protocols/Sensors/HIRES/HIRES_FieldBook.md#gimbal-balancing): Step-by-step photo sequence of P3 gimbal-balance adjustment points, plus reference photo of the final settings table (steps currently stubbed `X / Y / Z / P / Q`).
- [ ] **Screenshot** · *Explicit* — [Drone Centre of Gravity Calibration](Protocols/Sensors/HIRES/HIRES_FieldBook.md#drone-centre-of-gravity-calibration): DJI Pilot 2 UI screenshot of the **Center of Gravity Auto Calibration** section (Calibrate button + post-calibration prompt).
- [ ] **Photo** · *Explicit* — [Drone Centre of Gravity Calibration](Protocols/Sensors/HIRES/HIRES_FieldBook.md#drone-centre-of-gravity-calibration): Companion field photo of the aircraft hovering in a windless environment during calibration.
- [ ] **Photo** · *Suggested* — [Equipment Checklist](Protocols/Sensors/HIRES/HIRES_FieldBook.md#equipment-checklist): Sensor mounting on the M350 — close-up showing connector orientation, lens-cap removal, and locking-pin engagement.
- [ ] **Photo** · *Suggested* — [Equipment Checklist](Protocols/Sensors/HIRES/HIRES_FieldBook.md#equipment-checklist): Pre-flight hero photo of the assembled HiRes payload + M350 in the "ready-to-fly" state.

## GOBI M350 Field Book — [Protocols/Sensors/GOBI/GOBI_M350_FieldBook.md](Protocols/Sensors/GOBI/GOBI_M350_FieldBook.md)

- [ ] **Photo** · *Suggested* — Sensor mounting close-up: GOBI on M350 quick-release with cable routing and SD/SSD slot visible.
- [ ] **Photo** · *Suggested* — Powering-on / boot-LED reference photo so operators can confirm a healthy state.

## GOBI IF1200 Field Book — [Protocols/Sensors/GOBI/GOBI_IF1200_FieldBook.md](Protocols/Sensors/GOBI/GOBI_IF1200_FieldBook.md)

- [ ] **Photo** · *Suggested* — IF1200 + GOBI assembled airframe photo with payload, antennas, and battery bay annotated.
- [ ] **Photo** · *Suggested* — Ground-station setup photo (RC, tablet, telemetry mast).

## CALViS Field Book — [Protocols/Sensors/CALVIS/CALViS_FieldBook.md](Protocols/Sensors/CALVIS/CALViS_FieldBook.md)

- [ ] **Photo** · *Suggested* — CALViS sensor head close-up showing fibre routing and downwelling sensor orientation.
- [ ] **Photo** · *Suggested* — Field-deployed CALViS rig with downwelling sensor levelled and unobstructed.

## M3M Field Book (stub) — [Protocols/Sensors/M3M/M3M_FieldBook.md](Protocols/Sensors/M3M/M3M_FieldBook.md)

- [ ] **Photo** · *Suggested* — Platform overview: Mavic 3M with multispectral payload, labelled.
- [ ] **Photo** · *Suggested* — Equipment checklist flat-lay (controller, batteries, panels, SD cards).
- [ ] **Photo** · *Suggested* — Calibration target deployment (multispectral panel pre-/post-flight capture).
- [ ] **Screenshot** · *Suggested* — In-flight DJI Pilot mission monitoring view.

## Processing Pipelines (overview) — [Protocols/Pipelines/GryfnProcessingPipeline/Gryfn_Processing_Pipeline.md](Protocols/Pipelines/GryfnProcessingPipeline/Gryfn_Processing_Pipeline.md)

- [ ] **Screenshots** · *Explicit* — [GOBI — Standard Processing Pipeline](Protocols/Pipelines/GryfnProcessingPipeline/Gryfn_Processing_Pipeline.md#-gobi--standard-processing-pipeline): Step-by-step GPT screenshots — polygon import → exposure setting → ELM panel selection → pipeline submission — matching the level of detail used in the CALViS section.

## HiRes Processing Pipeline — [Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md)

- [ ] **Screenshot** · *Explicit* — [Method 1 — PhaseOne iX Capture](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#method-1--phaseone-ix-capture-windows-gui): iX Capture GUI showing camera-calibration profile load.
- [ ] **Screenshot** · *Explicit* — [Method 1 — PhaseOne iX Capture](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#method-1--phaseone-ix-capture-windows-gui): LCC (Light Calibration / flat-field) correction step in the GUI.
- [ ] **Screenshot** · *Explicit* — [Method 1 — PhaseOne iX Capture](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#method-1--phaseone-ix-capture-windows-gui): Export-settings dialog for calibrated GeoTIFF / DNG output.
- [ ] **Screenshot** · *Explicit* — [Method 2 — PhaseOne Image SDK](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#method-2--phaseone-image-sdk-linux-cli--shell-scripts): Terminal screenshot of the reference shell-pipeline invocation (env vars, command line, expected log output).
- [ ] **Screenshot** · *Explicit* — [Method 2 — PhaseOne Image SDK](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#method-2--phaseone-image-sdk-linux-cli--shell-scripts): Sample structured processing report (parameters, versions, run time, checksums).
- [ ] **Screenshot** · *Explicit* — [Method 3 — Display-focused orthomosaic](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#method-3--display-focused-orthomosaic): Photogrammetry-software UI (Metashape / ODM) showing HiRes frame alignment and ortho settings.
- [ ] **Photo / Image** · *Explicit* — [Method 3 — Display-focused orthomosaic](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md#method-3--display-focused-orthomosaic): Example display-focused RGB orthomosaic output, watermarked "DISPLAY ONLY".

## M3M Processing Pipeline (stub) — [Protocols/Pipelines/M3MPipeline/M3M_Processing_Pipeline.md](Protocols/Pipelines/M3MPipeline/M3M_Processing_Pipeline.md)

- [ ] **Screenshots** · *Suggested* — GPT workflow for multispectral input (band selection, ELM, pipeline submission).
- [ ] **Photo / Chart** · *Suggested* — Example outputs: multispectral orthomosaic + NDVI / vegetation-index preview.

## Spectral Panel Cleaning & Calibration (stub) — [Protocols/QA/SpectralPanel/Spectral_Panel_Cleaning_and_Calibration.md](Protocols/QA/SpectralPanel/Spectral_Panel_Cleaning_and_Calibration.md)

- [ ] **Photo** · *Suggested* — Correct vs incorrect panel handling (gloved edge-grip vs fingers on surface).
- [ ] **Photo** · *Suggested* — Approved cleaning consumables (microfibre, solvent bottle) laid out.
- [ ] **Photo** · *Suggested* — Panel storage / protective case (open + closed) showing correct stacking.
- [ ] **Photo** · *Suggested* — Pre- and post-flight panel-capture workflow on tripod / table.
- [ ] **Photo** · *Suggested* — Field QA inspection: surface contamination, scratches, specular highlights.

---

## Summary by type

| Type        | Explicit | Suggested | Total |
| ----------- | -------- | --------- | ----- |
| Diagram     | 2        | 0         | 2     |
| Photo       | 2        | 14        | 16    |
| Screenshot  | 8        | 2         | 10    |
| Chart       | 0        | 2         | 2     |
| **Total**   | **12**   | **18**    | **30** |

> Counts include the "Photo / Image" item under Method 3 as a Photo and
> the "Photo / Chart" item under M3M as a Photo. Adjust if recategorised.
