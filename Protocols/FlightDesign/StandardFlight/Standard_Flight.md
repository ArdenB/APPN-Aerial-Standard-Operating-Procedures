# Standard Flight Procedure

> [!IMPORTANT]
> This protocol outlines the standard operational flight procedure for
> routine APPN aerial surveys using the GOBI or CALViS payloads. It
> covers the three most common setup scenarios, which can be adapted
> to suit most field situations. The equipment list under each scenario
> covers field equipment only.
>
> For sensor-specific equipment, procedures, and safety information,
> see the relevant sensor fieldbook:
>
> - [CALViS Fieldbook](../../Sensors/CALVIS/CALViS_FieldBook.md)
> - [GOBI M350 Fieldbook](../../Sensors/GOBI/GOBI_M350_FieldBook.md)
> - [GOBI IF1200 Fieldbook](../../Sensors/GOBI/GOBI_IF1200_FieldBook.md)
>
> For periodic calibration / APEx test flights, see the
> [Validation Flight Procedure](../ValidationFlight/Validation_Flight.md).

---

> [!NOTE]
> **Outstanding items deferred to a future revision.**
> The procedure content below is complete for revision 1.0. The only
> remaining items are tracked in the
> [future-release backlog](../../../TODO_FUTURE.md):
>
> - A suggested hero/cover photo of a correctly-staged standard flight
>   site (see [`/IMAGE_TODO.md`](../../../IMAGE_TODO.md)).
> - Pre-season decisions on flight-line orientation and ELM-panel
>   requirements under variable illumination, pending APEx / Field EWG
>   sign-off.

---

## Document Structure

This protocol is organised into two parts:

