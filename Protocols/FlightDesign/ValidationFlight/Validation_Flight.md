# Validation Flight Procedure

> [!IMPORTANT]
> This protocol outlines the **validation flight procedures** used to
> periodically check that APPN aerial payloads (GOBI, CALViS) remain
> within spectral and spatial calibration, and to support the APPN
> APEx experimental program. It defines three validation flight types,
> each with its own purpose, frequency, and acceptance criteria.
>
> Validation flights are intended to be flown:
>
> - At **regular intervals** by every node, so that data products
>   remain comparable across nodes and over time.
> - **Any time a sensor is returned to service** after repairs,
>   firmware updates, or other maintenance.
> - **Whenever a flight parameter is being formally tested** under the
>   APEx program.
>
> For routine operational surveys, see the
> [Standard Flight Procedure](../StandardFlight/Standard_Flight.md).
>
> For sensor-specific equipment, procedures, and safety information,
> see the relevant sensor fieldbook:
>
> - [CALViS Fieldbook](../../Sensors/CALVIS/CALViS_FieldBook.md)
> - [GOBI M350 Fieldbook](../../Sensors/GOBI/GOBI_M350_FieldBook.md)
> - [GOBI IF1200 Fieldbook](../../Sensors/GOBI/GOBI_IF1200_FieldBook.md)

---

> [!CAUTION]
> **This document is being completely restructured.**
> Section ordering, scope, and procedural detail will all change in
> upcoming revisions. Treat the material below as a placeholder
> scaffold only and do not rely on the current content for field use
> until this notice is removed.
>
> Reworking of this document will occur as part of early-season APEx
> work. Any validation flights flown in the meantime should follow the
> [Standard Flight Procedure](../StandardFlight/Standard_Flight.md).

---

