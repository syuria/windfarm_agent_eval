import pandas as pd

from windwatch.reporting import build_summary


def test_build_summary_returns_basic_counts():
    df = pd.DataFrame({
        "turbine_id": ["T1", "T1", "T2"],
        "is_anomaly": [True, False, True],
        "risk_score": [0.8, 0.2, 0.9],
    })
    summary = build_summary(df)
    assert summary["total_readings"] == 3
    assert summary["anomaly_count"] == 2
    assert summary["turbines"]["T1"]["readings"] == 2
