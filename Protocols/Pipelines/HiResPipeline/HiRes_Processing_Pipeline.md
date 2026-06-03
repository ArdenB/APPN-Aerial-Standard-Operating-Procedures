# HiRes Processing Pipeline

> [!CAUTION]
> Portions of this method are **still under development**, with work continuing
> over the 2026 winter season. The flight parameters in the
> [HiRes Fieldbook](../../Sensors/HIRES/HIRES_FieldBook.md) were chosen to
> allow the different processing methods to be tested robustly. 


> [!IMPORTANT]
> This page documents the **standardised GRYFN processing pipelines** used
> within APPN for UAV-based data processing, intended for trained APPN staff
> processing CALViS, GOBI, HiRes, and M3M datasets. Adherence to the
> pipelines below ensures reproducibility, quality assurance, and
> cross-project comparability. For any processing run that **deviates from
> the standard pipeline**, detailed records must be kept of every parameter
> changed, the rationale, and any anticipated implications for data quality.

This page documents the standardised HiRES (PhaseOne) processing pipeline
within APPN for UAV-based data processing. These configurations define
consistent, transparent, and repeatable processing workflows across
GRYFN-supported sensors and platforms, supporting reproducibility, quality
assurance, and cross-project comparability. The files are intended to be used
as reference and default templates for approved processing pipelines, with any
deviations explicitly documented to maintain traceability and data integrity.

The standard pipelines and the data products they output are detailed below.
For a tabular summary of output formats, resolutions and software
compatibility, see
[Standard Data Products](../../Background/StandardDataProducts/Standard_Data_Products.md).


---

## Document Structure

