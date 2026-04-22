# Validation Test Flight Procedure

**Version 1.0 – April 2026**

> The goal of this protocol is to outline a standard test flight and a
> modified test flight for all APPN drone payloads. The standard test flight
> is to be flown under the exact same parameters to check the variation in
> spectral and geometric accuracy between flights. The standard test flight
> should be flown:
>
> - At regular intervals **(exact interval TBD)** by all nodes to check that
>   sensors are still comparable.
> - Any time a sensor is returned to service after repairs and maintenance.
>
> The modified test flight is to be used to test different parameters as
> part of the APPN APEx program. It is based on the standard test flight
> but with modifications to test a range of parameters.

---

## Equipment Required

- [ ] UAV, controller and batteries
- [ ] GOBI or CALViS
- [ ] 2 × GRYFN 4-panel set (11%, 30%, 56%, 82%)
  - If two sets are not available, then 1 can be used.
- [ ] 1 × GRYFN 2-panel validation set (20%, 45%)
- [ ] 5 × Propeller Aeropoints or other ground control points (GCPs)
- [ ] 1 × folding table
- [ ] 1 × tape measure
- [ ] Weather station
  - Details TBD.
- [ ] Downwelling radiation sensor
  - Details TBD.
- [ ] Optional spectroradiometer (SVC, FieldSpec)
- [ ] Spirit bubble
- [ ] All other equipment listed in the GOBI or CALViS standard operating
      procedures

> The modified test flight may require additional equipment to test
> specific information. See the detailed experiment list for more
> information.

---

## Standard Validation Flight – GOBI & CALViS

The standard validation flight consists of 5 flightlines over an area of
approximately 7,200 m² (60 m × 120 m). It can be flown over any safe and
convenient location, though it would ideally be flown over crops or grass
if available. The figure below shows how equipment should be placed in the
field.

- The default orientation should be North–South (as per the figure below)
  and flown as close as possible to solar noon.
- One GCP should be placed in each flightline in a diagonal pattern at
  10%, 30%, 50%, 70% and 90% of the flightline (see figure). These will be
  positioned by taking a stroll along the flight lines with the UAV
  controller showing its live location.
- The first GRYFN 4× reflectance panel set should be placed in flightline 1
  ~30% of the way along the line (see figure).
  - This panel set will be used for ELM generation in the GRYFN Processing
    Tool.
  - This panel should be placed on the fold-out table levelled using the
    spirit bubble, and the approximate heights should be measured and
    recorded. This will be used to validate LiDAR and spectral
    characteristics.
  - Ensure that panels are set up in the following order:
    11%, 30%, 56%, 82% reflectance.

![Standard validation flight panel layout](APPN_Validation_Flight_Rev1.0_media/image_d43bd2392053.jpg)

- The second panel should be placed at the centre of flightline 4, about
  30% from the start.
  - This is so one panel set is being captured in an alternative flight
    direction.
  - If a spectroradiometer is available, it should be set up above the
    panels on a continuous capture in the nadir configuration.
- The independent validation panel should be placed at the centre of
  flightline 3, 50% of the way along.

**Legend**

| Symbol | Meaning |
| ------ | ------- |
| ![Ground control points](APPN_Validation_Flight_Rev1.0_media/image_0343859d6c18.svg) | Ground control points |
| ![GRYFN reflection panel set](APPN_Validation_Flight_Rev1.0_media/image_70fce4aa1513.svg) | GRYFN reflection panel set |
| ![Independent validation panel](APPN_Validation_Flight_Rev1.0_media/image_df0114ae9e97.png) | Independent validation panel |

---

## IF1200 + CALViS or GOBI

1. Using QGroundControl, set up a new flight mission in a safe and
   convenient location. This can be over a field that needs surveying and
   is therefore useful for two purposes.
2. Create a rectangular survey area of approximately 6,200 m².
   1. Export the polygon and import it into the *HPI Polygon Tool*.
3. Use the parameters outlined below for flight planning in QGroundControl:

   | Parameter            | Setting                                |
   | -------------------- | -------------------------------------- |
   | Altitude             | 50 m                                   |
   | Flight speed         | 3.2 m/s                                |
   | Trigger Distance     | Leave as default (number is irrelevant)|
   | Spacing              | 12 m                                   |
   | Angle                | 180°                                   |
   | Turnaround Distance  | 10 m                                   |

4. Load this mission onto the IF1200.
5. **INSERT EXPOSURE SETTING PROCEDURE.**

---

## DJI M350 RTK + GOBI

1. Using DJI Pilot 2, set up a new flight mission in a safe and convenient
   location. This can be over a field that needs surveying and is therefore
   useful for two purposes.
