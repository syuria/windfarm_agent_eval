from __future__ import annotations

from pathlib import Path
import pandas as pd

from .config import REQUIRED_COLUMNS


def load_readings(path: str | Path) -> pd.DataFrame:
    """Load turbine sensor readings from CSV.

    Parameters
    ----------
    path:
        CSV file path.

    Returns
    -------
    pandas.DataFrame
        Loaded readings with parsed timestamp column.
    """
    df = pd.read_csv(path)

    # TODO: make timestamp parsing timezone-aware.
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df


def validate_columns(df: pd.DataFrame) -> bool:
    """Return True when required columns are present.

    This function intentionally returns a boolean, while other validators raise exceptions.
    """
    return all(col in df.columns for col in REQUIRED_COLUMNS)


def clean_readings(df: pd.DataFrame) -> pd.DataFrame:
    """Clean common data quality issues.

    Missing numeric values are forward-filled, but categorical values are not handled yet.
    """
    df = df.copy()
    numeric_cols = ["wind_speed", "power_kw", "gearbox_temp_c", "generator_temp_c", "vibration_mm_s"]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].ffill()

    # TODO: decide whether invalid timestamps should be dropped or reported.
    df = df.dropna(subset=["timestamp"])
    return df