- [Processing methods](#processing-methods)
  - [Method 1 — Orthomosaic in Agisoft Metashape](#method-1--orthomosaic-in-agisoft-metashape)
  - [Image tiling methods (in development)](#image-tiling-methods-in-development)
    - [PhaseOne iX Capture (Windows GUI)](#phaseone-ix-capture-windows-gui)
    - [PhaseOne Image SDK (Linux CLI / shell scripts)](#phaseone-image-sdk-linux-cli--shell-scripts)

---

## Processing methods


APPN's HiRes (PhaseOne) processing approach is still being developed. The
method documented in full below is **Method 1 — an orthomosaic workflow in
Agisoft Metashape**, which currently serves as a practical, hands-on starting
point for working with HiRes data.

There are also two **image tiling methods**, based on the
[PhaseOne iX Capture / Image SDK](https://geospatial.phaseone.com/) toolchain,
which were developed independently by **UWA**/**DPIRD** and **UQ**. Ongoing work over the
season is focused on combining them into a single, unified approach, which will
be documented in future revisions of this protocol.

| # | Method | Status | Developed by | Toolchain | Operating system | Primary output |
|---|--------|--------|--------------|-----------|------------------|----------------|
| 1 | Orthomosaic in Agisoft Metashape | Documented (interim) | APPN | Agisoft Metashape | Windows or Linux | RGB orthomosaic + DEM |
| — | Image tiling — PhaseOne iX Capture (GUI) | In development | UWA/DPIRD | PhaseOne iX Capture (GUI) | Windows | Calibrated, tiled RGB frames |
| — | Image tiling — PhaseOne Image SDK (CLI) | In development | UQ | PhaseOne Image SDK + shell scripts | Linux | Calibrated, tiled RGB frames |

> [!NOTE]
> Method 1 is an **interim** workflow for getting familiar with the data; the
> APPN-uniform approach has not yet been confirmed. Its main advantage is that
> it is **easy to implement** and produces a **single data product** that is
> straightforward to work with and to display. The trade-off is that the
> stitching process introduces some **mosaicing artefacts** and a slight
> **loss of resolution**.
>
> The two **image tiling methods** were developed independently by UWA/DPIRD and UQ.
> Both apply the same PhaseOne radiometric calibration, lens correction, and
> geometric model, and ongoing work this season is focused on reconciling them
> into a **single, unified approach**.

---

### Method 1 — Orthomosaic in Agisoft Metashape

> [!NOTE]
> This is an interim, hands-on workflow so those new to HiRes can get a feel
> for the data and Agisoft. It is not perfect and is not a one-size-fits-all
> approach. The APPN-uniform approach has not been confirmed as of yet.
> — Richard Harwood

#### Step 1 — Locate the processed JPEGs

![Folder of processed JPEGs](HiRes_Processing_Pipeline_media/1_folder_of_jpgs_processed.png)

Start with a folder of the processed HiRes JPEG frames ready for import.

#### Step 2 — Prepare the AeroPoints / GCP file

![Formatted AeroPoints](HiRes_Processing_Pipeline_media/2_formatted_aeropoints.png)

Format the AeroPoints (ground control points) into the layout Metashape
expects — label, easting/northing (or lat/lon), and elevation.

#### Step 3 — Load the JPEGs into Agisoft

![JPEGs loaded into Agisoft](HiRes_Processing_Pipeline_media/3_jpges_loaded_agisoft.png)

Drag and drop (or **Add Photos**) the processed JPEGs into the Metashape
chunk so the images appear in the workspace.

#### Step 4 — Set / convert the coordinate reference system

![Convert CRS](HiRes_Processing_Pipeline_media/4_convert_CRS.png)

Set the camera CRS and convert it to the project's target CRS so the imagery
and control points share the same coordinate system.

#### Step 5 — Import the AeroPoints

![Load AeroPoints](HiRes_Processing_Pipeline_media/5_load_aerpoints.png)

Import the formatted AeroPoints file as markers/GCPs, mapping the columns to
the correct coordinate fields.

#### Step 6 — Check the imported AeroPoints

![Check loaded AeroPoints](HiRes_Processing_Pipeline_media/5_load_aerpoints_check.png)

Verify the markers loaded correctly and sit in sensible positions relative to
the camera locations.

#### Step 7 — Hit "Yes to all"

![Yes to GCP](HiRes_Processing_Pipeline_media/6_yes_to_gcp.png)


#### Step 8 — Set up Align photos

![Align photos](HiRes_Processing_Pipeline_media/7_align_photos.png)

Run **Align Photos** to estimate camera positions and build the sparse point
cloud.

#### Step 9 — Run Alignment 

![Aligned photos](HiRes_Processing_Pipeline_media/8_align_photos.png)


#### Step 10 — Load a marker

![Filter photos by marker](HiRes_Processing_Pipeline_media/9_filtrer%20photos%20by%20marker.png)



Select a marker (GCP) to begin refining its position across the images. Select filter photos by marker to see which images contain the marker.  

#### Step 11 — Inspect the distance from the aeropoint to the centre of the GCP
![Load marker](HiRes_Processing_Pipeline_media/8_marker_load.png)


#### Step 12 — Move the marker

![Marker moved](HiRes_Processing_Pipeline_media/10_marker_moved.png)

Drag the marker to its precise location on the ground control target in the
image.

#### Step 13 — Repeat across images and markers

![Marker again](HiRes_Processing_Pipeline_media/11_marker_again.png)

Repeat the marker placement on the remaining images so each GCP is accurately
pinned across all views. Note that you should do ~ 5 images fro a GCP/Marker. Essentially repeat the process until the point is consistently falling in the middle of the GCP for a given marker. 

#### Step 14 — Optimise cameras

![Optimise cameras](HiRes_Processing_Pipeline_media/12_optmise_cameras.png)

Run **Optimise Cameras** 

#### Step 15 — Build point cloud

![Build point cloud](HiRes_Processing_Pipeline_media/13_build_pointcloud.png)

Start **Build Point Cloud** to generate the dense point cloud from the aligned
imagery.

#### Step 16 — Point cloud settings

![Build point cloud settings](HiRes_Processing_Pipeline_media/14_build_pointcloud_2.png)

Set the quality and depth-filtering options, then run the dense point cloud
build.

#### Step 17 — Build DEM

![Build DEM](HiRes_Processing_Pipeline_media/15_build_dem.png)

Start **Build DEM** to generate the digital elevation model from the point
cloud.

#### Step 18 — DEM settings

![Build DEM settings](HiRes_Processing_Pipeline_media/16_build_dem2.png)

Confirm the source data, projection, and resolution, then run the DEM build.

#### Step 19 — Build orthomosaic

![Build orthomosaic](HiRes_Processing_Pipeline_media/17_buiild_ortho.png)

Start **Build Orthomosaic** to generate the orthorectified mosaic from the
imagery and DEM.

#### Step 20 — Orthomosaic settings

![Build orthomosaic settings](HiRes_Processing_Pipeline_media/18_build_ortho2.png)

Set the surface (DEM), blending mode, and resolution, then run the
orthomosaic build.

#### Step 21 — View the orthomosaic

![View orthomosaic](HiRes_Processing_Pipeline_media/19_view_ortho.png)

Inspect the finished orthomosaic for coverage, colour balance, and any
mosaicing artefacts.

#### Step 22 — Export the orthomosaic

![Export orthomosaic](HiRes_Processing_Pipeline_media/20_export_ortho.png)

Export the orthomosaic as a GeoTIFF, confirming the CRS, resolution, and
output path.

---

### Method 2 - Image tiling method (in development)

> [!IMPORTANT]
> The two methods have were developed **independently by UWA/DPRID and UQ** and are
> based on the PhaseOne iX Capture / Image SDK toolchain. Ongoing work this
> season is focused on **combining them into a single, unified approach**,
> which will be documented in future revisions of this protocol. Both are
> intended to produce the standard, radiometrically and geometrically rigorous
> APPN tiled image products. 

