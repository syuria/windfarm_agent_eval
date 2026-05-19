import pandas as pd

from windwatch.features import add_basic_features, add_rolling_features


def test_add_basic_features_creates_asset_id_and_ratios():
    df = pd.DataFrame({
        "turbine_id": ["T1"],
        "timestamp": [pd.Timestamp("2024-01-01")],
        "wind_speed": [5.0],
        "power_kw": [50.0],
        "gearbox_temp_c": [40.0],
        "generator_temp_c": [50.0],
    })
    result = add_basic_features(df)
    assert result.loc[0, "asset_id"] == "T1"
    assert result.loc[0, "temp_delta_c"] == 10.0
    assert result.loc[0, "power_per_wind"] == 10.0


def test_add_rolling_features_adds_columns():
    df = pd.DataFrame({
        "turbine_id": ["T1", "T1", "T1"],
        "timestamp": pd.date_range("2024-01-01", periods=3, freq="5min"),
        "gearbox_temp_c": [40, 45, 50],
        "vibration_mm_s": [1, 2, 3],
    })
    result = add_rolling_features(df, window=2)
    assert "vibration_roll_mean" in result.columns
    assert result["vibration_roll_mean"].iloc[-1] == 2.5
