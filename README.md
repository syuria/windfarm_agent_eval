# WindWatch Mini

WindWatch Mini is a small Python project for experimenting with wind-turbine sensor analytics.
It loads SCADA-like CSV data, calculates simple health features, detects anomalies, and produces
basic turbine risk summaries.

This repository is intentionally incomplete and slightly inconsistent. It is designed as a small
codebase for coding-agent evaluation tasks.

## Features

- Load turbine sensor readings from CSV files
- Clean and validate required columns
- Compute rolling temperature and vibration indicators
- Detect possible anomalies using a simple threshold-based approach
- Produce a component-level risk score
- Export summary output as JSON

## Example

```bash
python -m windwatch.cli data/sample_readings.csv --output summary.json
```

## Expected columns

The loader currently expects:

- `timestamp`
- `turbine_id`
- `wind_speed`
- `power_kw`
- `gearbox_temp_c`
- `generator_temp_c`
- `vibration_mm_s`
- `status`

Some modules refer to `asset_id` instead of `turbine_id`. This should be standardised later.

## Known gaps

- TODO: improve validation and error messages
- TODO: add proper probabilistic Remaining Useful Life model
- TODO: improve handling of missing timestamps
- TODO: support multiple input files
- TODO: add configuration file for thresholds