1. **[Background and common elements of all standard flights](#background-and-common-elements-of-all-standard-flights)** —
   shared setup rules that apply to every standard flight design:
   - [Flight-line Orientation](#flight-line-orientation)
   - [Panel Setup](#panel-setup)
     - [Validation Panel Setup](#validation-panel-setup)
   - [Ground Control Points](#ground-control-points)
2. **The three standard flight designs**, each with its own overview,
   when-to-use criteria, flight-design notes, and equipment list:
   - [Dual ELM panel flight](#dual-elm-panel-flight) — default
     pattern for nodes with 2 ELM panel sets; required for longer
     flights and variable illumination.
   - [Single ELM panel flight](#single-elm-panel-flight) — for
     nodes with a single ELM panel set or short missions in stable
     conditions.
   - [Multi-Flight Capture](#multi-flight-capture) — for survey
     areas too large to capture in a single mission, split into
     overlapping sub-flights with shared ELM panels and tie GCPs.

---

## Background and common elements of all standard flights

> [!IMPORTANT]
> This section describes the **placement of GCPs and reflectance panels**
> that is common to all standard flight patterns described below.
>
> All placements given here (distances, positions, panel locations,
> GCP distributions) are **approximate guidelines, not strict
> requirements**. Operators should use common sense and adapt the
> layout to the realities of the site:
>
> - Use the **nearest existing path, bare strips, tramlines etc** in the
>   crop to access and place the panels and GCP's.
> - **Do not place panels or GCPs inside experimental plots** or
>   anywhere they would damage the crop, disturb a treatment, or
>   obstruct other field operations.
> - Keep panels and GCPs clear of shadows (from trees, infrastructure,
>   the operator, or the UAV itself) and away from the take-off /
>   landing zone.
> - Where the ideal position is not accessible, move to the closest
>   practical location that still satisfies the intent of the layout
>   (e.g. good distribution across the survey area, panels overflown
>   at correct time).

> [!CAUTION]
> **Keep panels and GCPs away from the edge of the capture window.**
>
> Depending on the exact flight parameters (altitude, overlap, turn 
> geometry), GOBI and CALViS can fail to capture data the
> outermost portion of the planned capture polygon — meaning targets
> placed near the edge may be missed entirely or only partially
> captured.
>
> - **Place all GCPs and reflectance panels inside an "effective
>   capture area" approximately 10% smaller than the planned capture
>   polygon** (i.e. set back from each edge by ~10% of the polygon's
>   short-axis dimension).
> - If site access forces a panel or GCP to sit near the edge of the
>   field, **expand the planned capture polygon outward** so that the
>   target still falls comfortably inside the effective capture area.
> - Do not rely on the nominal polygon boundary as the usable imaging
>   extent.
>
> Failure to place ELM panels correctly can render a flight's data
> completely unusable for radiometric analysis.

### Flight-line Orientation

> [!NOTE]
> GRYFN recommends aligning flight lines with the planting direction for
> "operational reasons", as this greatly reduces stitching artefacts
> between adjacent flight lines. Testing flight-line angle is a top
> priority for APEx, and this guidance may be revised before the start of
> the season (tracked in the
> [future-release backlog](../../../TODO_FUTURE.md)).

### Panel Setup

All reflectance panels must be deployed on **open, unshaded, level
ground**, clear of the take-off / landing zone and clear of any
obstructions that could cast shadows across the panels at any point
during the flight window.

![GRYFN 4-panel ELM reflectance set arranged in order of brightness on a levelled folding table in an open, unshaded paddock](Standard_Flight_media/panel_setup_table.jpg)

*Figure: A GRYFN 4-panel ELM reflectance set deployed on a folding table in
an open, unshaded area. Panels are laid out in order of brightness along the
intended flight direction, elevated above the soil surface, and positioned
clear of vegetation, infrastructure, and the take-off / landing zone.*

**Place panels on a folding table.** All radiometric panels deployed in
the field should be placed on a folding table. A standard fixed-height
blow-mould trestle table (e.g. the
[Lifetime 6ft Standard Blow Mould Trestle Table](https://www.bunnings.com.au/lifetime-6ft-standard-blow-mould-trestle-table_p3192212)
from Bunnings) is suitable for most deployments; where a height-adjustable
table is preferred (e.g. to better match canopy height or work around uneven
ground), the
[Versalite 180 Multi-Height Table](https://questoutdoors.com.au/collections/multi-height-table/products/versalite-180-multi-height-table)
from Quest Outdoors is a more expensive alternative. Mounting the panels on
a table is important because:

- **Levelling.** Panels must be level for accurate reflectance
  retrieval, and it is far easier to level a table than to find a
  level patch of ploughed or uneven ground.
- **Reduced spectral contamination.** Elevating the panels above the
  canopy reduces stray reflected light from the surrounding crop
  contaminating the panel signal.
- **Reduced dust and debris.** Raising the panels off the ground
  reduces their susceptibility to dust, soil splash, and trampling
  damage.

Level the table using the spirit level, and **record the height of
the panel surface above the ground** in the flight log.

**Panel ordering and orientation.** Lay out each panel set in **order
of brightness** (e.g. darkest → brightest), with the row of panels
**oriented along the planned flight direction**.

> [!IMPORTANT]
> Hyperspectral line scanners image perpendicular to the flight
> direction. If panels are laid out perpendicular to flight (i.e.
> across the scan line), multiple panels can fall within a single
> scanline and introduce significant errors during the ELM
> calibration. Always align the panel row **with** the flight
> direction so each panel occupies its own set of scanlines.

#### Validation Panel Setup

In all the flight designs described below, the **2-panel validation
panel set** is deployed near the **middle of the survey area**, on its
own levelled folding table, following the same general setup rules as
the main ELM panels above.

In addition, **two GCPs are paired with the validation panels** to
support data QC:

1. **Elevated GCP** — placed on the validation panel table, alongside
   the validation panels.
2. **Ground GCP** — placed directly on the ground in the **adjacent
   flight line**, positioned **perpendicular to the elevated GCP** (i.e.
   on a line running across-track from the table).

![Field photograph of the validation panel table: 2-panel validation reflectance set on a levelled folding table with the elevated GCP mounted alongside, and the paired ground GCP placed in the adjacent flight line perpendicular to the elevated GCP](Standard_Flight_media/validation_panel_table.jpg)

*Figure: Validation panel deployment. The 2-panel validation reflectance
set is mounted on a levelled folding table with an elevated GCP placed
alongside the panels. The paired ground GCP sits in the adjacent flight
line, perpendicular (across-track) to the elevated GCP, so the two GCPs
can be used during QC to check for flight-line tearing and vertical
accuracy.*

This paired GCP arrangement is used during data QC to check for:

- **Flight-line tearing / mis-registration** between adjacent lines
  (the two GCPs should resolve to the same horizontal position
  across-track).
- **Vertical (height) accuracy**, by comparing the measured elevation
  difference between the elevated and ground GCPs against the recorded
  table height.

> [!CAUTION]
> This procedure was designed with **Propeller Aeropoints** in mind. If
> using a different GCP system, consider whether it is safe and
> practical to take a location measurement on top of a table. If not,
> place the "elevated" GCP on the ground a few metres clear of the
> table instead, and record the offset.


### Ground Control Points

All of the standard flight designs specify a **minimum of 5 GCPs**.
This number is based on the standard pack of 5 Propeller Aeropoints.

There are several distinct types of spatial error in UAV imagery, and
the placement of these five GCPs is chosen so that **at least one GCP
checks each of the main error types**:

- **2 × centre GCPs (the validation pair, described above)** — check
  for **flight-line tearing** (across-track mis-registration) and
  **vertical / elevation accuracy**.
- **2 × corner GCPs** — placed near **opposite corners** of the survey
  area, **directly under a flight line**, to check for **temporal GNSS
  drift** across the duration of the flight.
- **1 × off-axis GCP** — placed **between two flight lines** (i.e. not
  directly under the nadir track) to check for **off-axis / lateral
  registration errors**.

> [!NOTE]
> The 5-GCP layout is a **minimum**. Additional GCPs are encouraged for
> all flights and are **strongly recommended** for larger survey areas
> and for the multi-flight capture configuration (see below).


---

## Dual ELM panel flight

### Overview

This flight uses **two sets of ELM (Empirical Line Method) reflectance
panels**, deployed at approximately the **1/3 and 2/3 positions along
the long axis of the survey area**. 

**Rationale:**

- **Reduced temporal offset between target and panel capture.** Splitting
  the panels across the field minimises the elapsed time (and therefore
  the change in solar geometry and atmospheric conditions) between any
  given image and its nearest panel overflight.
- **Redundancy.** Both panel sets can be ingested by the GRYFN Processing
  Tool (GPT) during radiometric calibration, providing a backup if
  one panel set is shaded, disturbed, or otherwise unusable. See the
  [Processing Pipelines](../../Pipelines/GryfnProcessingPipeline/Gryfn_Processing_Pipeline.md#reflectance-target-values)
  page for how panel reflectance targets are ingested during the ELM
  calibration.
- **Improved reflectance retrieval** over longer flights where
  illumination conditions are more likely to drift.

**When to use this flight:**

- **Default** flight pattern for all nodes equipped with two ELM panel
  sets.
- **Recommended** for all flights longer than **10 minutes**.
- **Mandatory** for flights longer than **15 minutes**.

- **Mandatory** under variable illumination conditions (e.g. broken
  cloud), regardless of flight duration. (APEx results dependent)

### Flight design

![Top-down diagram of a dual ELM panel flight: survey polygon with two 4-panel reflectance sets placed at the 1/3 and 2/3 positions along the long axis, validation panel set near the centre, flight lines aligned with the long axis, ~10% edge-of-polygon buffer, and a 5-GCP layout (two centre validation GCPs, two corner GCPs, one off-axis GCP)](Standard_Flight_media/dual_elm_panel_flight_diagram.png)

*Figure: Dual ELM panel flight layout. Two reflectance panel sets are
deployed at approximately the 1/3 and 2/3 positions along the long axis
of the survey area, with the validation panel set and its paired GCPs
near the centre. The 5-GCP layout covers centre, corner, and off-axis
positions, and all panels and GCPs sit inside the ~10% effective
capture area inset from the polygon edge.*


### Ground Equipment Required

- [ ] 2 × GRYFN 4-panel reflectance set (11%, 30%, 56%, 82%)
- [ ] 1 × GRYFN 2-panel validation reflectance set
- [ ] 5 × Ground control points (GCPs) — Propeller Aeropoints or
      equivalent (more for larger areas)
- [ ] 2 × Folding tables (1 per panel set)
- [ ] Spirit level (to level the tables)
- [ ] Tape measure

> [!IMPORTANT]
> All other equipment listed in the relevant sensor fieldbook is also
> required.

---

## Single ELM panel flight

### Overview

This flight uses a **single set of ELM (Empirical Line Method) reflectance
panels**, deployed near the **centre of the survey area** and are only flown 
over once.

**Rationale:**

- **Simpler logistics.** Only one main panel set needs to be deployed,
  levelled, and monitored — appropriate for nodes equipped with a
  single ELM panel set or for short missions where setup time is at a
  premium.
- **Adequate radiometric calibration for short flights.** Over short
  durations, illumination conditions are unlikely to drift far enough
  to require a second panel observation, and the validation panels
  provide a basic check on the calibration.

**When to use this flight:**

- **Default** flight pattern for nodes equipped with **only one ELM
  panel set**.
- **Acceptable** for short missions of **≤ 10 minutes** under stable
  illumination conditions (clear sky or uniform overcast).
- **Not recommended** for flights longer than 10 minutes — use the
  [Dual ELM panel flight](#dual-elm-panel-flight) instead.
- **Not permitted** under variable illumination (e.g. broken cloud),
  regardless of flight duration. (Pending APEx confirmation — see the
  [future-release backlog](../../../TODO_FUTURE.md).)

### Flight design

![Top-down diagram of a single ELM panel flight: survey polygon with one 4-panel reflectance set placed near the centre, validation panel set adjacent in the middle of the survey area, flight lines aligned with the long axis, ~10% edge-of-polygon buffer, and a 5-GCP layout (two centre validation GCPs, two corner GCPs, one off-axis GCP)](Standard_Flight_media/single_elm_panel_flight_diagram.png)

*Figure: Single ELM panel flight layout. One 4-panel reflectance set is
deployed near the centre of the survey area, alongside the validation
panel set and its paired GCPs. The 5-GCP layout covers centre, corner,
and off-axis positions, and all panels and GCPs sit inside the ~10%
effective capture area inset from the polygon edge.*

### Ground Equipment Required

- [ ] 1 × GRYFN 4-panel reflectance set (11%, 30%, 56%, 82%)
- [ ] 1 × GRYFN 2-panel validation reflectance set
- [ ] 5 × Ground control points (GCPs) — Propeller Aeropoints or
      equivalent (more for larger areas)
- [ ] 2 × Folding tables (1 per panel set)
- [ ] Spirit level (to level the tables)
- [ ] Tape measure

> [!IMPORTANT]
> All other equipment listed in the relevant sensor fieldbook is also
> required.

---

## Multi-Flight Capture

> [!IMPORTANT]
> While the GRYFN Processing Tool (GPT) is capable of merging multiple
> sub-flights during processing, this workflow has frequently produced
> issues with the ELM calibration. The **current recommendation is to
> process each sub-flight individually** and only merge the resulting
> products downstream. GRYFN is aware of the issue, and this guidance
> may be revised in a future update to GPT.

### Overview

This configuration covers survey areas that are **too large to be
captured in a single mission** (due to battery endurance, radio range,
or regulatory line-of-sight constraints) and must be split into
**two or more sub-flights**. Sub-flights are deliberately planned to
**overlap** along their shared boundary, and a **shared ELM panel
set plus a pair of "tie" GCPs are placed inside the overlap region**
and **left in place between sub-flights**. This shared equipment is
overflown by both sub-flights and is the primary mechanism for
stitching the sub-flights into a single, radiometrically and
geometrically consistent product.

**Rationale:**

- **Shared radiometric reference across sub-flights.** Because the
  same ELM panel set is observed by both sub-flights (without being
  moved or re-levelled), it provides a common radiometric anchor,
  letting the sub-flights be calibrated onto a consistent reflectance
  scale even when illumination changes between flights.
- **Geometric tie between sub-flights.** The two shared "tie" GCPs in
  the overlap zone are observed by both sub-flights and pin the
  sub-flights together horizontally and vertically, preventing seams
  and offsets at the sub-flight boundary.
- **Equipment stays put.** Leaving the shared panels and tie GCPs in
  place between sub-flights eliminates re-deployment error (panels
  re-levelled differently, GCPs moved by a few cm) that would
  otherwise corrupt the tie.\
  _Battery / payload swaps and any required pilot relocations happen
  while the shared equipment remains undisturbed._\
  _(Operators should remain on-site to monitor the shared equipment
  between sub-flights.)_\

**When to use this flight:**

- **Mandatory** when the planned survey area cannot be completed in a
  single mission within UAV endurance and regulatory line-of-sight
  limits.
- **Recommended** when a single-mission survey would exceed
  **15 minutes** on the wing and the area can be sensibly divided
  into shorter sub-flights.
- Each individual sub-flight should otherwise follow the
  [Dual ELM panel flight](#dual-elm-panel-flight) layout, with its own
  panels at ~1/3 and 2/3 along its long axis (one of which will be
  the shared overlap panel set).



### Flight design

![Top-down diagram of a multi-flight capture: two sub-flight polygons with a deliberate overlap zone along their shared boundary, a shared 4-panel ELM reflectance set and two tie GCPs placed inside the overlap zone (highlighted) and overflown by both sub-flights, dual-panel placement within each sub-flight (with the shared set serving as one panel position for each), validation panel placement within one sub-flight, and expanded GCP distribution across the full survey area](Standard_Flight_media/multi_flight_capture_diagram.png)

*Figure: Multi-Flight Capture layout. The survey area is split into two
sub-flights with a deliberate overlap zone at their shared boundary. A
shared ELM panel set and two tie GCPs sit inside the overlap (and are
left in place between sub-flights), giving both sub-flights a common
radiometric and geometric anchor. Each sub-flight otherwise follows the
dual-panel layout, with the validation panel set in one sub-flight and
an expanded GCP distribution across the full area.*

### Ground Equipment Required

- [ ] 2 × GRYFN 4-panel reflectance set (11%, 30%, 56%, 82%)
      — 1 dedicated to the individual sub-flights + **1 shared set
      placed in the overlap zone and left in place between
      sub-flights**
- [ ] 1 × GRYFN 2-panel validation reflectance set
- [ ] 10 × Ground control points (GCPs) — Propeller Aeropoints or
      equivalent (minimum; more strongly recommended for large areas).
      Includes **2 × "tie" GCPs placed inside the overlap zone and
      left in place between sub-flights**
- [ ] 4 × Folding tables (1 per panel set)
- [ ] Spirit level (to level the tables)
- [ ] Tape measure

> [!IMPORTANT]
> All other equipment listed in the relevant sensor fieldbook is also
> required.

> [!CAUTION]
> The shared overlap-zone panel set and tie GCPs **must not be moved,
> re-levelled, or otherwise disturbed between sub-flights**. If they
> are bumped, shaded, or relocated, the radiometric and geometric
> tie between sub-flights is lost and the sub-flights cannot be
> reliably stitched. If the shared equipment is disturbed, treat
> the affected sub-flights as independent captures and re-fly if
> possible.

> [!NOTE]
> **Two-sub-flight limit for nodes with only 2 ELM panel sets.**
>
> The configuration described above assumes a node has **2 ELM panel
> sets** in total: one is dedicated to the first sub-flight and the
> other is the shared set in the overlap zone (which then also serves
> as one of the panel positions for the second sub-flight). This
> covers a survey split into **exactly 2 sub-flights**.
>
> Splitting a survey into **3 or more sub-flights** is not possible
> with only 2 panel sets, because every internal (middle) sub-flight
> has **two overlap zones** (one with each neighbour) and therefore
> requires its own pair of shared panel sets. 
>
> If a node with only 2 panel sets must cover an area larger than two
> sub-flights can fit, **divide the area into independent zones, each
> sized to fit within a 2-sub-flight capture**, and treat each zone as
> a separate site. Do **not** attempt a 3+ sub-flight
> capture by re-using or re-deploying a panel set during sub-flights —
> moving the shared equipment breaks the radiometric and geometric
> tie that the multi-flight design depends on.

---
 