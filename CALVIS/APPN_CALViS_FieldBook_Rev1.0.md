# APPN – CALViS Fieldbook

> This fieldbook provides a standardised operational guide for APPN CALViS UAV
> deployments, supporting safe flight operations, consistent sensor
> configuration, and high-integrity data capture. It is intended for trained
> APPN staff conducting hyperspectral, LiDAR, and GNSS-INS data acquisitions,
> and promotes repeatability, transparency, and confidence in downstream data
> analysis across APPN operations.

> **This protocol must be followed for all standard APPN CALViS UAV flights.**
> Adherence to these procedures is essential to ensure operational safety, data
> integrity, and comparability of datasets across deployments. For any flights
> that **fall outside standard operating procedures**, detailed records must be
> kept documenting all deviations, including the specific settings changed, the
> rationale for those changes, and any anticipated implications for data
> quality or analysis.

---

## Equipment Checklist

> Ensure batteries for all equipment are fully charged before heading to the
> field. Ensure charging cables are available for necessary equipment.

- **Aircraft**
  - Inspired Flight IF1200A
  - Aircraft batteries and spares
  - Landing gear
  - Landing pad
  - Spare parts
  - Tools
  - Logbook
- **Radio Control Transmitter / Ground Control Station**
- **Headwall CoAligned HP sensor payload**
  - Headwall coaligned system
  - GNSS antennae
  - Dovetail to XT60 + XT60 to XT30 cables/adapter
  - Dual ethernet cable and adaptor
  - Exposure reference panel
