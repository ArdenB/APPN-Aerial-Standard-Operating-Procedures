# APPN – GOBI M350 Fieldbook

> This fieldbook provides a standardised operational guide for APPN GOBI UAV
> deployments on the DJI M350, supporting safe flight operations, consistent
> sensor configuration, and high-integrity data capture. It is intended for
> trained APPN staff conducting hyperspectral, LiDAR, RGB, and GNSS-INS data
> acquisitions, and promotes repeatability, transparency, and confidence in
> downstream data analysis across APPN operations.

> **This protocol must be followed for all standard APPN GOBI UAV flights.**
> Adherence to these procedures is essential to ensure operational safety,
> data integrity, and comparability of datasets across deployments. For any
> flights that **fall outside standard operating procedures**, detailed
> records must be kept documenting all deviations, including the specific
> settings changed, the rationale for those changes, and any anticipated
> implications for data quality or analysis.

---

## Equipment

> Ensure batteries for all equipment are fully charged before heading to the
> field. Ensure charging cables are available for necessary equipment.

- [ ] **Aircraft**
  - [ ] Aircraft batteries
  - [ ] Landing gear
  - [ ] Landing pad
  - [ ] Spare parts
  - [ ] Tools
  - [ ] Logbook
- [ ] **Radio Control Transmitter / Ground Control Station**
- [ ] **GRYFN Gobi**
  - [ ] Gobi system
  - [ ] Power cables, chargers
  - [ ] Ethernet cable
  - [ ] SD card
  - [ ] *Capture* polygon files
