# Data Folder Structure

APPN aerial data follows a standard folder layout so raw, processed, and
metadata artefacts are consistent across nodes, sites, sensors, and runs.

## Reference

Full specification:
[APPN_GenricFileStorage wiki](https://github.com/ArdenB/APPN_GenricFileStorage/wiki).

## Standard path

```
./{NodeName}/{Project}/{Site}/{Sensor}/
  {YYYYMMDD}/Run_{XX}/T0_raw
```

## Per-run / per-day artefacts

All paths below are relative to the per-day folder:

```
./{NodeName}/{Project}/{Site}/{Sensor}/{YYYYMMDD}/
```

| Artefact         | Suffix under day folder        | Notes                                           |
| ---------------- | ------------------------------ | ----------------------------------------------- |
| Raw capture data | `Run_{XX}/T0_raw`              | Hyperspec cubes, LiDAR, GNSS-INS, `.graw`       |
| GCP data         | `Run_{XX}/T0_raw/Vault`        | Location may change; see fieldbook              |
| Field notes      | `FieldNotes.txt`               | Per-day, free-text issues log                   |
| Run overview     | `RunOverview.csv`              | Per-run metadata (APEx conditions, `RunFailed`) |
| Processed data   | `Run_{XX}/T1_proc`             | `.gpro` from APPN GPT pipeline                  |

> [!IMPORTANT]
> When data from a failed run is being kept (e.g. for debugging with GRYFN),
> set the `RunFailed` boolean column of `RunOverview.csv` to `True`.

## Site-level documentation

Site-wide reference data (plot layouts, trial information, etc.) lives
in a sibling `Documentation/` folder at the **site** level — alongside
each sensor's data, not inside any sensor or per-day folder:

```
./{NodeName}/{Project}/{Site}/
  Documentation/
    Plot_Layout/
    Trial_Info/
  {Sensor}/
    {YYYYMMDD}/Run_{XX}/T0_raw
```

### `Documentation/Plot_Layout/`

Holds the **plot polygon vector files** that every sensor's processing
pipeline keys off. Three families of file are recognised — see the
[Plot Delineation protocol](../../PlotProtocols/PlotDelineation/Plot_Delineation.md#file-naming-convention)
for the full specification.

| Artefact | Filename pattern | Notes |
| --- | --- | --- |
| **Main plot file** *(mandatory)* | `{YYYYSiteName}_plots.geojson` | The single required file. Entry point for every downstream pipeline. |
| Plot variants *(optional)* | `{YYYYSiteName}_plots_{descriptor|sensor}[_v{NN}].geojson` | e.g. `_unbuffered`, `_rszone`, or sensor-specific (`_HIRES`) when justified. |
| Sampling files *(optional)* | `{YYYYSiteName}_sampling_{measurement}_{YYYYMMDD}[_v{NN}].geojson` | One per measurement type (`biomass`, `height`, `emergence`, `headcount`, …). |
| Permanent GCPs *(optional)* | `{YYYYSiteName}_gcp[_v{NN}].geojson` | Permanent surveyed markers only — temporary per-flight GCPs stay with the flight (`Run_{XX}/T0_raw/Vault`). |
| Tool config sidecar | `{YYYYSiteName}_plots_v{NN}.json` | e.g. FIELDimageR settings — saved alongside the plot file for reproducibility. |
| Deprecated copies | `…_deprecated.geojson` | Superseded files retained for provenance (terminal `_deprecated` tag). |
| Folder README *(strongly recommended)* | `README.md` | Site-specific context: current main file, variants in use, deprecation log, known quirks. |

> [!IMPORTANT]
> `{YYYYSiteName}_plots.geojson` is the **only mandatory vector file**
> and must exist for every APPN project and site. All other files in
> the folder are optional.

### `Documentation/Trial_Info/`

Holds the **trial-information spreadsheet(s)** that join to the plot
file via `plot_id`. APPN mandates only the `plot_id` column — every
other column is trial-specific. See
[Joining Trial Information](../../PlotProtocols/PlotDelineation/Plot_Delineation.md#joining-trial-information).

| Artefact | Filename pattern | Notes |
| --- | --- | --- |
| Trial info (current) | `{YYYYSiteName}_trial_info.csv` | CSV preferred; XLSX accepted. Must include a `plot_id` column matching the plot file. |
| Deprecated copies | `{YYYYSiteName}_trial_info_{YYYYMMDD}_deprecated.csv` | Same `_deprecated` / `_v{NN}` conventions as plot files. |
| Folder README *(strongly recommended)* | `README.md` | Source spreadsheets, contacts, column definitions, quirks. |

### Example (full site)

```
USYD_Narrabri/2025_SIFOzBarley/2025IAWatson_F/
  Documentation/
    Plot_Layout/
      2025IAWatson_plots.geojson
      2025IAWatson_plots_unbuffered_v01.geojson
      2025IAWatson_plots_HIRES_v01.geojson
      2025IAWatson_sampling_biomass_20251104_v01.geojson
      2025IAWatson_gcp_v01.geojson
      README.md
    Trial_Info/
      2025IAWatson_trial_info.csv
      README.md
  CALVIS/20251104/Run_01/T0_raw/...
  HIRES/20251104/Run_01/T0_raw/...
```

## Related

- [CALViS Fieldbook](CALViS-Fieldbook)
- [GOBI M350 Fieldbook](GOBI-M350-Fieldbook)
- [GOBI IF1200 Fieldbook](GOBI-IF1200-Fieldbook)
- [QA Process](QA-Process)
