import pandas as pd

from windwatch.data_loader import validate_columns, clean_readings


def test_validate_columns_true_for_required_columns():
    df = pd.DataFrame({
        "timestamp": [],
        "turbine_id": [],
        "wind_speed": [],
        "power_kw": [],
        "gearbox_temp_c": [],
        "generator_temp_c": [],
        "vibration_mm_s": [],
        "status": [],
    })
    assert validate_columns(df) is True


def test_clean_readings_drops_invalid_timestamps():
    df = pd.DataFrame({
        "timestamp": ["2024-01-01 00:00:00", "not-a-date"],
        "wind_speed": [7.0, None],
        "power_kw": [100.0, 110.0],
        "gearbox_temp_c": [60.0, 61.0],
        "generator_temp_c": [65.0, 66.0],
        "vibration_mm_s": [2.0, 2.1],
    })
    cleaned = clean_readings(df)
    assert len(cleaned) == 1