> [!IMPORTANT]
> **Document status — work in progress.**
> This protocol is a draft and requires further revision before it can
> be considered final. New figures also need to be produced to
> illustrate the procedures described below.
>
> **Outstanding TODOs:**
>
> **Content review**
> - [ ] Define and confirm the **frequency** of each validation flight
>       type (currently `_TODO_`).
> - [ ] Confirm the **acceptance criteria / pass-fail thresholds** for
>       each validation flight type with the Field EWG.
> - [ ] Cross-check terminology and links against the sensor fieldbooks
>       and the [Standard Flight Procedure](../StandardFlight/Standard_Flight.md).
> - [ ] Confirm equipment checklists with field operators (all three
>       validation flight types).
>
> **Figures to produce** (see master list in [`/IMAGE_TODO.md`](../../../IMAGE_TODO.md))
> - [ ] **Diagram** — Spectral validation flight: panel layout,
>       flight-line orientation, and GCP distribution.
> - [ ] **Diagram** — Spatial validation flight: GCP layout (including
>       elevated / paired GCPs), flight-line geometry, and any check
>       targets.
> - [ ] **Diagram** — APEx experimental flight: reference layout used
>       as the starting point for parameter sweeps.
> - [ ] **Photo (suggested)** — Example validation site with uniform
>       crop cover, fixed repeatable location, clear of tall
>       obstructions (see [Site selection](#site-selection)).
> - [ ] **Chart (suggested)** — Sample QC plot showing spectral
>       validation metrics (e.g. panel-derived reflectance drift,
>       band-to-band offsets) annotated as pass vs fail (see
>       [Acceptance criteria](#acceptance-criteria)).
>
> **Cross-links to add**
> - [ ] Processing pipeline page describing how validation outputs are
>       analysed (radiometric drift, geometric error reports).
> - [ ] QA process page describing how validation results feed into
>       the node-level QA record.
>
> **Pending APEx decisions (revise before season start)**
> - [ ] Lock the standard validation flight footprint (area, altitude,
>       speed, overlap) once APEx parameter sweeps complete.
> - [ ] Confirm minimum solar elevation / time-of-day window for
>       routine validation flights.
> - [ ] Confirm whether spectral and spatial validation can be
>       combined into a single overflight or must be flown separately.

---

## Document Structure

This protocol is organised into two parts:

1. **[Background and common elements of all validation flights](#background-and-common-elements-of-all-validation-flights)** —
   shared setup rules that apply to every validation flight design:
   - [Site selection](#site-selection)
   - [Flight-line orientation and timing](#flight-line-orientation-and-timing)
   - [Panel setup](#panel-setup)
   - [Ground Control Points](#ground-control-points)
   - [Records and metadata](#records-and-metadata)
2. **The three validation flight types**, each with its own overview,
   when-to-use criteria, flight-design notes, and equipment list:
   - [Spectral validation flight](#spectral-validation-flight) —
     periodic check that the radiometric / spectral response of the
     sensor remains within tolerance and is comparable across nodes.
   - [Spatial validation flight](#spatial-validation-flight) —
     periodic check on geometric accuracy (horizontal, vertical, and
     across-track / between-flight-line registration).
   - [APEx experimental flight](#apex-experimental-flight) —
     parameter-sweep flights used by the APPN APEx program to test
     and refine flight settings, sensor configuration, and processing
     options.

---

## Background and common elements of all validation flights

> [!IMPORTANT]
> This section describes the **placement of GCPs and reflectance
> panels, site selection, and metadata recording** that is common to
> all validation flight types described below.
>
> All placements given here (distances, positions, panel locations,
> GCP distributions) are **approximate guidelines, not strict
> requirements**. Operators should adapt the layout to the realities
> of the site:
>
> - Use the **nearest existing path, bare strip, or tramline** to
>   access and place panels and GCPs.
> - **Do not place panels or GCPs inside experimental plots** or
>   anywhere they would damage the crop, disturb a treatment, or
>   obstruct other field operations.
> - Keep panels and GCPs clear of shadows (from trees, infrastructure,
>   the operator, or the UAV itself) and away from the take-off /
>   landing zone.

> [!CAUTION]
> **Keep panels and GCPs away from the edge of the capture window.**
>
> Depending on the exact flight parameters (altitude, overlap, turn
> geometry), GOBI and CALViS can fail to capture data in the
> outermost portion of the planned capture polygon. Place all
> validation targets inside an **effective capture area** set back
> from each edge of the planned polygon.
>
> See the
> [Standard Flight Procedure background section](../StandardFlight/Standard_Flight.md#background-and-common-elements-of-all-standard-flights)
> for the full rationale and the recommended ~10% inset.

### Site selection

Validation flights can be flown over any safe and convenient location,
but should ideally be flown:

- Over a **closed crop canopy or uniform grass cover** wherever
  possible, to provide a stable spectral and structural reference.
- At a **fixed, repeatable site at each node**, so that successive
  validation flights can be compared directly without site effects
  confounding the result.
- Clear of nearby tall obstructions (trees, sheds, powerlines) that
  would cast shadows or restrict flight-line geometry.

> _TODO: Add guidance on minimum site footprint, and on documenting
> the chosen validation site at each node._

> [!NOTE]
> 🖼️ **Image needed (photo, suggested):** Example field photograph
> of an appropriate validation site — uniform crop or grass cover,
> fixed repeatable location at the node, clear of tall obstructions —
> to anchor the site-selection criteria above.

### Flight-line orientation and timing

- Default flight-line orientation is **North–South**, flown as close
  as practical to **solar noon**.
- Record the **actual flight-line orientation, start time, and end
  time** for every validation flight. Validation flights are only
  comparable across nodes and over time if these parameters are
  consistent — and where they cannot be, they must be logged.

> _TODO: Confirm minimum solar elevation, maximum permissible wind
> speed, and any other go / no-go weather criteria for validation
> flights, once APEx results are available._

### Panel setup

The panel setup for validation flights follows the same rules as for
operational surveys — see
[Panel Setup](../StandardFlight/Standard_Flight.md#panel-setup) and
[Validation Panel Setup](../StandardFlight/Standard_Flight.md#validation-panel-setup)
in the Standard Flight Procedure for the full procedure (table,
levelling, ordering, orientation, height recording, paired GCP).

The key validation-specific points are:

- Validation flights **always include the GRYFN 2-panel validation
  set** with its paired elevated + ground GCPs.
- Where two ELM panel sets are available, both should be deployed
  (see the
  [Dual ELM panel flight](../StandardFlight/Standard_Flight.md#dual-elm-panel-flight)
  layout).
- Panel positions and the **panel surface height above the ground**
  must be recorded for every validation flight.

### Ground Control Points

Validation flights use the same minimum **5-GCP layout** described in
the Standard Flight Procedure
([Ground Control Points](../StandardFlight/Standard_Flight.md#ground-control-points)),
with **at least one GCP placed inside each flight line** and the
paired elevated + ground GCPs at the validation panel table.

Additional GCPs are encouraged for validation flights, since the
purpose of the flight is precisely to measure spatial accuracy.

### Records and metadata

For every validation flight, record (at minimum):

- **Flight identifier**, node, operator, date, and start / end time.
- **Sensor and platform** (including firmware / software versions).
- **Site identifier** and any deviations from the standard site.
- **Flight parameters** actually flown (altitude, speed, overlap,
  flight-line angle).
- **Weather**: cloud cover, wind speed and direction, air temperature,
  approximate solar elevation.
- **Panel configuration**: number of panel sets, table heights,
  position relative to flight lines.
- **GCP layout**: positions and any deviations from the standard
  5-GCP layout.
- **Reason for the flight**: scheduled interval, post-maintenance
  check, APEx experiment, etc.

> _TODO: Link this to a standard validation flight log template /
> wiki page once available._

---

## Spectral validation flight

### Overview

The spectral validation flight is a periodic check that the
**radiometric and spectral response** of the GOBI and CALViS payloads
remains within tolerance — both against itself over time, and against
other nodes flying the equivalent payload.

**Rationale:**

- **Drift detection.** Detects gradual changes in sensor response
  (e.g. due to ageing optics, panel degradation, or seasonal
  illumination differences) before they affect operational data
  quality.
- **Inter-node comparability.** Provides a common reference flight
  pattern that lets every node check that its calibrated reflectance
  products agree with those of other nodes flying the same payload.
- **Post-maintenance check.** Confirms that a sensor returned to
  service after repair, replacement, or firmware change still
  produces reflectance values consistent with its pre-maintenance
  baseline.

**When to use this flight:**

- At **regular intervals** by every node — _TODO: define interval
  (e.g. monthly during the field season, quarterly out of season)._
- **Any time a sensor is returned to service** after repairs,
  firmware updates, or replacement of optical components.
- Whenever the **standard radiometric panels** are replaced,
  re-characterised, or otherwise changed.

### Flight design

> [!NOTE]
> 🖼️ **Image needed (diagram):** Top-down annotated diagram of the
> spectral validation flight layout — panel placement (dual ELM where
> available), validation panel position, flight-line orientation and
> overlap, and the 5-GCP layout.

> _TODO: Insert annotated diagram showing the spectral validation
> flight layout — panel placement (dual ELM where available),
> validation panel position, flight-line orientation and overlap, and
> the 5-GCP layout._

The current draft layout is the dual-panel flight described in the
Standard Flight Procedure, flown over the node's fixed validation
site. Specifically:

- **Survey footprint:** approximately **7,200 m² (60 m × 120 m)**
  rectangle (working draft — to be locked once APEx parameter sweeps
  complete).
- **Flight lines:** 5 lines, oriented North–South by default, flown
  close to solar noon.
- **Panels:** GRYFN 4-panel ELM sets at ~30% along flight line 1 and
  ~30% along flight line 4 (the second set captured under a different
  flight-line direction relative to the first); GRYFN 2-panel
  validation set near the centre of flight line 3.
- **GCPs:** one GCP per flight line in a diagonal pattern at 10%,
  30%, 50%, 70%, and 90% of the line, plus the paired elevated /
  ground GCP at the validation panel table.

![Spectral validation flight panel layout (legacy placeholder figure — to be replaced)](Validation_Flight_media/image_d43bd2392053.jpg)

> [!NOTE]
> 🖼️ **Image needed (diagram):** The figure above is a **legacy
> placeholder** retained only so the section is not blank. Replace
> with a new annotated top-down diagram of the spectral validation
> flight — dual ELM panel placements, validation panel position, N–S
> flight-line orientation, edge buffer, and the 5-GCP layout, plus a
> legend for GCPs, GRYFN reflectance panel sets, and the independent
> validation panel. Tracked in [IMAGE_TODO.md](../../../IMAGE_TODO.md).

#### IF1200 + CALViS or GOBI flight parameters _(draft)_

1. Using QGroundControl, set up a new flight mission at the node's
   fixed validation site.
2. Create a rectangular survey area of approximately **6,200 m²**.
   1. Export the polygon and import it into the *HPI Polygon Tool*.
3. Use the parameters below for flight planning in QGroundControl:

   | Parameter            | Setting                                |
   | -------------------- | -------------------------------------- |
   | Altitude             | 50 m                                   |
   | Flight speed         | 3.2 m/s                                |
   | Trigger Distance     | Leave as default (number is irrelevant)|
   | Spacing              | 12 m                                   |
   | Angle                | 180°                                   |
   | Turnaround Distance  | 10 m                                   |

4. Load this mission onto the IF1200.
5. **TODO: Insert exposure-setting procedure for the spectral
   validation flight.**

#### DJI M350 RTK + GOBI flight parameters _(draft)_

1. Using DJI Pilot 2, set up a new flight mission at the node's fixed
   validation site.
2. Create a rectangular survey area of approximately **6,200 m²**.
3. Create a smaller rectangular *capture* polygon inside the *survey*
   polygon, inset by approximately **2 × the flight speed (~7 m)** in
   the direction of flight. The figure below outlines this — the red
   polygon is the *capture* polygon, the yellow is the *survey*
   polygon.

   ![Capture vs survey polygon](Validation_Flight_media/image_154a62ad07f2.png)

   1. Export the polygon and import it into the
      [HPI Polygon Tool](http://apps.headwallphotonics.com/).

4. Use the parameters below for flight planning in DJI Pilot 2:

   | Parameter             | Setting |
   | --------------------- | ------- |
   | Altitude              | 50 m    |
   | Flight speed          | 3.2 m/s |
   | Side Overlap          | 49%     |
   | Frontal Overlap Ratio | 80%     |
   | Course Angle          | 180°    |
   | Margin                | 0       |
   | Elevation Optimisation| FALSE   |

5. **TODO: Insert exposure-setting procedure for the spectral
   validation flight.**

### Acceptance criteria

> [!NOTE]
> 🖼️ **Image needed (chart, suggested):** Sample QC chart (e.g.
> exported plot) showing spectral validation metrics over time —
> panel-derived reflectance drift, band-to-band offsets,
> spectroradiometer–UAV mismatch — with the pass/fail thresholds
> annotated.

> _TODO: Define quantitative pass / fail thresholds for the spectral
> validation flight (e.g. maximum drift in panel-derived reflectance,
> maximum band-to-band offset, maximum spectroradiometer–UAV
> mismatch)._

### Ground Equipment Required

- [ ] UAV, controller, and batteries
- [ ] GOBI or CALViS payload
- [ ] 2 × GRYFN 4-panel ELM set (11%, 30%, 56%, 82%)
      — if only 1 is available, fall back to the single-panel layout
- [ ] 1 × GRYFN 2-panel validation set (20%, 45%)
- [ ] 5 × Propeller Aeropoints or equivalent GCPs
- [ ] 2 × Folding tables (1 per panel set)
- [ ] Spirit level (to level the tables)
- [ ] Tape measure
- [ ] Optional spectroradiometer (SVC, FieldSpec) for an independent
      spectral reference
- [ ] Downwelling radiation sensor _(TODO: add details)_
- [ ] Weather station _(TODO: add details)_

> [!IMPORTANT]
> All other equipment listed in the relevant sensor fieldbook is also
> required.

---

## Spatial validation flight

### Overview

The spatial validation flight is a periodic check on the **geometric
accuracy** of the GOBI and CALViS payloads — covering horizontal
position, vertical / elevation accuracy, and across-track or
between-flight-line registration.

**Rationale:**

- **Detects geometric drift.** Picks up changes in IMU / GNSS /
  boresight alignment that would otherwise show up only as subtle
  stitching errors in operational products.
- **Validates the standard 5-GCP layout.** Confirms that the GCP
  configuration recommended in the Standard Flight Procedure is
  actually resolving the spatial errors it is intended to detect.
- **Post-maintenance check.** Confirms that a sensor returned to
  service after physical disassembly, mount changes, or boresight
  recalibration still produces geometrically consistent products.

**When to use this flight:**

- At **regular intervals** by every node — _TODO: define interval._
- **Any time** a sensor or its mount has been physically disturbed
  (e.g. boresight recalibration, lens / optics swap, IMU replacement,
  remount on a different airframe).
- After any **firmware or processing-software update** that could
  affect georeferencing.

### Flight design

> [!NOTE]
> 🖼️ **Image needed (diagram):** Top-down annotated diagram of the
> spatial validation flight layout — expanded GCP distribution,
> paired elevated / ground GCPs, and any additional check targets
> used to characterise across-track and vertical error.

> _TODO: Insert annotated diagram showing the spatial validation
> flight layout — extended GCP distribution, paired elevated / ground
> GCPs, and any additional check targets used to characterise
> across-track and vertical error._

Working draft layout:

- Same survey footprint and flight-line geometry as the
  [Spectral validation flight](#spectral-validation-flight) (so that
  the two validations can be flown back-to-back at the same site if
  scheduling allows).
- **Expanded GCP layout:** the standard 5-GCP layout (one per flight
  line in a diagonal pattern) **plus** additional GCPs near the
  corners and at off-axis positions between flight lines, to give
  redundant checks on each spatial-error mode described in the
  [Standard Flight GCP rationale](../StandardFlight/Standard_Flight.md#ground-control-points).
- **Paired elevated + ground GCPs** at the validation panel table to
  check vertical accuracy and across-track tearing.
- Optional **independently surveyed check targets** (e.g. permanent
  ground markers with known coordinates) to provide an external
  reference independent of the flight's own GCPs.

### Acceptance criteria

> _TODO: Define quantitative pass / fail thresholds for the spatial
> validation flight (e.g. RMSE in horizontal position, vertical
> offset between elevated and ground GCPs vs measured table height,
> across-track tearing between adjacent flight lines)._

### Ground Equipment Required

- [ ] UAV, controller, and batteries
- [ ] GOBI or CALViS payload
- [ ] 1 × GRYFN 4-panel ELM set (for radiometric reference, even
      though spectral accuracy is not the primary target)
- [ ] 1 × GRYFN 2-panel validation set (for the paired elevated /
      ground GCP arrangement)
- [ ] **Extended GCP set** — at least 5 (the standard layout) plus
      additional GCPs for corners and off-axis positions; more is
      better
- [ ] 2 × Folding tables (1 per panel set)
- [ ] Spirit level (to level the tables)
- [ ] Tape measure
- [ ] Optional independently surveyed check targets

> [!IMPORTANT]
> All other equipment listed in the relevant sensor fieldbook is also
> required.

---

## APEx experimental flight

### Overview

APEx experimental flights are **parameter-sweep flights** used by the
APPN APEx program to test and refine flight settings, sensor
configuration, and processing options. Unlike the spectral and
spatial validation flights — which are flown under fixed parameters
to detect change — APEx flights deliberately vary one or more
parameters at a time and compare the resulting products.

**Rationale:**

- **Parameter discovery.** Provides the empirical basis for choosing
  the operational defaults locked into the
  [Standard Flight Procedure](../StandardFlight/Standard_Flight.md).
- **Site- and platform-specific tuning.** Allows nodes to test
  variations relevant to their local conditions (illumination range,
  canopy types, terrain, airframe).
- **Documented evidence base.** Generates the data behind APPN-wide
  recommendations on flight altitude, speed, overlap, exposure,
  flight-line orientation, etc.

**When to use this flight:**

- Whenever a flight parameter is being **formally tested** under the
  APEx program.
- During **APPN Calibration Week** or equivalent campaigns where
  multiple parameter sweeps are scheduled together.
- Any time a node wants to **propose a change to the Standard Flight
  Procedure** — the change must be supported by an APEx flight
  comparing the proposed setting against the current default.

### Flight design

> [!NOTE]
> 🖼️ **Image needed (diagram):** Top-down annotated diagram of the
> APEx reference layout — the spectral validation flight footprint
> with standard panel and GCP positions clearly marked as the
> baseline against which parameter sweeps are compared.

APEx flights start from the
[Spectral validation flight](#spectral-validation-flight) layout
(panels, GCPs, site, base flight parameters) and then vary the
parameter under test. The unchanged baseline flight is **always
flown as a control alongside the experimental variant(s)**, so that
the effect of the parameter change can be isolated from day-to-day
illumination and weather variability.

For each APEx flight, record:

- The **parameter being varied** and the values tested.
- The **control / baseline parameters** used for comparison.
- The **flight order** (control vs experimental) and elapsed time
  between flights.
- All standard validation-flight metadata (see
  [Records and metadata](#records-and-metadata) above).

### APEx test catalogue _(draft)_

> Stoplight rating (used during APEx planning):
>
> - **Green** — go for Calibration Week
> - **Blue** — yes at Calibration Week if achievable, but follow up
>   with tests later in the season
> - **Red** — abandon for now

#### Calibration Week

1. **Flight height** (determined by GSD required)
   1. 20 m to 120 m
   2. Mixed pixels
2. **Flight speed, frame period, front oversampling, and gain settings**
3. **Exposure setting protocol**
   1. Set the exposure with a fixed angle / bracket?
   2. Setting at exposure with lower reflectance panel (50–60%)?
   3. Three-point ELM vs four-point ELM
4. **Side overlap settings** (tearing)
5. **Time of day (solar angles)**
   1. Angles between 10° (Adelaide 8 am winter solstice) and 85°
      (Gatton solar noon summer solstice)
   2. Ideally every 5° or 10°
   3. Covers time of day and seasonality

#### Post Calibration Week

1. **UWA-DPIRD?** Crosstrack illumination — April
   1. Panels set up in the middle and edge of the flight lines
   2. Very high flights seem to be more pronounced
2. **UQ-CSU?** Flight orientation (should be done in fully closed
   crop canopy)
   1. Default is N–S
   2. E–W
   3. NE–SW
   4. NW–SE


> Test different **wind speed and climate conditions** (may not be a
> discrete experiment if a high-frequency weather station is set up
> at every location and the data are mined post-season):
>
> 1. Minimum flight speed may change in different conditions.
> 2. There may be a maximum permissible wind speed for these sensors
>    and UAV platforms.
> 3. Movement of plants and mixing of pixels.
> 4. Whether flights are acceptable under uniform cloud cover.

### Acceptance criteria

APEx flights do not have pass / fail criteria in the same sense as
the spectral and spatial validation flights — their purpose is
**measurement, not certification**. Each APEx experiment must
nevertheless define, in advance:

- The **metric(s)** that will be used to compare the experimental
  variants against the control.
- The **threshold(s)** at which the experimental setting would be
  recommended over the current default.
- How the result will be **reported back** to the Field EWG and, if
  adopted, propagated into the Standard Flight Procedure.

### Ground Equipment Required

- [ ] All equipment listed for the
      [Spectral validation flight](#ground-equipment-required) above
- [ ] **Any additional equipment specific to the experiment**
      (e.g. extra panel sets for cross-track illumination tests,
      independent weather station, additional GCPs for orientation
      sweeps, spectroradiometer for ELM comparisons).

> [!IMPORTANT]
> All other equipment listed in the relevant sensor fieldbook is also
> required.

---
