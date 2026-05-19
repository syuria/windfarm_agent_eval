from __future__ import annotations

import json
from pathlib import Path
import pandas as pd


def build_summary(df: pd.DataFrame) -> dict:
    """Build a small JSON-serialisable summary."""
    total = len(df)
    anomalies = int(df["is_anomaly"].sum()) if "is_anomaly" in df else 0

    by_turbine = {}
    for turbine_id, group in df.groupby("turbine_id"):
        by_turbine[str(turbine_id)] = {
            "readings": int(len(group)),
            "anomalies": int(group.get("is_anomaly", pd.Series(dtype=bool)).sum()),
            "max_risk_score": float(group.get("risk_score", pd.Series([0])).max()),
        }

    return {
        "total_readings": total,
        "anomaly_count": anomalies,
        "anomaly_rate": anomalies / total if total else 0,
        "turbines": by_turbine,
    }


def write_summary(summary: dict, output_path: str | Path) -> None:
    """Write a summary JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
