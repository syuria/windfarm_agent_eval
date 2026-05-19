"""Static configuration for turbine analytics.

These values are placeholders and should eventually be loaded from a config file.
"""

DEFAULT_THRESHOLDS = {
    "gearbox_temp_c": 85.0,
    "generator_temp_c": 90.0,
    "vibration_mm_s": 7.5,
    "power_ratio_low": 0.25,
}

REQUIRED_COLUMNS = [
    "timestamp",
    "turbine_id",
    "wind_speed",
    "power_kw",
    "gearbox_temp_c",
    "generator_temp_c",
    "vibration_mm_s",
    "status",
]
