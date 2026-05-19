from __future__ import annotations

import pandas as pd


def add_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add simple derived features used by the detector."""
    result = df.copy()

    # Inconsistent naming: some downstream code expects asset_id.
    if "asset_id" not in result.columns and "turbine_id" in result.columns:
        result["asset_id"] = result["turbine_id"]

    result["temp_delta_c"] = result["generator_temp_c"] - result["gearbox_temp_c"]
    result["power_per_wind"] = result["power_kw"] / result["wind_speed"].replace(0, 1)
    return result


def add_rolling_features(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    """Add rolling features per turbine.

    TODO: use time-based windows instead of row counts.
    """
    result = df.sort_values(["turbine_id", "timestamp"]).copy()
    group = result.groupby("turbine_id", sort=False)
    result["vibration_roll_mean"] = group["vibration_mm_s"].transform(lambda s: s.rolling(window).mean())
    result["gearbox_temp_roll_max"] = group["gearbox_temp_c"].transform(lambda s: s.rolling(window).max())
    return result
