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

## Related

- [CALViS Fieldbook](CALViS-Fieldbook)
- [GOBI Fieldbook](GOBI-Fieldbook)
- [QA Process](QA-Process)
