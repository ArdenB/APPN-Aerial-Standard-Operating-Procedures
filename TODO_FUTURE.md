# APPN Aerial SOP — Future-Release Backlog (Rev 1.1+)

This document tracks work **deferred beyond revision 1.0**. Items land here
when they cannot be completed for the 1.0 cut because they depend on:

- **External processes** — Field EWG ratification, APEx parameter sweeps.
- **Field / design assets** — photos, diagrams, screenshots that must be
  produced on-site or in a design tool (tracked in detail in
  [IMAGE_TODO.md](IMAGE_TODO.md)).
- **Named owners** — sections explicitly assigned to a specific person.
- **Documents not in scope for 1.0** — stubs planned for a later revision.

The live, must-clear-for-1.0 list is in [TODO.md](TODO.md). When an item
here becomes actionable, move it back into `TODO.md` (or complete it
directly) and update [Protocols/STATUS.md](Protocols/STATUS.md) /
[publish.yaml](publish.yaml) as appropriate.

---

## 1. Documents deferred to a future revision

These pages are **not part of revision 1.0**. They remain stubs / scaffolds
and are flagged in [Protocols/STATUS.md](Protocols/STATUS.md) as such. Each
ships in 1.0 with a clear "planned for a future revision" banner rather than
unvalidated content.

### M3M Fieldbook — [Protocols/Sensors/M3M/M3M_FieldBook.md](Protocols/Sensors/M3M/M3M_FieldBook.md)

- [ ] Write the M3M fieldbook (equipment checklist, preflight,
  mission-standard types, camera capture settings, onsite preflight,
  flight ops, in-flight checks, post-flight, data offload, sensor
  configuration reference, GSD vs altitude lookup) — mirror the structure
  used by the HiRes and CALViS fieldbooks.

### Spectral Panel Cleaning and Calibration — [Protocols/QA/SpectralPanel/Spectral_Panel_Cleaning_and_Calibration.md](Protocols/QA/SpectralPanel/Spectral_Panel_Cleaning_and_Calibration.md)

- [ ] Write the protocol covering: safe handling and storage of reference
  panels; routine cleaning procedures and approved consumables; pre- and
  post-flight panel capture workflows; recalibration intervals and
  traceability records; field QA checks and rejection criteria.

### HiRes Processing Pipeline — [Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md](Protocols/Pipelines/HiResPipeline/HiRes_Processing_Pipeline.md)

Replace the AI-scaffolded content with verified, operator-authored
instructions.

- [ ] **Method 1 — PhaseOne iX Capture (Windows GUI):** pin the iX Capture
  version, document exact GUI parameter presets + screenshots, and document
  export settings for handover to the orthomosaic stage.
- [ ] **Method 2 — PhaseOne Image SDK (Linux CLI):** pin the Image SDK
  version, add the reference shell pipeline (repo location, invocation, env
  vars), document parity checks against Method 1, and document the
  container / environment (Conda / Docker) used for runs.
- [ ] **Method 3 — Display-focused orthomosaic:** confirm the preferred
  photogrammetry tool + version, document the filename / folder convention
  distinguishing display products from the standard `RGB_Orthomosaic.tif`,
  and document the required watermark / metadata flag
  ("display only — not for quantitative use").

### M3M Processing Pipeline — [Protocols/Pipelines/M3MPipeline/M3M_Processing_Pipeline.md](Protocols/Pipelines/M3MPipeline/M3M_Processing_Pipeline.md)

- [ ] Write the M3M processing pipeline documentation (toolchain, inputs,
  step sequence, outputs, QA checks).

### Ground-Based Phenotyping and Environmental Platforms — [Protocols/Background/PhenotypingAndEnvironmental/Ground_Phenotyping_and_Environmental.md](Protocols/Background/PhenotypingAndEnvironmental/Ground_Phenotyping_and_Environmental.md)

- [ ] Replace the placeholder section with the formal ground phenotyping /
  environmental protocols once they exist.

---

## 2. Pending Field EWG approval

Items explicitly flagged in source documents as requiring APPN **Field EWG**
review / ratification before they can be treated as the APPN standard.

### Standard Flight — [Protocols/FlightDesign/StandardFlight/Standard_Flight.md](Protocols/FlightDesign/StandardFlight/Standard_Flight.md)

- [ ] Flight-line orientation guidance (align-with-planting direction).
- [ ] Whether the Dual ELM panel flight is mandatory under variable
  illumination.
- [ ] Whether the Single ELM panel flight is permitted at all under
  variable illumination.

### Validation Flight — [Protocols/FlightDesign/ValidationFlight/Validation_Flight.md](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md)

- [ ] Confirm pass-fail / acceptance criteria for each validation flight
  type.
- [ ] Confirm the **frequency** of each validation flight type.
- [ ] Confirm equipment checklists with field operators for all three
  validation flight types.

---

## 3. Pending APEx / GRYFN parameter decisions (revise before season start)

These need data from APEx parameter sweeps or a GRYFN decision before they
can be locked.

### Standard Flight

- [ ] Confirm the season-start parameter set and the "single offload per
  flight" rule with APEx.

### Validation Flight

- [ ] Lock the standard validation flight footprint (area, altitude, speed,
  overlap) once APEx parameter sweeps complete.
