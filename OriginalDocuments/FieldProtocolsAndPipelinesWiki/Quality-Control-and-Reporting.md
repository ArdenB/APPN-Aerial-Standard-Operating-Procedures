<p>
This page outlines the <strong>quality control (QC) checks</strong> applied to standard APPN UAV data products, and provides guidance on how users can <strong>assess, interpret, and report data quality</strong> in downstream analysis and publications.
</p>

<p>
The intent is to support transparency, informed use, and consistent reporting, rather than to present data products as error‑free or universally applicable.
</p>

<hr>

<details>
  <summary><strong>Scope and intent</strong></summary>

- QC information is provided to help users understand the strengths and limitations of standard APPN UAV data products.
- QC checks are primarily focused on <strong>data completeness, internal consistency, and gross errors</strong>.
- Fitness for purpose ultimately depends on the scientific question, experimental design, and environmental conditions at the time of data capture.

</details>

<hr>

<details>
  <summary><strong>Quality control during acquisition</strong></summary>

<p>
Standard APPN operations follow documented platform‑specific SOPs (e.g. CALViS and GOBI FieldBooks) designed to minimise avoidable sources of error during data capture.
</p>

Typical acquisition‑level QC elements include:

- Verification of GNSS‑INS operation and stability prior to and during flight
- Use of calibrated reflectance panels for hyperspectral data
- Oversampling and overlap constraints to reduce interpolation artefacts
- Monitoring of sensor health, logging continuity, and environmental conditions
- Immediate post‑flight confirmation that expected raw data files were recorded

<p>
These checks aim to ensure that data are suitable for downstream processing, but do not guarantee that all data will be optimal for every analysis.
</p>

</details>

<hr>

<details>
  <summary><strong>Quality control during processing</strong></summary>

<p>
Standard processing pipelines apply a series of automated and semi‑automated checks as part of routine product generation.
</p>

Typical processing‑stage QC includes:

<ul>
<li>Removal of extreme outliers in LiDAR point clouds</li>
<li>Consistency checks between LiDAR‑derived surfaces and optical products</li>
<li>Verification of expected spatial resolution and spatial extent</li>
<li>Radiometric scaling and metadata checks for hyperspectral products</li>
<li>Detection of missing or incomplete output products</li>
</ul>

<p>
Processing logs and configuration files provide traceability of the parameters used to generate each output.
</p>

</details>

<hr>

<details>
  <summary><strong>What users should check</strong></summary>

<p>
Users are encouraged to perform basic QC checks before analysis, including:
</p>

<ul>
<li>Confirming spatial coverage and alignment of products (e.g. DSM, orthomosaics)</li>
<li>Inspecting for obvious artefacts (striping, seams, missing lines)</li>
<li>Reviewing metadata for spatial resolution, coordinate reference system, and processing version</li>
<li>Assessing whether environmental conditions (wind, cloud, sun angle) may have influenced data quality</li>
</ul>

<p>
For hyperspectral data, users should also consider signal‑to‑noise characteristics and band‑specific artefacts relevant to their application.
</p>

</details>

<hr>

<details>
  <summary><strong>Quality metrics and error reporting</strong></summary>

<p>
Not all standard data products are delivered with formal error estimates or uncertainty surfaces at this stage but will in the future.
</p>

Where available, supplementary information may include:

- Nominal spatial resolution and point density
- Acquisition geometry (altitude, overlap, flight direction)
- Basic completeness indicators (e.g. missing data flags)

<p>
Users requiring formal error propagation or uncertainty quantification should treat standard products as inputs to further analysis rather than final error‑bounded measurements.
</p>

</details>

<hr>

<details>
  <summary><strong>Reporting and citation guidance</strong></summary>

<p>
When publishing or reporting results derived from APPN UAV data, users are encouraged to:
</p>

<ul>
<li>Clearly state the platform and standard pipeline used (e.g. CALViS standard pipeline)</li>
<li>Report nominal spatial resolution rather than implying pixel‑scale accuracy</li>
<li>Describe any additional processing, filtering, or corrections applied by the user</li>
<li>Note known limitations or deviations from standard operating procedures</li>
</ul>

<p>
Where possible, reference the relevant APPN documentation or pipeline version to support reproducibility.
</p>

</details>

<hr>

<details>
  <summary><strong>Deviations and non-standard workflows</strong></summary>

<p>
Any deviation from standard acquisition or processing workflows may affect data quality and comparability.
</p>

<p>
Users should:
</p>

<ul>
<li>Document deviations clearly in project records and publications</li>
<li>Avoid direct comparison with standard datasets without appropriate caveats</li>
<li>Consult APPN staff if uncertainty exists around data interpretation</li>
</ul>

</details>