- [ ] **Ground reference kit**
  - [ ] Reflectance calibration panels (11%, 30%, 56%, 82%)
  - [ ] Calibration validation panels (20%, 45%)
  - [ ] Ground control points and RTK GNSS system
  - [ ] 2 × folding tables to elevate panels
  - [ ] *If over 50 km from CORS base station*, a portable RTK base station
        ([link to GRYFN gitbook](https://gryfn.gitbook.io/gryfn-operations/operations/base-station-availability))
- [ ] **Accessories**
  - [ ] Safety gear (signage and high-vis vests)
  - [ ] Aeronautical radio
  - [ ] Field laptop and spare batteries
  - [ ] External storage media
  - [ ] Water, food, esky, sunscreen, bug spray, first aid kit, etc.
  - [ ] Spirit bubble, spirit level (or angle measurement) and measuring tape
  - [ ] Portable fan (for cooling GOBI during data offload)
  - [ ] External power brick (for charging UAV RC)

---

## Flight Planning – DJI M350

1. Using a GPS survey system (Emlid, Trimble…) or GIS software, create a
   polygon of the area of interest with a 5-metre margin around the area of
   interest.
2. Using the GRYFN flight planning spreadsheet and DJI Pilot 2, set the
   parameters such as speed, overlap, and altitude. Orientation of the
   survey will be North–South in a paddock, or row-aligned for a plot trial.
3. Create two polygons: a *survey* polygon and a *capture* polygon. Ensure
   the *survey* polygon is 2× the flight speed larger than the *capture*
   polygon in the direction of travel (as per the figure below). Save both
   polygons uniquely.

   ![Survey vs capture polygon layout](APPN_GOBI_FieldBook_Rev1.0_media/image_154a62ad07f2.png)

4. If using QGIS, import the *capture* KML into Google Earth and immediately
   export it again. This is due to the required formatting Google Earth
   supplies.
5. Import the *capture* KML into the
   [HPI Polygon Tool](http://50.170.92.179/) and export. This polygon sets
   the activation of the hyperspectral sensor within Hyperspec3.
6. Import the *survey* polygon into DJI Pilot 2 (M350), or into
   QGroundControl (IF1200).
7. Using both the flight planning app (DJI Pilot 2 or QGroundControl) and
   the GRYFN flight calculator, determine the speed, altitude, and frame
   period required to survey the area of interest.
8. Ensure the frame period is > 20% oversampled and the side overlap is
   > 30%.

## Flight Planning – Inspired Flight IF1200A

1. *Need to add details here.*

---

## Pre-Flight

1. Conduct airspace and weather checks. If collecting hyperspectral data,
   collection time must be within ±2 hours of solar noon
   (refer: <https://gml.noaa.gov/grad/solcalc/>).
2. *(Optional)* Set up the Emlid RTK (install a peg or permanent GCP below
   the base station for recurring flights), let it run for at least
   15 minutes, and start recording the RINEX file before flying.
3. Set up reflectance targets on the tables for calibration and validation.
   2 sets of GRYFN reflectance panels should be used if available, at
   alternate ends of the capture, with the validation panel located
   centrally. Make sure you have GCPs installed (and coordinates recorded
   using Emlid) in the field for geometric calibration.
4. Set up a safe UAV RTH location, RTH altitude, and other geo-fencing
   settings on the respective drone.
5. Attach payload (Gobi or CALViS) to the aircraft:
   - Connect the power cable from aircraft to payload (non-standard payload
     bus only).
   - Connect both GNSS antenna cables to the correct ports (match A1 and
     A2).
   - Remove RGB and Nano HP lens caps.
   - Insert RGB SD card.
   - For M350, connect the C-type power cable to power the gimbal (make
     sure the B side of the cable is toward the outer side of the drone and
     the upper side of the light sensor).
   - For M350, activate the battery-powered fan (if warm ambient
     conditions). Avoid leaving GOBI powered on in stagnant air or high
     heat (> ~35–38 °C).
6. Power on the radio controller; check battery status.
7. Launch DJI Pilot 2 on the M350, or QGroundControl on the IF1200
   controller.
8. Review the flight plan, checking operational height.
9. Power on the aircraft; confirm connection to RC/GCS and battery status;
   ensure Remote ID is enabled (if flying the IF1200).
10. If you are using RTK (M350), check that you are receiving GNSS
    corrections. There should be more than 8 satellites for good correction
    (check the RTK fix in the M350 controller settings). The IF1200 does
    not use RTK, but ensure a minimum of 8 satellites and GPS.
11. Upload the flight plan to the aircraft (IF1200).

---

## Sensor Configuration

1. Place the exposure reference panel under the Nano HP lens; avoid casting
   shadows.
   - Place the drone legs upon exposure-angle cones, ensuring a fixed angle
     is achieved each exposure setting.
     **(angle provided through SIF excellence)**
2. Connect to GOBI Wi-Fi or connect the ethernet cable to the payload. Set
   a static IP address for the sensor at `10.0.65.2` (or anything other
   than `50`, `100`, and `128`, and must be less than `255`).
3. Navigate to the GOBI WebUI at `10.0.65.50`.
4. Ensure a valid elevation is achieved.
5. Name the mission, using the convention `YYYYMMDD_XXXX`
   (`YYYY` = year; `MM` = month; `DD` = day, must be 2 digits;
   `XXXX` = a short reference or abbreviation for the job).
6. Click **VNIR Setup**.
7. Open the Flight Calculator and update altitude/speed; adjust the
   oversampling buffer (must be at least 20%, recommended setting is 30%).
   **(value may change through hyperspectral excellence)**
8. Adjust exposure until ~95%
   **(value may change through hyperspectral excellence)** spectral
   saturation at the **peak of the 90th percentile line** without exceeding
   the frame period.
   - The maximum distance from the VNIR HS sensor to the GOBI reflectance
     panel is 40 cm. This is calculated based on the FOV and a 20 cm panel
     size.
9. Use the lowest gain mode that still provides sufficient saturation.
10. Import the polygon KML or text file.
11. Place the lens cap on the Nano HP.
12. Click **Collect Dark Reference**; remove the lens cap afterwards.
13. Remove the exposure reference panel.
14. Press **Start Mission**.
15. Remove the ethernet cable and begin flight operations.

---

## Flight Operations

1. Ensure the aircraft (M350) is in **Position** flight mode.
2. Sync the flight plan to the radio controller if applicable; double-check
   the flight plan.
3. Clear people/objects away from the UAV.
4. Notify crew/observers that takeoff is beginning.
5. Begin manual takeoff, check stick controls work, and then fly to ~12 m
   AGL; **do not exceed** the trigger altitude (20 m default) before
   mission start.
6. Perform dynamic alignment (one to two figure-8 patterns).
7. Enable autonomous mission.
8. Monitor UAV battery voltage/percentage in flight.
9. After mission, switch back to **Position** mode to regain manual
   control.
10. Lower to capture altitude and perform post-mission dynamic alignment
    (figure-8).
11. Land and disarm UAV.
12. Leave the UAV, transmitter, and sensor powered on; begin post-flight
    checks. Ensure data transfer is finished before turning off the sensor.
13. **Do not hot-swap the batteries.** Treat each flight as a new flight.

---

## Post-Flight Sensor Configuration

1. Reconnect to GOBI Wi-Fi or ethernet cable.
2. Open a browser to `10.0.65.50` or refresh the UI.
3. Press **Stop Mission**.
4. Replace the Nano HP and RGB lens caps.
5. Open WinSCP or equivalent and confirm the data.

---

## Post-Flight

1. Disconnect the ethernet cable from the payload.
2. Disconnect the aircraft batteries.
3. Disconnect the payload power cable.
4. Disconnect the payload GNSS cables.
5. Undo the mounting clamp, remove the payload, and place it in its case.

---

## Data Confirmation

| Sensor type   | File count                                                   | File size                                  | Notes                                                                                                  |
| ------------- | ------------------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **GNSS-INS**  | 1 file                                                       | ~1.5 MB per minute                         | A new file will be created if time rolls over the hour (UTC time, not capture time).                   |
| **LiDAR**     | 1 per minute                                                 | ~175 MB per file                           | First & last file may be smaller. Files may be smaller if over a low-reflectivity object.              |
| **VNIR**      | Mission time (s) ÷ Frame Period value ≈ number of data cubes | Several GB even for short flights.         | Check that `frameindex`, `imu_gps`, and `settings` files all exist.                                    |
| **RGB**       | One image every 2 s\* (by default)                           | ~30–70 MB per image                        | Check the event file vs the number of images.                                                          |

---

## Offload Data

1. Open WinSCP or similar FTP software.
2. Connect to the GRYFN Gobi via `gryfn@10.0.65.50` (password: `gryfn`).
3. Raw GNSS & LiDAR PCAP location: `/data/{mission name}`.
4. VNIR data location: `/data/capturedData/captured/{dateTime}`.
5. GOBI logs location: `/data/gryfn.log.{date}`.
6. RGB images are stored on the camera SD card.
7. Download GNSS, LiDAR, logs, and RGB after each mission; download
   hyperspectral data later due to its size.
8. Clear data directories after download to avoid filling the 500 GB SSD.

### Data storage, processing & validation

1. Downloaded data should be stored in the correct `T0_raw` folder of the [APPN Folder Structure](https://github.com/ArdenB/APPN_GenricFileStorage/wiki).
2. The bundeled .graw should be saved in the same `T0_raw` folder
3. The .gpro should be generated using the APPN GPT Pipeline (.json and wiki links TBD)
4. Standard QA process should be performed following [this guide](../QAprocess/APPN_AerialDataQC_Rev1.0.md)

---

## Appendix

### FTP & Service Reference

| Service           | Protocol | IP            | Port | User       | Password |
| ----------------- | -------- | ------------- | ---- | ---------- | -------- |
| GOBI              | FTP      | `10.0.65.50`  | 22   | `gryfn`    | `gryfn`  |
| SBG               | FTP      | `10.0.65.100` | 21   | `operator` | *(none)* |
| Headwall polygon  | HTTP     | `apps.headwallphotonics.com` | — | — | — |

### Headwall Polygon Tool — Workflow

1. Import KML.
   - Must be in Google Earth format.
2. Export KML.
3. Save KML.
4. In File Explorer, rename the KML as the survey name.

### Setting a Static IP Address

If connecting over an ethernet connection, a static IP address will need to
be set:

1. Open *Network and Internet Settings*.
2. Open *Change Adapter Options*.
3. Open *Properties* for the Ethernet port/adapter.
4. Open *Properties* for IPv4.
5. Set IP address to `10.0.65.2`.
6. Set subnet mask to `255.255.255.0`.
7. Press **OK**.

### IP Address Reference

| Service      | Address              |
| ------------ | -------------------- |
| GRYFN WebUI  | `10.0.65.50`         |
| HSInsight    | `10.0.65.50:8080`    |
| Ouster       | `10.0.65.128`        |
| SBG          | `10.0.65.100`        |