- [ ] Confirm minimum solar elevation / time-of-day window for routine
  validation flights.
- [ ] Confirm whether spectral and spatial validation can be combined into a
  single overflight or must be flown separately.

---

## 4. Sections owned by named contributors

### CALViS Fieldbook — [Protocols/Sensors/CALVIS/CALViS_FieldBook.md](Protocols/Sensors/CALVIS/CALViS_FieldBook.md)

- [ ] **APEx in-field testing:** evaluate whether to keep the ±20° solar-noon
  window or adopt the GRYFN solar-altitude recommendation (latitude-dependent).
  Tests are planned as part of the APEx experimental flights this season.
- [ ] Add a reference image and notes covering the recommended sensor angle
  during exposure setting (see [IMAGE_TODO.md](IMAGE_TODO.md)).

### Aerial Data QC — [Protocols/QA/QAprocess/AerialDataQC.md](Protocols/QA/QAprocess/AerialDataQC.md)

- [ ] Richard to check and update the **Create the Vector Layer** section.

### Plot Delineation — [Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md](Protocols/PlotProtocols/PlotDelineation/Plot_Delineation.md)

- [ ] **Method cross-validation (Zeljana Grbovic):** confirm that all three
  methods (FIELDimageR, DPIRD Field Mapping Tool, GPT) produce consistent
  results; fold any required changes back into the protocol.
- [ ] Improve the FIELDimageR corner-coordinate fitting workflow (currently
  iterative).

### HiRes Fieldbook — [Protocols/Sensors/HIRES/HIRES_FieldBook.md](Protocols/Sensors/HIRES/HIRES_FieldBook.md)

Season working plan — team responsibilities (to be confirmed by each node):

- [ ] **UQ** — lead the photogrammetry pipeline build.
- [ ] **Author (technical)** — contribute to photogrammetry processing /
  Metashape settings.
- [ ] **James** — support pipeline development.
- [ ] **Dillon** — technical review (proposed).
- [ ] **Richard / Arden (USyd)** — support and advise (proposed).
- [ ] **CSU team** — provide technical input (proposed).
- [ ] **Bipul** — integration of tooling for image conversions (proposed).
- [ ] **Warin & Bipul** — lead non-photogrammetry pipeline.

Season working plan — critical outstanding items:

- [ ] **Working team confirmation** — node leads to confirm named
  contributors for the photogrammetry pipeline.
- [ ] **PhaseOne SDK capability** — confirm scope of Image SDK functionality
  and resourcing for GUI / code expertise.
- [ ] **Boresight calibration** — decide whether to pursue as a means of
  improving image geo-location.

Field procedure:

- [ ] **Gimbal Balancing** — write the step-by-step P3 gimbal-balance
  procedure (currently stubbed; assigned to @franco) and add the
  accompanying photo sequence + final settings-table reference (see
  [IMAGE_TODO.md](IMAGE_TODO.md)).

### Aerial Data QC — future scope expansion

- [ ] Expand the QC procedure beyond the Cali Week 2026 lead-up so it becomes
  the standing standard for future flights.
- [ ] Extend QC coverage beyond hyperspectral drones.
- [ ] Update the naming-conventions table when panels other than GRYFN are
  sourced.
- [ ] Complete the **Positional QC** and **LiDAR QC** sections.
- [ ] Confirm the provisional positional-accuracy thresholds (caution at 5 cm
  RMSE, fail at 10 cm RMSE) during the APEx flights.
- [ ] Develop the **Spectral QC** accuracy-reporting procedure and an
  acceptable spectral accuracy baseline using the APEx flights.
- [ ] Develop the **LiDAR QC** sampling and accuracy-reporting procedures and
  an acceptable LiDAR accuracy baseline using the APEx flights.
- [ ] Document the GCP-conversion process for each supported GCP type
  (Aeropoint, Trimble, …).

---

## 5. Operational parameters still to be defined

### Standard Flight — [Protocols/FlightDesign/StandardFlight/Standard_Flight.md](Protocols/FlightDesign/StandardFlight/Standard_Flight.md)

- [ ] Maximum permissible wind speed per UAV / sensor combination.
- [ ] Minimum acceptable solar elevation for routine surveys.
- [ ] Standard exposure-setting procedure (cross-link once finalised in the
  sensor fieldbooks).

### Validation Flight — [Protocols/FlightDesign/ValidationFlight/Validation_Flight.md](Protocols/FlightDesign/ValidationFlight/Validation_Flight.md)

- [ ] Confirm minimum solar elevation and maximum permissible wind for
  validation flights.
- [ ] Insert the exposure-setting procedure for the spectral validation
  flights (referenced in two procedure blocks).
- [ ] Specify required **weather station** and **downwelling radiation
  sensor** models.
- [ ] Add guidance on minimum site footprint and on documenting site
  selection.
- [ ] Link to a standard validation flight log template.

---

## 6. Figure / image backlog

All photos, diagrams, screenshots, and charts are tracked in detail in
[IMAGE_TODO.md](IMAGE_TODO.md) (30 items). These require field capture or
design-tool work and are deferred as a batch to a future revision unless
captured opportunistically before the 1.0 cut.