2. Create a rectangular survey area of approximately 6,200 m².
3. Create a smaller rectangular survey which sits inside this larger
   *survey* area. This shapefile will be input to the GOBI to set the
   capture location.
   1. This polygon needs to be smaller by 2× the flight speed (~7 m) in the
      direction of the flight. The figure below outlines this — the red
      polygon is the *capture* polygon, the yellow is the *survey*
      polygon.

   ![Capture vs survey polygon](APPN_Validation_Flight_Rev1.0_media/image_154a62ad07f2.png)

   2. Export the polygon and import it into the
      [HPI Polygon Tool](http://apps.headwallphotonics.com/).

4. Use the parameters outlined below for flight planning in DJI Pilot 2:

   | Parameter             | Setting |
   | --------------------- | ------- |
   | Altitude              | 50 m    |
   | Flight speed          | 3.2 m/s |
   | Side Overlap          | 49%     |
   | Frontal Overlap Ratio | 80%     |
   | Course Angle          | 180°    |
   | Margin                | 0       |
   | Elevation Optimisation| FALSE   |

5. **EXPOSURE SETTING PROCEDURE.**

---

## Potential Experiments

> As part of APEx, we would like to fly these experimental flights during
> Calibration Week or across the 2026 calibration trials (where possible,
> given we need to fly these anyway).

**Stoplight rating**

- 🟢 **Green** – go for Cali Week
- 🔵 **Blue** – yes at Cali Week if achievable, but follow up with tests
  later in season
- 🔴 **Red** – abandon for now

### Cali Week

1. Flight height (determined by GSD required)
   1. 20 m to 120 m
   2. Mixed pixels?
2. Flight speed, frame period, front oversampling, and gain settings
3. Exposure setting protocol
   1. Set the exposure with a fixed angle/bracket?
   2. Setting at exposure with lower reflectance panel (50–60%)?
   3. Three-point ELM vs four-point ELM
4. Side overlap settings (tearing?)
5. Time of day (solar angles)
   1. Angles between 10° (Adelaide 8 am winter solstice) and 85° (Gatton
      solar noon summer solstice)
   2. Ideally every 5° or 10°
   3. This covers time of day and seasonality

### Post Cali Week

1. **UWA-DPIRD?** Crosstrack illumination — April
   1. Panels set up in the middle and edge of the flight lines
   2. Very high flights seem to be more pronounced
2. **UQ-CSU?** Flight orientation (should be done in fully closed crop
   canopy)
   1. Default is N–S
   2. E–W
   3. NE–SW
   4. NW–SE

### Extras and Post-Processing Experiments

1. UAV platform?
   1. Vibrations
2. RTK?
3. Auscors base station vs Emlid RINEX? Particularly for remote sites.
4. DSM resolution?
5. Spectral binning in different ways
6. Spit out SBG error reports in GPRO

> Test different **wind speed and climate conditions** (may not be an
> experiment if we set up a high-frequency weather station at every
> location and then data-mine post-season):
>
> 1. Minimum flight speed may change in different conditions.
> 2. There may be a maximum permissible wind speed for these sensors and
>    UAV platform.
> 3. What about movement of plants and mixing of pixels?
> 4. Can we fly with uniform cloud cover?
**Validation Test Flight Procedure**

**Version 1.0 – April 2026**

*The goal of this protocol is to outline a standard test flight and a modified test flight for all APPN drone payloads. The standards test flight is to be flown under the exact same parameters to check the variation in spectral and geo accuracy between. The standard test flight should be flown:*

- *At regular intervals ** (exact interval tbd) ** by all node to check sensors are still comparable*
- *Anytime a sensor is returned to service after repairs and maintenance *

*The modified test flight is to be used to test different parameters as part of the APPN APEx program. It’s based on the standard test flight but with modification to test a range of parameters. *

**Equipment required **

- UAV, controller and batteries
- GOBI or CALViS
- 2x GRYFN 4 panel set (11%, 30%, 56%, 82%)
	- If two sets are not available, then 1 can be used
- 1x GRYFN 2 panel validation set (20%, 45%)
- 5x Propellor Aeropoints or other ground control points (GCP)
- 1x Folding table
- 1x tape measure
- Weather station
	- Details tbd
- Downwelling radiation sensor.
	- Details tbd
- Optional spectroradiometer (SVC, FieldSpec)
- Spirit bubble
- All other equipment listed in the GOBI or CALViS standard operating procedures

*The modified test flight may require additional equipment to test specific information. See detailed experiment list for more information*.

**Standard Validation Flight – GOBI & CALViS**

The standard validation flight consists of 5 flightlines over an area of approximately 7200m2 (60m x 120m). It can be flown over any safe and convenient location though it would ideally by flown over crops or grass if available. Figure one shows how equipment should be placed in the field.

- The default orientation should be North-South (as per the figure below) and flown as close as possible to solar noon.
- One GCP should be place in each flightline in a diagonal pattern at 10%, 30% 50%, 70% and 90% of the flightline (see below figure). These will be positioned by taking a little stroll along the flight lines with the UAV controller showing its live location.
- The first GRYFN 4x reflectance panel set should be placed in flightline 1 ~ 30% of the way along the line (see below figure).
	- This panel set will be used for ELM generation in the GRYFN Processing Tool.
	- This panel should be placed on the fold out table levelled using the spirit bubble, and the approximate heights should be measured and recorded. This will be used to validate LIDAR and spectral characteristics.
	- Ensure that panels are set up in the following order - 11%, 30%, 56%, 82% reflectance.

![](APPN_Validation_Flight_Rev1.0_media/image_d43bd2392053.jpg)

- The second panel should be placed at the centre of flightline 4 about 30% from the start
	- This is so one panel set is being captured in an alternative flight direction.
	- If a spectroradiometer is available this should be set up above the panels on a continuous capture in the nadir configuration.
- The independent validation panel should be placed at the centre of flightline 3, 50% of the way along.

Ground control points

![](APPN_Validation_Flight_Rev1.0_media/image_0343859d6c18.emf)

GRYFN Reflection Panel set

![](APPN_Validation_Flight_Rev1.0_media/image_70fce4aa1513.emf)

Independent Validation Panel

![](APPN_Validation_Flight_Rev1.0_media/image_df0114ae9e97.png)**IF1200 + CALVIS or GOBI**

1. Using ‘QGroundControl’ set up a new flight mission in a safe and convenient location.  This can be over a field which needs surveying and therefore useful for two purposes.
2. Create a rectangular survey area of approximately 6200 m2.
	1. Export the polygon and import it into ‘HPI Polygon Tool’.
3. Use the parameters outlined below for flight planning in QGroundControl.

**Parameter**

**Setting**

Altitude

50 m

Flight speed

3.2 m/s

Trigger Distance

Leave as default (number is irrelevant)

Spacing

12 m

Angle

180 degrees

Turnaround Distance

10 m

1. Load this mission onto the IF1200.
2. **INSERT EXPOSURE SETTING PROCEDURE**

**DJI M350 RTK + GOBI**

1. Using ‘DJI Pilot 2’ set up a new flight mission in a safe and convenient location.  This can be over a field which needs surveying and therefore useful for two purposes.
2. Create a rectangular survey area of approximately 6200 m2.
3. Create a smaller rectangular survey which sits inside this larger ‘survey’ area.  This shapefile will be input to the GOBI to set capture location.
	1. This polygon needs to be smaller by 2x the flight speed (~7 m) in the direction of the flight. The below figure outlines this where the red polygon is the ‘capture’ polygon the yellow the ‘survey’.

![](APPN_Validation_Flight_Rev1.0_media/image_154a62ad07f2.png)

-
	1. Export the polygon and import it into ‘[HPI Polygon Tool](http://apps.headwallphotonics.com/)’

1. Use the Parameters outlined below for flight planning in ‘DJI Pilot 2’.

**Parameter**

**Setting**

Altitude

50 m

Flight speed

3.2 m/s

Side Overlap

49%

Frontal Overlap Ratio

80%

Course Angle

180 degrees

Margin

0

Elevation Optimisation

FALSE

1. **EXPOSURE SETTING PROCEDURE **

**Potential Experiments**

*As part of APEx, we would like to fly these experimental flights during Calibration Week or across the 2026 Calibration trials (where possible given we need to fly these anyway).*

*Stoplight Rating:*

- *Green – Go for Cali Week*
- *Blue– yes at Cali week if achievable, but follow up with tests later in season*
- *Red – abandon for now*

***Cali Week***

1. Flight height (determined by GSD required)
	1. 20 m to 120 m
	2. Mixed pixels?
2. Flight speed, frame period, front oversampling and gain settings
3. Exposure setting protocol
	1. Set the exposure with a fixed angle/bracket?
	2. Setting at exposure w/ lower reflectance panel (50-60%)?
	3. Three point ELM vs. four point ELM
4. Side overlap settings (tearing?)
5. Time of day (Solar angles)
	1. Angles between 10 degrees (Adelaide 8am winter solstice) and 85 degrees (Gatton solar noon summer solstice)
	2. Ideally every 5 or 10 degrees
	3. This covers time of day and seasonality

***Post cali week***

1. **UWA-DPIRD?** Crosstrack illumination - April
	1. Panels setup in the middle and edge of the flight lines
	2. Very high flights seem to be more pronounced
2. **UQ-CSU?** Flight orientation (should be done in fully closed crop canopy)
	1. Default is N-S
	2. E-W
	3. NE-SW
	4. NW-SE

***Extras and post processing experiments***

1. UAV platform?
	1. Vibrations
2. RTK?
3. Auscors base station vs EMLID RINEX? Particularly for remote sites.
4. DSM resolution?
5. Spectral binning in different ways
6. Spit out SBG error reports in GPRO

- Test different **wind speed and climate conditions** (may not be an experiment if we set up high frequency weather station at every location then data mine post season)
	-
		1. Minimum flight speed may change in different conditions
		2. May be a max permissible wind speed for these sensors and UAV platform
		3. What about movement of plants and mixing of pixels?
		4. Can we fly with uniform cloud cover?
