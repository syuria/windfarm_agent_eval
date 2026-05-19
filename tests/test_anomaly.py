import pandas as pd

from windwatch.anomaly import detect_threshold_anomalies, anomaly_counts_by_asset


def test_detect_threshold_anomalies_flags_high_vibration():
    df = pd.DataFrame({
        "gearbox_temp_c": [50.0],
        "generator_temp_c": [55.0],
        "vibration_mm_s": [9.0],
        "power_per_wind": [1.2],
    })
    result = detect_threshold_anomalies(df)
    assert bool(result.loc[0, "is_anomaly"]) is True


def test_anomaly_counts_by_asset_counts_true_values():
    df = pd.DataFrame({
        "asset_id": ["T1", "T1", "T2"],
        "is_anomaly": [True, False, True],
    })
    result = anomaly_counts_by_asset(df)
    assert result["anomaly_count"].sum() == 2