- **Ground reference kit**
  - Reflectance calibration panels (11%, 30%, 56%, 82%)
  - Calibration validation panels (20%, 45%)
  - Ground control points and RTK GNSS system
  - 2 × folding tables to elevate panels
  - *If over 50 km from CORS base station*, a portable RTK base station
    ([link to GRYFN gitbook](https://gryfn.gitbook.io/gryfn-operations/operations/base-station-availability))
- **Accessories**
  - Safety gear (signage and high-vis vests)
  - Aeronautical radio
  - Field laptop (with Headwall software installed) and spare batteries
  - External storage media
  - Water, food, esky, sunscreen, bug spray, first aid kit, etc.
  - Spirit bubble, spirit level (or angle measurement) and measuring tape
  - External power brick (for charging UAV RC)

---

## Preflight Planning

> Ensure that you apply for UAV flight approvals for locations and dates of
> flights well in advance.

1. Using a GPS survey system (Emlid, Trimble…) or a GIS software, create a
   polygon of the area of interest. Make sure your polygon includes the areas
   where you will place your calibration panels and GCPs, with an additional
   5 m buffer to avoid incomplete data.
2. Save this polygon twice as a KML — once as a *survey* polygon and once as a
   *capture* polygon.
3. If using QGIS, export the polygon as a KML (in Geometry, select *include
   z-dimension*, and ensure the CRS is set to WGS 84). Import the *capture*
   KML into the [HPI Polygon Tool](http://50.170.92.179/) and export. This
   polygon sets the activation of the hyperspectral sensor within Hyperspec3.
4. Import the *survey* polygon into QGroundControl.
5. Using both QGroundControl and the GRYFN flight calculator, determine the
   speed, altitude, and frame period required to survey the area of interest.
   - Do not go below 2 m/s or above 8 m/s for stability reasons (GRYFN).
     Speeds greater than 8 m/s lead to excessive aircraft pitch and speeds
     less than 2 m/s accentuate the impacts of wind on aircraft stability and
     cause a visibly less smooth trajectory.
   - Altitude and speed will be tested and recommended from APEx results.
   - Ensure the frame period is at a minimum of 20% oversampling, the side
     overlap is > 40% for the SWIR sensor, and the *turnaround distance* is
     2× flight speed (> 3× at > 6 m/s).
6. Ensure flight lines are in the direction of planting (GRYFN).

---

## Onsite Preflight Operations

1. Conduct airspace and weather checks. No cloud cover. Maximum wind speed
   15 km/h. Try to ensure the sun is ±20° of solar noon, approximately
   2 hours before or after noon (**however**, this will depend on time of year
   and latitude — please check
   [here](https://gml.noaa.gov/grad/solcalc/) if unsure).
   - *Optional:* set up the Emlid RTK (install a peg for recurring flights),
     let it run for at least 15 minutes, and start recording the RINEX file
     before flying.

2. Turn on the aeronautical radio and set to local CTAF (find in
   [ERSA](https://www.airservicesaustralia.com/aip/aip.asp)).

3. Set up reflectance targets for calibration and validation, using a spirit
   bubble to ensure they are all laid flat. Place 2 GCPs in the field to
   ensure geometric calibration. GCPs should be located next to calibration
   panels, and should be in alternate flight lines.

   - Both the calibration and validation panels should be placed on level
     folding tables to avoid dirt, reduce angle, and reduce spectral
     spillover. Having them level is important.
   - 2 sets of GRYFN calibration reflectance panels should be used if
     available, especially for flights longer than 15 minutes.
   - When using 1 calibration panel, the panel should be placed in the centre
     of a flight line in the middle of the flight.
   - When using two panels, they should be placed in the centre of flight
     lines 1/3 and 2/3 of the mission, noting that all missions would be less
     than 30 minutes long due to limitations of the IF1200.
   - You will need to move the panels if you will be flying multiple
     missions. Panels need to be in every flight in a multi-flight mission
     capture so that you fly over a calibration panel approximately every
     15 minutes.

   ![Calibration panel layout](APPN_CALViS_FieldBook_Rev1.0_media/image_a8646f9369b2.png)

4. Set up the landing pad and UAV in a safe RTH location.
   - In dusty environments, an additional tarp should be used under the
     landing pad.

5. Perform all on-ground safety checks for the UAV.

6. Attach the CALViS sensor payload to the aircraft.
   > **Warning:** The IF1200 dovetail has no hot-swap protection, so ensure
   > the IF1200 is powered off when attaching or removing the sensor
   > ([more details](https://gryfn.gitbook.io/gryfn-hardware/headwall-co-aligned-hp/user-manual/integration)).

   - Connect the 8-inch antenna mast with the Trimble AV18 antenna to the A1
     position (front left).
   - Slide the sensor into the dovetail mount, lock the dovetail latch, and
     clip on the safety wire.
   - Connect the power cable from aircraft to payload dovetail.
   - Connect the A1 GNSS antenna cable.
   - **Remove the lens cap!**
   - Clean the lens with approved cleaner (e.g.,
     [Zeiss Lens Wipes](https://eyesolutions.com.au/products/zeiss-lens-wipes),
     recommended by Gryfn).
   - Leave the LiDAR ethernet cable disconnected until ready for takeoff.

7. Power on the radio controller and/or ground control station.
   - Check radio controller / ground control battery status.

8. Launch QGroundControl on the controller.

9. Review the flight plan. Double-check the area of interest, GCPs, and
   reflectance panels are all within the capture polygon.

10. Power on the aircraft.
    - Ensure the radio controller / ground control station connects to the
      aircraft.
    - Check aircraft battery status.
    - Ensure Remote ID is enabled.

11. Upload the flight plan to the aircraft.

---

## Sensor Configuration — Hyperspec III (VNIR + SWIR)

1. Place the GRYFN exposure reference panel (82%) under the lens.
   - Point the centerline of the drone at the sun (to reduce shadows).
   - Ensure no shadow is cast on the exposure reference panel.

2. Connect the dual-ethernet cables to the VNIR and SWIR ports.

3. Ensure a static IP is set using the steps in the
   [Appendix](#appendix) of this document.

   | Sensor | Software       |
   | ------ | -------------- |
   | VNIR   | HS Insight     |
   | SWIR   | Hyperspec III  |

4. Open Hyperspec III.
   - Wait 2–3 minutes for the SWIR sensor to reach capture temperature.
     Hyperspec III won't connect until the SWIR is at temperature
     (listen for the click).

5. Navigate to the VNIR sensor.
   - Open *Live View*.

6. Set the **Frame Period** based on flight parameters using the
   [GRYFN Flight Calculator](https://gryfn.gitbook.io/gryfn-operations/operations/flight-planning/flight-planning-calculator)
   spreadsheet.

7. Adjust the Frame Period for sufficient oversampling.
   - GRYFN recommends adjusting oversample to 20% for standard flights and
     conditions.

8. Adjust **Exposure** until the spectral graph is ~95% saturated at peak
   (dependent on spectra of interest), while not exceeding the frame period
   value.
   - When adjusting exposure, use the lowest gain mode possible while still
     achieving sufficient saturation to boost SNR, without adjusting frame
     period.
   - Low gain is unlikely to ever be possible with SWIR (GRYFN).

9. Toggle Hyperspec III to the SWIR sensor.

10. Repeat the frame period / exposure steps for the SWIR sensor.

11. Open the **GPS** tab.

12. Upload the HSI polygon KML file.
    - Take note of the current ground-level altitude.

13. Open the **Capture** tab.
    - Ensure the number of active polygons shows the correct amount.

14. Update the name of the data collection folder.

15. Ensure the frame period and exposure have carried over properly from the
    Live Video tab sensors.

16. Ensure the number of active polygons shows the correct amount.

17. Place the lens cap on the sensor.

18. Toggle **Dark Reference**.

19. Click **Start**.
    - You should hear two clicks, signaling that the dark reference is
      complete.

20. After the dark reference is complete, open the **Advanced** tab next to
    polygons.

21. Recall your ground-level altitude from the GPS tab.

22. Set the minimum polygon altitude high enough above ground level to allow
    the alignment procedure.
    - 5–10 m above ground at minimum, preferably at least 20 m below flight
      altitude if possible.

23. Set the maximum polygon altitude high enough above your flight altitude
    to give buffer in case of slight altitude offsets.
    - At least 10 m above flight altitude. Unless the pilot plans on flying
      above the polygon to return home after the mission, this can be set as
      high as you'd like.

24. Press **Start**. Wait until the **Pause** icon appears.

25. Disconnect the ethernet cable from the VNIR and SWIR ports.

26. Remove the exposure reference panel.

27. **Remove the lens cap!**

28. Connect the LiDAR ethernet cable to the VNIR port.

29. Begin flight operations.

---

## Flight Operations

1. Ensure the aircraft is in **Position** flight mode.
2. Sync the flight plan to the radio controller if applicable.
3. Double-check the flight plan.
4. Clear people/objects away from the UAV.
5. Let crew/observers know you are about to take off.
6. Begin manual takeoff. Do not exceed the minimum polygon altitude until
   mission start.
7. Perform a dynamic alignment procedure outside the polygon (a figure-8 and
   back-and-forth manoeuvre at take-off and landing) at a recommended speed
   of **5 m/s**.
8. Enable autonomous mission.
9. Monitor UAV battery voltage/percentage in flight.
10. Upon completion of mission, return the aircraft to **Position** flight
    mode. The pilot will regain manual control of the aircraft.
11. Lower to alignment altitude and complete the post-mission dynamic
    alignment procedure.
12. Land and disarm the UAV.
13. Leave the UAV, transmitter, and sensor power on; move to post-flight
    checklists.

---

## Post-Flight Sensor Configuration

1. Disconnect the LiDAR ethernet cable from the VNIR port.
2. Connect the dual-ethernet cables to the VNIR and SWIR ports.
3. In Hyperspec III, open the **Capture** tab and press **Stop**.
4. Confirm data file sizes in Hyperspec III for both VNIR and SWIR sensors
   through the **Storage** tab.
   - Should be on a scale of thousands to tens or hundreds of thousands,
     depending on flight length.
   - Also look for LiDAR files for the flight; these are the `.pcap` files in
     the VNIR `captureddata` directory.
5. In a web browser, connect to the APX Web Configuration at
   `10.0.65.51:8080`.
6. After logging in, go to **Data Logging** and disable the session.
7. Turn off the drone and sensor.

---

## Post-Flight

1. Disconnect aircraft batteries.
2. Place the lens cap on the sensor.
3. Disconnect the ethernet cable from the payload.
4. Disconnect the payload GNSS cable.
5. Disconnect the payload power cable.
6. Undo the payload mounting latch, remove the payload, and place it in the
   storage case.
7. Pack up the aircraft.
8. Collect reflectance panels.

---

## Data Integrity Checks

| Sensor type   | File count                                                       | File size                                                            | Notes                                                                                                                          |
| ------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **GNSS-INS**  | 1 file per 3 minutes                                             | ~4–5 MB per file                                                     | First and last files may be smaller depending on start/stop time within the UTC minute.                                        |
| **LiDAR**     | 1 file per minute                                                | ~113 MB per file                                                     | First & last file may be smaller depending on start/stop time. Files may be smaller if over a low-reflectivity object.         |
| **VNIR**      | Mission time (s) ÷ Frame Period value ≈ number of data cubes     | Several GB of data even for short flights.                           | Check that `frameindex`, `imu_gps`, and `settings` files all exist.                                                            |
| **SWIR**      | Mission time (s) ÷ Frame Period value ≈ number of data cubes     | Several GB of data even for short flights.                           | Check that `frameindex`, `imu_gps`, `pps`, and `settings` files all exist.                                                     |

---

## Data Confirmation & Download

### VNIR, SWIR + LiDAR

1. Connect to the VNIR + SWIR ethernet ports.
2. Open Hyperspec III.
3. Open the **Data Storage** tab.
4. Select the mission folder.
5. Choose a local storage destination.
6. Navigate to the mission date.
7. Select all files.
8. Download all files.

### GNSS-INS

1. Connect to the SWIR ethernet port.
2. Open a web browser to `10.0.65.51:8080`.
3. Log in.
4. Open the **Data Logging** tab.
5. Click on **INTERNAL**.
6. Download all files from within that mission window.
7. The files required for GPT will be any with a matching UTC time to the
   VNIR or SWIR `imu_gps` file.

---

## Appendix

### Setting a Static IP Address

A static IP address needs to be set on the accessing machine to connect to
the sensors:

1. Open *Network and Internet Settings*.
2. Open *Change Adapter Options*.
3. Open *Properties* for the Ethernet port/adapter.
4. Open *Properties* for *Internet Protocol Version 4 (TCP/IPv4)*.
5. Use the following IP address: `10.0.65.2`
6. Subnet mask: `255.255.255.0`
7. Press **OK**.

### Network & Service Reference

| Service              | Address / details                                                              |
| -------------------- | ------------------------------------------------------------------------------ |
| APX WebUI (APX-15) — SWIR ethernet port | `10.0.65.51:8080`                                                              |
| FTP site             | IP `10.0.65.50`, port `22`, user `hpi`, password `HeadwallnHP###` (`###` = serial number of the Nano HP) |
| Headwall polygon tool | `apps.headwallphotonics.com`                                                  |

### Headwall Polygon Tool — Workflow

1. Import KML.
   - Must be in Google Earth format.
2. Export KML.
3. Save KML.
4. In File Explorer, rename the KML as the survey name.
__APPN–CALViS FIELDBOOK__

*This fieldbook provides a standardised operational guide for APPN CALViS UAV deployments, supporting safe flight operations, consistent sensor configuration, and high‑integrity data capture\. It is intended for trained APPN staff conducting hyperspectral, LiDAR, and GNSS‑INS data acquisitions, and promotes repeatability, transparency, and confidence in downstream data analysis across APPN operations\.*

*This protocol *__*must be followed*__* for all standard APPN CALViS UAV flights\. Adherence to these procedures is essential to ensure operational safety, data integrity, and comparability of datasets across deployments\. For any flights that *__*fall outside standard operating procedures*__*, detailed records must be kept documenting all deviations, including the specific settings changed, the rationale for those changes, and any anticipated implications for data quality or analysis\.*

__EQUIPMENT CHECKLIST__

*Ensure batteries for all equipment are fully charged before heading to the field\. Ensure charging cables are available for necessary equipment\. *

- __Aircraft__
	- Inspired Flight IF1200A
	- Aircraft batteries and spares
	- Landing gear
	- Landing pad
	- Spare parts
	- Tools
	- Logbook
- __Radio Control Transmitter / Ground Control Station__
- __Headwall CoAligned HP sensor payload__
	- Headwall coaligned system
	- GNSS antennae
	- Dovetail to XT60 \+ XT60 to XT30 cables/adapter
	- Dual ethernet cable and adaptor
	- Exposure reference panel
- __Ground reference kit__
	- Reflectance calibration panels \(11%, 30%, 56%, 82%\)
	- Calibration validation panels \(20%, 45%\)
	- Ground control points and RTK GNSS system
	- 2 x Folding tables to elevate panels
	- *If over 50 km from CORS base station*, a portable RTK base station \([link to GRYFN gitbook](https://gryfn.gitbook.io/gryfn-operations/operations/base-station-availability)\)
- __Accessories__
	- Safety gear \(signage and high vis vests\)
	- Aeronautical radio
	- Field laptop \(with Headwall software installed\) and spare batteries
	- External storage media
	- Water, food, esky, sunscreen, bug spray, first aid kit, etc\.
	- Spirit bubble, spirit level \(or angle measurement\) and measuring tape
	- External power brick \(For charging UAV RC\)

__PREFLIGHT PLANNING __

*Ensure that you apply for UAV flight approvals for locations and dates of flights well in advance\.*

1. Using a GPS survey system \(Emlid, Trimble…\) or a GIS software create a polygon of the area of interest\. Make sure your polygon includes the areas where you will place your calibration panels and GCPs, with an additional 5m buffer to avoid incomplete data\. 
2. Save this polygon twice as a KML\.  Once as a ‘survey’ polygon\.  Once as a ‘capture’ polygon\. 
3. If using QGIS, export the polygon as a kml \(in Geometry select include z\-dimension, and ensure the crs is set to WGS 84\)\. Import the ‘capture’ KML into [HPI Polygon Tool](http://50.170.92.179/) and export\. This polygon sets the activation of the hyperspectral sensor within Hyperspec3\. 
4. Import the ‘Survey’ polygon into QGroundControl\. 
5. Using both QGroundControl and the GRYFN flight calculator\. Determine the speed, altitude, and frame period required to survey the area of interest\. 
	- Do not go below 2 m/s or above 8 m/s for stability reasons \(GRYFN\), speeds greater than 8 m/s lead to excessive aircraft pitch and speeds less than 2 m/s accentuate the impacts of wind on aircraft stability and cause visibly less smooth trajectory\.
	- Altitude and speed will be tested and recommended from APEx results
	- Ensuring that the frame period is at a minimum 20% oversampling, the side overlap is >40% for the SWIR sensor, and the ‘turnaround distance’ is 2x flight\-speed \(>3x at >6m/s\)\.   
6. Ensure flight lines are in the direction of planting \(GRYFN\)\.

__ONSITE PREFLIGHT OPERATIONS__

1. Conduct airspace and weather checks\. No cloud cover\. Maximum wind speed 15 km/h?  Try to ensure sun is ±20°of solar noon, approximately 2 hours before or after noon \(__however__, *this will depend upon time of year and latitude so please check *[*here*](https://gml.noaa.gov/grad/solcalc/)* if unsure*\)
	- Set up the Emlid RTK \(install a peg for recurring flights\), let it run for at least 15 minutes, and start recording the RINEX file, before flying \(*OPTIONAL*\)\. 
2. Turn on aeronautical radio and set to local CTAF \(find in [ERSA](https://www.airservicesaustralia.com/aip/aip.asp)\)\.
3. Setup reflectance targets for calibration and validation, using spirit bubble to ensure they are all laid flat\. Placing 2 GCPs in the field to ensure geometric calibration\. GCPs should be located next to calibration panels, and ensure they are in alternate flight lines\. 

- Both the calibration and validation panels should be placed on a level folding tables to avoid dirt, reduce angle and reduce spectral spillover\. Having them level is important\.
- 2 sets of GRYFN calibration reflectance panels should be used if available especially for flight length >15 minutes
- When using 1 Calibration panel, the panel should be placed in the center of a flight line in the middle of the flight
- When using two panels, they should be placed in the center of flight lines 1/3 and 2/3 of the mission, noting that all missions would be less than 30 minutes long due to limitations of the IF1200\.
- You will need to move the panels if you will be flying multiple missions\. Panels need to be in every flight in multi\-flight mission capture so that you fly over a calibration panel approximately every 15 minutes\. 

![](APPN_CALViS_FieldBook_Rev1.0_media/image_a8646f9369b2.png)

1. Setup landing pad and UAV in a safe RTH location\. 

- In dusty environments an additional tarp should be used under the landing pad

1. Perform all on ground safety checks for UAV\.
2. Attach CALViS sensor payload to aircraft\. \(__Warning__: *The IF1200 dovetail has no hotswap protection so ensure that when attaching or removing the sensor that the IF1200 is powered off*, [more details](https://gryfn.gitbook.io/gryfn-hardware/headwall-co-aligned-hp/user-manual/integration)\)

- Connect the 8\-inch antenna mast with the Trimble AV18 antenna to the A1 position \(front left\)
- Slide sensor into dovetail mount, lock dovetail latch, clip on safety wire\.
- Connect power cable from aircraft to payload dovetail\.
- Connect the A1 GNSS antenna cable\.
- __Remove lens cap\!__
- Clean the lens with approved cleaner \(i\.e\., [Zeiss Lens Wipes](https://eyesolutions.com.au/products/zeiss-lens-wipes) recommended by Gryfn\)
- Leave LiDAR ethernet cable disconnected until ready for takeoff\.

1. Power on radio controller and/or ground control station\.

- Check radio controller/ground control battery status\.

1. Launch Q ground control software on control\.
2. Review flight plan\. Double check area of interest, GCPs and reflectance panels are all within capture polygon\.
3. Power on aircraft\.

- Ensure radio controller/ground control station connects to aircraft\.
- Check aircraft battery status\.
- Ensure Remote ID is enabled

1. Upload flight plan to aircraft\.

__SENSOR CONFIGURATION — Hyperspec III \(VNIR \+ SWIR\)__

1. Place GRYFN exposure reference panel \(82%\) under lens\. 

- Point the centerline of the drone at the sun \(to reduce shadows\)
- Ensure no shadow is cast on the exposure reference panel\.

1. Connect dual\-ethernet cables to VNIR and SWIR ports\.
2. Ensure static IP is set using the steps in Appendix of this document\.

VNIR – HS Insight – 

SWIR – Hyperspec III

1. Open Hyperspec III\.

- Wait 2–3 minutes for SWIR sensor to achieve capture temperature\. Hyperspec III won't connect to the SWIR is at temperature\. \(Listen for the click\)

1. Navigate to the VNIR sensor

- Open “Live View”

1. Set Frame Period based on flight parameters using [GRYFN Flight Calculator](https://gryfn.gitbook.io/gryfn-operations/operations/flight-planning/flight-planning-calculator) spreadsheet\.
2. Adjust Frame Period for sufficient oversampling

- GRYFN recommends adjusting oversample to 20%__ __for standard flights and conditions\. 

1. Adjust Exposure until Spectral Graph is ~95% saturated at peak \(dependent on spectra of interest\) while not exceeding frame period value\.

- When adjusting Exposure, use the lowest gain mode possible while still achieving sufficient saturation to boost SNR, without adjusting frame period\.
- Low gain is unlikely to ever be possible with SWIR \(GRYFN\)

1. Toggle Hyperspec III to the SWIR sensor\.
2. Repeat frame period/exposure steps for the SWIR sensor\.
3. Open GPS tab\.
4. Upload HSI polygon KML file\.

- Take note of current ground\-level altitude\.

1. Open Capture tab

- Ensure number of active polygons shows the correct amount\.

1. Update the name of the data collection folder\.
2. Ensure frame period and exposure have carried over properly from the Live Video tab sensors\.
3. Ensure number of active polygons shows the correct amount\.
4. Place lens cap on sensor\.
5. Toggle Dark Reference\.
6. Click Start\.

- You should hear two clicks, signaling dark reference is complete\.

1. After dark reference is complete, open the Advanced tab next to polygons\.
2. Recall your ground\-level altitude from the GPS tab\.
3. Set the minimum polygon altitude high enough above ground level to allow alignment procedure\.

- 5–10 m above ground at minimum, preferably at least 20 m below flight altitude if possible\.

1. Set the maximum polygon altitude high enough above your flight altitude to give buffer in case of slight altitude offsets

- At least 10 m above flight altitude\. Unless pilot plans on flying above the polygon to return home after the mission, this can be set as high as you’d like\.

1. Press Start\. Wait until the Pause icon appears\.
2. Disconnect ethernet cable from VNIR and SWIR ports\.
3. Remove exposure reference panel\.
4. __Remove Lens CAP\!__
5. Connect LiDAR ethernet cable to VNIR port\.
6. Begin flight operations\.

__FLIGHT OPERATIONS__

1. Ensure aircraft is in Position flight mode\.
2. Sync flight plan to radio controller if applicable\.
3. Double check flight plan\.
4. Clear people/objects away from UAV\.
5. Let crew/observers know you are about to takeoff\.
6. Begin manual takeoff\. Do not exceed minimum polygon altitude until mission start\.
7. Perform a dynamic alignment procedure outside the polygon \(A Figure\-8 and back\-and\-forth maneuver at take\-off and landing\) at a recommended speed of __5m/s__\.	
8. Enable autonomous mission\.
9. Monitor UAV battery voltage/percentage in flight\.
10. Upon completion of mission, return aircraft to Position flight mode\. Pilot will regain manual control of aircraft\.
11. Lower to alignment altitude and complete post\-mission dynamic alignment procedure\.
12. Land and disarm the UAV\.
13. Leave UAV, transmitter, and sensor power on, move to post\-flight checklists\.

__POST\-FLIGHT SENSOR CONFIGURATION__

1. Disconnect LiDAR ethernet cable from VNIR port\.
2. Connect dual\-ethernet cables to VNIR and SWIR ports\.
3. In Hyperspec III open Capture tab, press Stop\.
4. Confirm data file sizes in Hyperspec III for both VNIR and SWIR sensors through the storage tab\.

- Should be on a scale of thousands to tens or hundreds of thousands depending on flight length\.
- Also look for LiDAR files for the flight these are the \.pcap files in the VNIR captureddata directory\.

1. In web browser, connect to APX Web Configuration @ 10\.0\.65\.51:8080
2. After logging in, go to Data Logging and Disable the session\.
3. Turn off the drone and sensor\.

__POST\-FLIGHT__

1. Disconnect aircraft batteries\.
2. Place lens cap on sensor\.
3. Disconnect ethernet cable from payload\.
4. Disconnect payload GNSS cable\.
5. Disconnect payload power cable\.
6. Undo payload mounting latch, remove payload, and place in storage case\.
7. Pack up aircraft\.
8. Collect reflectance panels\.

__DATA INTEGRITY CHECKS__

__SENSOR TYPE__

__GNSS\-INS__

__LiDAR__

__VNIR__

__SWIR__

__FILE COUNT__

1 file per 3 minutes

1 file per minute

Mission time \(s\) ÷ Frame Period value ≈ number of data cubes

Mission time \(s\) ÷ Frame Period value ≈ number of data cubes

__FILE SIZE__

~4–5 MB per file

~113 MB per file

VNIR data should capture several GB of data for even short flights\.

SWIR data should capture several GB of data for even short flights\.

__NOTES__

First and last files may be smaller depending on start/stop time within the UTC minute\.

First & last file may be smaller depending on start/stop time\. Files may be smaller if over low reflectivity object\.

Check that frameindex, imu\_gps, and settings files all exist\.

Check that frameindex, imu\_gps, pps, and settings files all exist\.

__DATA CONFIRMATION & DOWNLOAD__

__VNIR, SWIR, \+ LiDAR__

__GNSS\-INS__

1\. Connect to VNIR \+ SWIR ethernet ports\.

1\. Connect to SWIR ethernet port\.

2\. Open Hyperspec III\.

2\. Open web browser to: 10\.0\.65\.51:8080

3\. Open Data Storage tab\.

3\. Login\.

4\. Select mission folder\.

4\. Open Data Logging tab\.

5\. Choose local storage destination\.

5\. Click on INTERNAL\.

6\. Navigate to mission date\.

6\. Download all files from within that mission window

7\. Select all files\.

7\. The files required for GPT will be any with a matching UTC time to the VNIR or SWIR “imu\_gps” file\.

8\. Download all files\.

__APPENDIX__

__SETTING STATIC IP ADDRESS__

A static IP address needs to be set on the accessing machine to connect to the sensors:

1. Open Network and Internet Settings
2. Change Adapter Options
3. Open Properties for Ethernet port/adapter
4. Open Properties for Internet Protocol Version 4 \(TCP/IPv4\)
5. Use the following IP Address: 10\.0\.65\.2
6. Subnet Mask: 255\.255\.255\.0
7. Press OK

__IP ADDRESS__

__FTP SITE__

__HEADWALL POLYGON__

APX WebUI \- APX\-15 \- SWIR Ethernet Port: 10\.0\.65\.51:8080

IP Address: 10\.0\.65\.50

Port: 22

User: hpi

Password: HeadwallnHP\#\#\# \(where \#\#\# is the serial number of the Nano HP\)

apps\.headwallphotonics\.com

1\. Import KML

    • Must be in Google Earth format\. 

2\. Export KML

3\. Save KML

4\. In File Explorer, rename KML as survey name

