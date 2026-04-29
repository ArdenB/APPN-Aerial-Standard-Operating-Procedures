# Processing Pipelines

This page documents the standardised GRYFN processing pipeline YAML files used
within APPN for UAV-based data processing. These YAML configurations define
consistent, transparent, and repeatable processing workflows across
GRYFN-supported sensors and platforms, supporting reproducibility, quality
assurance, and cross-project comparability. The files are intended to be used
as reference and default templates for approved processing pipelines, with any
deviations explicitly documented to maintain traceability and data integrity.

The standard pipelines and the data products they output are detailed below.
For a tabular summary of output formats, resolutions and software
compatibility, see [Standard Data Products](../StandardDataProducts/Standard_Data_Products.md).

---

## 🌿 CALViS — Standard Processing Pipeline

### LiDAR-derived products

#### LiDAR Digital Surface Model (DSM)

- **Output:** `LiDAR_DSM.tif`
- **Type:** Raster
- **Resolution:** 8 cm (fixed resolution)
- **Extent:** VNIR scene extent

#### LiDAR Digital Terrain Model (DTM)

- **Output:** `LiDAR_DTM.tif`
- **Type:** DTM
- **Resolution:** 100 cm (1 m)
- **Extent:** Processing extent

#### Combined LiDAR Point Cloud

- **Output:** `LiDAR_CombinedPointCloud.las`
- **Type:** Combined point cloud
- **Notes:** Outliers removed during combination

### Hyperspectral products

#### VNIR Orthomosaic

- **Output:** `VNIR_Orthomosaic.bin`
- **Type:** Orthomosaic (ENVI format, radiance-scaled)
- **Resolution:** 4 cm (GSD-based)
- **Notes:** binning = 2, radiometric calibration applied

#### SWIR Orthomosaic

- **Output:** `SWIR_Orthomosaic.bin`
- **Type:** Orthomosaic (ENVI format, radiance-scaled)
- **Resolution:** 4 cm (GSD-based)
- **Notes:** binning = 2, radiometric calibration applied

---

## 🌱 GOBI — Standard Processing Pipeline

### LiDAR-derived products

#### LiDAR Digital Surface Model (DSM)

- **Output:** `LiDAR_DSM.tif`
- **Type:** Raster
- **Resolution:** 8 cm (fixed resolution)
- **Extent:** VNIR scene extent

#### LiDAR Digital Terrain Model (DTM)

- **Output:** `LiDAR_DTM.tif`
- **Type:** DTM
- **Resolution:** 100 cm (1 m)
- **Extent:** Processing extent

#### Combined LiDAR Point Cloud

- **Output:** `LiDAR_CombinedPointCloud.las`
- **Type:** Combined point cloud
- **Notes:** Outliers removed during combination

### RGB & hyperspectral products

#### VNIR Orthomosaic

- **Output:** `VNIR_Orthomosaic.bin`
- **Type:** Orthomosaic (ENVI format, radiance-scaled)
- **Resolution:** 4 cm (GSD-based)
- **Notes:** binning = 2, radiometric calibration applied

#### RGB Orthomosaic

- **Output:** `RGB_Orthomosaic.tif`
- **Type:** Orthomosaic
- **Resolution:** 0.6 cm (fixed resolution)
- **Notes:** Feature-matching (SIFT) bundle adjustment applied
