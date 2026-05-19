from __future__ import annotations

import pandas as pd

from .config import DEFAULT_THRESHOLDS


def detect_threshold_anomalies(df: pd.DataFrame, thresholds: dict | None = None) -> pd.DataFrame:
    """Flag simple threshold anomalies.

    This is intentionally simple and not yet a production model.
    """
    thresholds = thresholds or DEFAULT_THRESHOLDS
    result = df.copy()

    result["high_gearbox_temp"] = result["gearbox_temp_c"] > thresholds["gearbox_temp_c"]
    result["high_generator_temp"] = result["generator_temp_c"] > thresholds["generator_temp_c"]
    result["high_vibration"] = result["vibration_mm_s"] > thresholds["vibration_mm_s"]

    # TODO: power ratio threshold should depend on wind speed regime.
    result["low_power_ratio"] = result.get("power_per_wind", 0) < thresholds["power_ratio_low"]

    result["is_anomaly"] = (
        result["high_gearbox_temp"]
        | result["high_generator_temp"]
        | result["high_vibration"]
        | result["low_power_ratio"]
    )
    return result


def anomaly_counts_by_asset(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise anomaly counts by asset.

    Note: this function expects asset_id, but CLI mostly uses turbine_id.
    """
    return (
        df.groupby("asset_id")["is_anomaly"]
        .sum()
        .reset_index(name="anomaly_count")
        .sort_values("anomaly_count", ascending=False)
    )
