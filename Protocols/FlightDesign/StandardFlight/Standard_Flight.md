# Standard Flight Procedure

**Version 0.1 – DRAFT, April 2026**

> The goal of this protocol is to outline the standard operational flight
> procedure for routine APPN aerial surveys using the GOBI or CALViS
> payloads. It covers the steps common to every survey flight — pre-flight
> planning, on-site setup, in-flight conduct, and immediate post-flight
> actions — so that data captured at any node is comparable and traceable.
>
> For sensor-specific setup and shutdown steps, see the
> [CALViS Fieldbook](../../Sensors/CALVIS/CALViS_FieldBook.md) and the
> [GOBI Fieldbook](../../Sensors/GOBI/GOBI_FieldBook.md).
>
> For periodic calibration / APEx test flights, see the
> [Validation Flight Procedure](../ValidationFlight/Validation_Flight.md).

---

## Equipment Checklist

- [ ] UAV, controller and sufficient charged batteries for the planned mission
- [ ] GOBI or CALViS payload (per sensor fieldbook)
- [ ] 1 × GRYFN 4-panel reflectance set (11%, 30%, 56%, 82%)
- [ ] Ground control points (GCPs) — Propeller Aeropoints or equivalent
- [ ] Folding table and spirit bubble (for panel set-up)
- [ ] Tape measure
- [ ] Weather station / handheld anemometer
- [ ] Field tablet or laptop with mission planning software
  (QGroundControl or DJI Pilot 2)
- [ ] Site map / plot boundary shapefile
- [ ] Paper or digital flight log
- [ ] All other equipment listed in the relevant sensor fieldbook

---

## Pre-Flight Planning

1. **Confirm the survey area** and obtain (or generate) a polygon
   shapefile of the area of interest.
2. **Check airspace and permissions** — confirm the site is clear of
   restricted airspace and that all required notifications / approvals
   are in place.
3. **Check weather forecast** for the planned flight window:
   - Wind speed within UAV and sensor limits.
   - No precipitation expected.
   - Solar conditions appropriate (ideally clear sky, sun > 30° elevation;
     uniform overcast may also be acceptable — TBD).
4. **Plan the mission** in QGroundControl (IF1200) or DJI Pilot 2
   (M350 RTK) using the parameters in the matching sensor fieldbook.
5. **Brief the team** on roles: pilot, visual observer, sensor operator,
   panel/GCP technician.

---

## On-Site Setup

1. Conduct a site safety walk and identify take-off / landing zones and
   emergency landing areas.
2. Set up the UAV and payload per the sensor fieldbook power-on sequence.
3. Deploy GCPs across the survey area in a distribution appropriate for
   the plot size (minimum 4 corners + 1 centre for small plots).
4. Set up the GRYFN reflectance panel set on the levelled folding table
   in an open, unshaded location near the survey area, oriented per the
   sensor fieldbook.
5. Record site metadata in the flight log:
   - Date, time, operators present.
   - Site name and coordinates.
   - Weather observations (wind, cloud cover, temperature).
   - Sensor serial numbers and firmware versions.
   - GCP IDs and approximate positions.

---

---

## Notes and Open Items

> This document is a starting scaffold. Items still to be defined:
>
> - Maximum permissible wind speed per UAV / sensor combination.
> - Standard exposure-setting procedure (cross-link once finalised in the
>   sensor fieldbooks).
> - Required GCP density as a function of plot size and GSD.
> - Minimum acceptable solar elevation for routine surveys.
