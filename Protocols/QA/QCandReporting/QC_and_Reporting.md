# Quality Control and Reporting

This page outlines the **quality control (QC) checks** applied to standard
APPN UAV data products, and provides guidance on how users can **assess,
interpret, and report data quality** in downstream analysis and publications.

The intent is to support transparency, informed use, and consistent reporting,
rather than to present data products as error-free or universally applicable.

For the operator-facing spectral and QGIS QC workflow used during routine data
preparation, see [Aerial Data QC](../QAprocess/AerialDataQC.md).

---

## Scope and intent

- QC information is provided to help users understand the strengths and
  limitations of standard APPN UAV data products.
- QC checks are primarily focused on **data completeness, internal
  consistency, and gross errors**.
- Fitness for purpose ultimately depends on the scientific question,
  experimental design, and environmental conditions at the time of data
  capture.

---

## Quality control during acquisition

Standard APPN operations follow documented platform-specific SOPs (e.g. CALViS
and GOBI Fieldbooks) designed to minimise avoidable sources of error during
data capture.

Typical acquisition-level QC elements include:

- Verification of GNSS-INS operation and stability prior to and during flight
- Use of calibrated reflectance panels for hyperspectral data
- Oversampling and overlap constraints to reduce interpolation artefacts
- Monitoring of sensor health, logging continuity, and environmental
  conditions
- Immediate post-flight confirmation that expected raw data files were
  recorded

These checks aim to ensure that data are suitable for downstream processing,
but do not guarantee that all data will be optimal for every analysis.

---

## Quality control during processing

Standard processing pipelines apply a series of automated and semi-automated
checks as part of routine product generation.

Typical processing-stage QC includes:

- Removal of extreme outliers in LiDAR point clouds
- Consistency checks between LiDAR-derived surfaces and optical products
- Verification of expected spatial resolution and spatial extent
- Radiometric scaling and metadata checks for hyperspectral products
- Detection of missing or incomplete output products

Processing logs and configuration files provide traceability of the parameters
used to generate each output.

---

## What users should check

Users are encouraged to perform basic QC checks before analysis, including:

- Confirming spatial coverage and alignment of products (e.g. DSM,
  orthomosaics)
- Inspecting for obvious artefacts (striping, seams, missing lines)
- Reviewing metadata for spatial resolution, coordinate reference system, and
  processing version
- Assessing whether environmental conditions (wind, cloud, sun angle) may have
  influenced data quality

For hyperspectral data, users should also consider signal-to-noise
characteristics and band-specific artefacts relevant to their application.

---

## Quality metrics and error reporting

Not all standard data products are delivered with formal error estimates or
uncertainty surfaces at this stage but will in the future.

Where available, supplementary information may include:

- Nominal spatial resolution and point density
- Acquisition geometry (altitude, overlap, flight direction)
- Basic completeness indicators (e.g. missing data flags)

Users requiring formal error propagation or uncertainty quantification should
treat standard products as inputs to further analysis rather than final
error-bounded measurements.

---

## Reporting and citation guidance

When publishing or reporting results derived from APPN UAV data, users are
encouraged to:

- Clearly state the platform and standard pipeline used (e.g. CALViS standard
  pipeline)
- Report nominal spatial resolution rather than implying pixel-scale accuracy
- Describe any additional processing, filtering, or corrections applied by the
  user
- Note known limitations or deviations from standard operating procedures

Where possible, reference the relevant APPN documentation or pipeline version
to support reproducibility.

---

## Deviations and non-standard workflows

Any deviation from standard acquisition or processing workflows may affect
data quality and comparability.

Users should:

- Document deviations clearly in project records and publications
- Avoid direct comparison with standard datasets without appropriate caveats
- Consult APPN staff if uncertainty exists around data interpretation
