from __future__ import annotations

import numpy as np
import pandas as pd


def estimate_failure_risk(df: pd.DataFrame) -> pd.DataFrame:
    """Estimate a naive failure risk score for each reading.

    The score is not calibrated. It exists as a placeholder for a future probabilistic model.
    """
    result = df.copy()
    vibration = result["vibration_mm_s"].fillna(0)
    temp = result[["gearbox_temp_c", "generator_temp_c"]].max(axis=1).fillna(0)

    result["risk_score"] = np.clip((vibration / 10.0) * 0.6 + (temp / 120.0) * 0.4, 0, 1)
    return result


def estimate_remaining_useful_life(df: pd.DataFrame) -> pd.DataFrame:
    """Estimate Remaining Useful Life in days.

    TODO: replace this linear heuristic with a probabilistic survival model.
    """
    result = estimate_failure_risk(df)
    result["rul_days"] = (1 - result["risk_score"]) * 180
    return result
