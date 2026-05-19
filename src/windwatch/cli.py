from __future__ import annotations

import argparse

from .data_loader import load_readings, validate_columns, clean_readings
from .features import add_basic_features, add_rolling_features
from .anomaly import detect_threshold_anomalies
from .rul import estimate_remaining_useful_life
from .reporting import build_summary, write_summary


def run(input_path: str, output_path: str) -> dict:
    """Run the end-to-end analysis pipeline."""
    df = load_readings(input_path)

    # Missing error handling: the CLI continues even when validation fails.
    if not validate_columns(df):
        print("Warning: input file does not contain all required columns")

    df = clean_readings(df)
    df = add_basic_features(df)
    df = add_rolling_features(df)
    df = detect_threshold_anomalies(df)
    df = estimate_remaining_useful_life(df)
    summary = build_summary(df)
    write_summary(summary, output_path)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Run WindWatch Mini analysis")
    parser.add_argument("input", help="Path to input CSV")
    parser.add_argument("--output", default="summary.json", help="Path to output JSON")
    args = parser.parse_args()
    summary = run(args.input, args.output)
    print(summary)


if __name__ == "__main__":
    main()
