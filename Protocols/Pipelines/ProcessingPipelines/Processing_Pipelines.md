# Processing Pipelines

**Version 0.1 – DRAFT, May 2026**

> [!IMPORTANT]
> This page documents the **standardised GRYFN processing pipelines** used
> within APPN for UAV-based data processing, intended for trained APPN staff
> processing CALViS and GOBI. Adherence to the
> pipelines below ensures reproducibility, quality assurance, and
> cross-project comparability. For any processing run that **deviates from
> the standard pipeline**, detailed records must be kept of every parameter
> changed, the rationale, and any anticipated implications for data quality.

This page documents the standardised GRYFN processing pipeline YAML files used
within APPN for UAV-based data processing. These YAML configurations define
consistent, transparent, and repeatable processing workflows across
GRYFN-supported sensors and platforms, supporting reproducibility, quality
assurance, and cross-project comparability. The files are intended to be used
as reference and default templates for approved processing pipelines, with any
deviations explicitly documented to maintain traceability and data integrity.

The standard pipelines and the data products they output are detailed below.
For a tabular summary of output formats, resolutions and software
compatibility, see
[Standard Data Products](../../Background/StandardDataProducts/Standard_Data_Products.md).

For additional information about all steps in this document, see the 
[Gryfn Documentation](https://gryfn.gitbook.io/gryfn-software/documentation/quick-start-guide)

---

## Document Structure

- [🌿 CALViS — Standard Processing Pipeline](#-calvis--standard-processing-pipeline)
  - [1. Configure GPT defaults](#1-configure-gpt-defaults)
  - [2. Format the raw data](#2-format-the-raw-data)
  - [3. Create the graw bundle](#3-create-the-graw-bundle)
  - [4. Load the Calvis_standard_pipeline](#4-load-the-calvis_standard_pipeline)
  - [5. Run the pipeline on a graw](#5-run-the-pipeline-on-a-graw)
  - [CALViS outputs](#calvis-outputs)
- [🌱 GOBI — Standard Processing Pipeline](#-gobi--standard-processing-pipeline)
  - [GOBI outputs](#gobi-outputs)

---

## 🌿 CALViS — Standard Processing Pipeline

This section describes the standard CALViS processing workflow using the
[`Calvis_standard_pipeline_v1.0.yaml`](https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures/blob/main/Protocols/Pipelines/ProcessingPipelines/yaml/Calvis_standard_pipeline_v1.0.yaml)
file in the GRYFN Processing Tool (**GPT, v1.9.2**).

> [!NOTE]
> The pipeline YAML lives in
> [`Protocols/Pipelines/ProcessingPipelines/yaml/`](https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures/tree/main/Protocols/Pipelines/ProcessingPipelines/yaml).
> Download the latest version from the link above before importing it
> into GPT (see [Step 4](#4-load-the-calvis_standard_pipeline)).

### 1. Configure GPT defaults

Before processing any data, configure GPT so that it uses the correct
radiometric calibration files and points to the correct panel target files.

![GPT defaults dialog showing radiometric calibration and reflectance target paths](Processing_Pipelines_media/GPT_defaults.png)

#### Sensor identification (boresight calibration)

Each CALViS unit has a unique sensor identifier embedded in the boresight
calibration filename. The naming convention is:

**Example:** `20250527_cAHP-191_SystemCal.yml`

Where `191` is the USYD sensor number; each CALViS unit is assigned its own
unique number.

> [!IMPORTANT]
> When processing data, you **must** verify that the sensor number in the
> boresight calibration file matches the sensor used for data collection.

#### Radiometric calibration files

Each sensor has an associated set of radiometric calibration files supplied
by GRYFN. The radiometric calibration folder contains subfolders; it is
recommended to remove the `.nuc` folder and keep the `.raw` folder to prevent
the Gryfn Processing Tool from grabbing the wrong files.

> [!IMPORTANT]
> Verify that the **Radiometric Calibration Location** parameter in GPT
> points to the correct calibration files for your specific sensor(s).

#### Reflectance target values

The Empirical Line Method (ELM) requires accurate reflectance target values
for the calibration panels.

- Four (4) calibration panels are used for the ELM process.
- Each panel has specific, measured target reflectance values.
- These values are unique to your panel set.

> [!IMPORTANT]
> Ensure the **Reflectance Target Location** parameter references the
> correct target values that correspond to your specific calibration
> panels.

### 2. Format the raw data

The example CALViS flight used here is `run_00`, a flight from UOA.

A complete CALViS dataset has four key components — **VNIR, SWIR, LiDAR,
and GNSS** — and these must be arranged correctly before a working graw
can be bundled. The raw data folder will look like this:

![Example CALViS RAW folder layout showing VNIR, SWIR, LiDAR and GNSS components](Processing_Pipelines_media/RAW_FOLDER_EG.png)

> [!NOTE]
> When you download the VNIR data it has the **LiDAR data nested inside**
> the VNIR folder, and the **VNIR dark frames** are in the same folder.
> The **SWIR dark frames** are in a separate folder. The GNSS folder
> contains the relevant `.TO4` files.

### 3. Create the graw bundle

#### Pre-bundle checks

Before each graw, confirm you have:

- [ ] System calibration file (matching the sensor used).
- [ ] Radiometric calibration files.
- [ ] Reflectance target file.

![UOA calibration paths](Processing_Pipelines_media/UOA_cals.png)

#### Bundling steps

1. **Set the system calibration file** to match the sensor you are using.

   ![GPT system calibration selection dialog](Processing_Pipelines_media/Sys_cal_set.png)

2. **Choose the raw data path.**

   ![GPT raw data path selection](Processing_Pipelines_media/raw_path.png)

3. **Click *Next*** to view the optional parameters.

   ![GPT bundling optional parameters dialog](Processing_Pipelines_media/optional.png)

   > [!NOTE]
   > Unless you have a specific reason to set an extent, **leave it
   > blank** — data can be cropped to the hyperspectral capture area
   > later, which is ideal for most standard flights. Other fields here
   > are also optional.

4. **Click *Next***. Give the bundle a logical name and save it under
   `T0_raw`.

   ![Save graw dialog with bundle named and saved under T0_raw](Processing_Pipelines_media/save_graw.png)

5. **Click *Create bundle***. You should see a progress report while the
   bundle is being created.

   ![Bundle creation progress dialog](Processing_Pipelines_media/bundle_prog.png)

### 4. Load the Calvis_standard_pipeline

Import the standard CALViS pipeline YAML
([`Calvis_standard_pipeline_v1.0.yaml`](https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures/blob/main/Protocols/Pipelines/ProcessingPipelines/yaml/Calvis_standard_pipeline_v1.0.yaml))
into GPT before running a job for the first time:

1. Open the pipelines manager.

   ![GPT pipelines manager — step 1 of upload](Processing_Pipelines_media/pipe1.png)

2. Import the `Calvis_standard_pipeline` YAML.

   ![GPT pipeline import dialog — step 2 of upload](Processing_Pipelines_media/pipe2.png)

3. Confirm the imported pipeline is listed.

   ![GPT pipelines manager showing imported Calvis_standard_pipeline — step 3 of upload](Processing_Pipelines_media/pipe3.png)

### 5. Run the pipeline on a graw

1. Select **New Job** and choose **Calvis_std** from the pipelines list.
   Choose your graw, name your gpro, and set the gpro output location.

   ![New job dialog: graw selection and gpro output path](Processing_Pipelines_media/gpro_file_paths.png)

   > [!IMPORTANT]
   > The gpro **must** be saved under `T1_proc`.

2. Configure GNSS processing. We currently recommend **PPRTX**.

   ![GNSS processing configuration dialog](Processing_Pipelines_media/GNSS.png)

   > [!CAUTION]
   > Double-check your **Datum**, **Grid**, and **Zone** before
   > continuing. Errors here propagate through every downstream product.

3. Load the reflectance target files. For this example flight we use the
   UOA panel target files.

   ![Reflectance target file selection — UOA panels](Processing_Pipelines_media/load_targets.png)

4. **VNIR ELM.** Cycle through the images until you find the four panels,
   then click **Draw target bounds**.

   ![Cycling through VNIR images to locate the four ELM panels](Processing_Pipelines_media/find_elm_vnir.png)

   Choose a target to work on:

   ![Selecting a VNIR ELM target panel](Processing_Pipelines_media/choose_targ_elm.png)

   Hold right-click and drag a rectangle around the panel:

   ![Drawing a target-bounds rectangle around a VNIR panel](Processing_Pipelines_media/11.png)

   Repeat for the remaining three panels:

   ![All four VNIR panels with target bounds drawn](Processing_Pipelines_media/vnir_done.png)

5. **SWIR ELM.** The process is the same as VNIR.

   ![SWIR ELM showing water bands (red box) and rogue values (red circle)](Processing_Pipelines_media/swir_eg.png)

   > [!TIP]
   > The SWIR will have water bands (red box in the figure above) and
   > sometimes rogue values (red circle). As a rule of thumb, **draw
   > normal-sized boxes that cover the panel** rather than cherry-picking
   > small areas to get a neater ELM.

6. Click **Submit**.

### CALViS outputs

The CALViS standard pipeline produces the LiDAR and hyperspectral products
listed below. See
[Standard Data Products](../../Background/StandardDataProducts/Standard_Data_Products.md)
for the canonical specifications, file sizes, and software compatibility.

| Product | Output filename | Resolution | Format | Notes |
|---|---|---|---|---|
| LiDAR Digital Surface Model (DSM) | `LiDAR_DSM.tif` | 8 cm (fixed) | GeoTIFF | Extent: VNIR scene |
| LiDAR Digital Terrain Model (DTM) | `LiDAR_DTM.tif` | 1 m | GeoTIFF | Extent: processing extent |
| Combined LiDAR Point Cloud | `LiDAR_CombinedPointCloud.las/.laz` | Native point spacing | LAS | Outliers removed during combination |
| VNIR Orthomosaic | `VNIR_Orthomosaic.bin` | 4 cm (GSD-based) | ENVI (`.bin` + `.hdr`) | binning = 2, radiometric calibration applied |
| SWIR Orthomosaic | `SWIR_Orthomosaic.bin` | 4 cm (GSD-based) | ENVI (`.bin` + `.hdr`) | binning = 2, radiometric calibration applied |

### Inspecting the CALViS Outputs. 

To inspect the DSM, DTM, RGB orthomosiac and the VNIR orthomosiac we recommend  QGIS https://qgis.org/, shown below is QGIS v4.0 +, to view the pointcloud we recommend CloudCompare https://www.cloudcompare.org/. Note that the same approach works for the GOBI products, the only difference being the RGB orthomosiac whcih can also be viewed in QGIS. 

The data outputs are stored in the "products" folder in the gpro 

   ![CALVIS_products](Processing_Pipelines_media/CALVIS_products.png)

#### Inspecting the VNIR orthomosiac

Open QGIS 4 and drag and drop the VNIR ".bin" then select "add layers"

   ![CALVIS_products](Processing_Pipelines_media/load_vnir_qgis.png)

You will notice that the hyperspectral orthomosiac has a poor visualisation , this is because the default bands (wavelengths) visualised in in QGIS are not ideal. We recommend setting the visualisation to Red Green Blue. To do this double click the file in the “Layers” section of QGIS, navigate to symbology and set the Red Green and Blue bands to the appropriate colour. 


   ![CALVIS_products](Processing_Pipelines_media/RGB_VNIR.png)

Next, it can be helpful to investigate, and sanity check some reflectance values.  To do this we can use the “Identify Features” button.  Click the button and then click a pixel on the orthomosiac. A good sanity check is to use a GRYFN panel, for example click on the 30% panel and check that the values are hovering around the 30% reflectance. One you click a pixel it defaults to a table, switching it to “graph” can make it easier to quickly interpret.  

   ![CALVIS_products](Processing_Pipelines_media/qgis_31_panel_vnir.png)

Following this you can click on grass, a crop, whatever is of interest to your flight (below is grass) 

   ![CALVIS_products](Processing_Pipelines_media/qgis_grass.png)

The steps for the SWIR are the same except  there are no presets for RGB bands. 


If your VNIR Orthmosiac looks  odd, it can be good to check your DSM to make sure the LIDAR was working. To investigate your DSM just drag and drop the “.TIF” file into QGIS (note that this is actually a GeoTiff and contains spatial information). Make sure that the min max values make logical sense (e.g. the distance between the ground and the tallest feature)

![alt text](Processing_Pipelines_media/qgis_dsm.png)

Lastly, if you want to view your point cloud you can drag and drop the (.las or .laz file) into CloudCompare

![alt text](Processing_Pipelines_media/cloud_compare.png)

![alt text](Processing_Pipelines_media/cloud_compare_yes_to_all.png)

![alt text](Processing_Pipelines_media/cloud_compare_point_cloud.png)

All these steps apply to the GOBI the only difference being the RGB image (which is a Geotiff and loads just like the DSM)


---

## 🌱 GOBI — Standard Processing Pipeline

The GOBI standard processing pipeline is defined by
[`Gobi_standard_pipeline_v1.0.yaml`](https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures/blob/main/Protocols/Pipelines/ProcessingPipelines/yaml/Gobi_standard_pipeline_v1.0.yaml).

> [!NOTE]
> The GOBI workflow closely mirrors the CALViS walkthrough above; only
> the GOBI-specific differences are called out below.

The GOBI processing worflow is very similar to the CALViS. The main difference is that there is no SWIR but there is RGB data. 

### 1. Configure GPT defaults

Repeated to make sure double checking is done

Before processing any data, configure GPT so that it uses the correct
radiometric calibration files and points to the correct panel target files.

![GPT defaults dialog showing radiometric calibration and reflectance target paths](Processing_Pipelines_media/GPT_defaults.png)

#### Sensor identification (boresight calibration)

Each GOBI unit has a unique sensor identifier embedded in the boresight
calibration filename. The naming convention is:

**Example:** `20241008_GOBI2405-APPN3_SystemCal.yml`

Where `APPN3` is the USYD sensor number; each GOBI unit is assigned its own
unique number.


> [!IMPORTANT]
> When processing data, you **must** verify that the sensor number in the
> boresight calibration file matches the sensor used for data collection.

#### Radiometric calibration files

Each sensor has an associated set of radiometric calibration files supplied
by GRYFN.

> [!IMPORTANT]
> Verify that the **Radiometric Calibration Location** parameter in GPT
> points to the correct calibration files for your specific sensor(s).

#### Reflectance target values

The Empirical Line Method (ELM) requires accurate reflectance target values
for the calibration panels.

- Four (4) calibration panels are used for the ELM process.
- Each panel has specific, measured target reflectance values.
- These values are unique to your panel set.

> [!IMPORTANT]
> Ensure the **Reflectance Target Location** parameter references the
> correct target values that correspond to your specific calibration
> panels.

### 2. Format the raw data

The example CALViS flight used here is `run_00`, a flight from USYD.

A complete CALViS dataset has four key components — **VNIR, RGB, LiDAR,
and GNSS** — and these must be arranged correctly before a working graw
can be bundled. The raw data folder will look like this:

![Example CALViS RAW folder layout showing VNIR, SWIR, LiDAR and GNSS components](Processing_Pipelines_media/gobi_raw_files.png)

### 3. Create the graw bundle

#### Pre-bundle checks

Before each graw, confirm you have:

- [ ] System calibration file (matching the sensor used).
- [ ] Radiometric calibration files.
- [ ] Reflectance target file.

![UOA calibration paths](Processing_Pipelines_media/GOBI_gen_settigs_usyd.png)

### Note here we switched from UOA to USYD

#### Bundling steps

1. **Set the system calibration file** to match the sensor you are using.

   ![GPT system calibration selection dialog](Processing_Pipelines_media/GOBI_bore_gpt.png)

2. **Choose the raw data path.**

   ![GPT raw data path selection](Processing_Pipelines_media/GOBI_raw_path_graw.png)

3. **Click *Next*** to view the optional parameters.

   ![GPT bundling optional parameters dialog](Processing_Pipelines_media/optional.png)

   > [!NOTE]
   > Unless you have a specific reason to set an extent, **leave it
   > blank** — data can be cropped to the hyperspectral capture area
   > later, which is ideal for most standard flights. Other fields here
   > are also optional.

4. **Click *Next***. Give the bundle a logical name and save it under
   `T0_raw`.   

    ![Save graw dialog with bundle named and saved under T0_raw](Processing_Pipelines_media/name_gobi_bundle.png)

5. **Click *Create bundle***.   

### 4. Load the GOBI_standard_pipeline

Import the standard GOBI pipeline YAML
([`Calvis_standard_pipeline_v1.0.yaml`](https://github.com/ArdenB/APPN-Aerial-Standard-Operating-Procedures/blob/main/Protocols/Pipelines/ProcessingPipelines/yaml/Gobi_standard_pipeline_v1.0.yaml))

1. Open the pipelines manager.

   ![GPT pipelines manager — step 1 of upload](Processing_Pipelines_media/pipe1.png)


2. Import the `Gobi_standard_pipeline` YAML.

   ![GPT pipeline import dialog — step 2 of upload](Processing_Pipelines_media/load_gobi_pipeline.png)   

 3. Confirm the imported pipeline is listed.

   ![GPT pipelines manager showing imported Calvis_standard_pipeline — step 3 of upload](Processing_Pipelines_media/GOBI_std_save.png)  

### 5. Run the pipeline on a graw

1. Select **New Job** and choose **Gobi_std** from the pipelines list.
   Choose your graw, name your gpro, and set the gpro output location.   

    ![New job dialog: graw selection and gpro output path](Processing_Pipelines_media/gobi_gpro_step1_setgraw_and_gpro.png)

   > [!IMPORTANT]
   > The gpro **must** be saved under `T1_proc`.  

2. Configure GNSS processing. 

   ![GNSS processing configuration dialog](Processing_Pipelines_media/GOBI_GNSS_CRS.png)

   > [!CAUTION]
   > Double-check your **Datum**, **Grid**, and **Zone** before
   > continuing. Errors here propagate through every downstream product.  

  There is no PPRTX option for GOBI.  
  
  3. Load the reflectance target files. For this example flight we use the
   UOA panel target files.

   ![Reflectance target file selection — USYD panels](Processing_Pipelines_media/gobi_usyd_targets.png)

   4. **VNIR ELM.** Cycle through the images until you find the four panels,
   then click **Draw target bounds**. (note explained in greater detail in the CALViS steps above)

   ![Selecting a VNIR ELM target panel](Processing_Pipelines_media/GOBI_ELM.png)
   


### GOBI outputs

The GOBI standard pipeline produces the LiDAR, hyperspectral, and RGB
products listed below. See
[Standard Data Products](../../Background/StandardDataProducts/Standard_Data_Products.md)
for the canonical specifications, file sizes, and software compatibility.

| Product | Output filename | Resolution | Format | Notes |
|---|---|---|---|---|
| LiDAR Digital Surface Model (DSM) | `LiDAR_DSM.tif` | 8 cm (fixed) | GeoTIFF | Extent: VNIR scene |
| LiDAR Digital Terrain Model (DTM) | `LiDAR_DTM.tif` | 1 m | GeoTIFF | Extent: processing extent |
| Combined LiDAR Point Cloud | `LiDAR_CombinedPointCloud.las` | Native point spacing | LAS | Outliers removed during combination |
| VNIR Orthomosaic | `VNIR_Orthomosaic.bin` | 4 cm (GSD-based) | ENVI (`.bin` + `.hdr`) | binning = 2, radiometric calibration applied |
| RGB Orthomosaic | `RGB_Orthomosaic.tif` | 0.6 cm (fixed) | GeoTIFF | Feature-matching (SIFT) bundle adjustment applied |

