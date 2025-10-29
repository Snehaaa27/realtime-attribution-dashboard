import pandas as pd
from datetime import datetime

def process_ga4_events(input_path: str, cleaned_output: str, metrics_output: str):
    """
    Process GA4 event data:
    - Cleans invalid/missing rows
    - Extracts useful time columns
    - Aggregates daily metrics
    """

    print("Loading data...")
    df = pd.read_csv(input_path)

    #Step 1: Clean Data
    print("Cleaning data...")
    df = df.dropna(subset=["event_name", "user_id", "event_timestamp"])  # remove missing
    df["timestamp"] = pd.to_datetime(df["event_timestamp"], errors="coerce")
    df = df.dropna(subset=["event_timestamp"])  # drop invalid timestamps

    #Step 2: Derived Columns
    print("Creating derived columns...")
    df["event_timestamp"] = pd.to_datetime(df["event_timestamp"], errors="coerce")
    df["date"] = df["event_timestamp"].dt.date
    df["hour"] = df["event_timestamp"].dt.hour
    df["session_id"] = df["user_id"].astype(str) + "_" + df["date"].astype(str)

    #Step 3: Aggregated Metrics
    print("Calculating daily metrics...")
    daily_metrics = (
        df.groupby("date")
        .agg(
            total_events=("event_name", "count"),
            unique_users=("user_id", "nunique"),
        )
        .reset_index()
    )
    print(df.columns)
    events_by_source = (
        df.groupby(["date", "source"])
        .size()
        .reset_index(name="event_count")
    )

    # --- Step 4: Save Results ---
    print("Saving cleaned and aggregated data...")
    df.to_csv(cleaned_output, index=False)
    daily_metrics.to_csv(metrics_output, index=False)

    print("Data processing complete!")
    print(f"Cleaned data saved to: {cleaned_output}")
    print(f"Daily metrics saved to: {metrics_output}")


if __name__ == "__main__":
    input_csv = "dbt_project/sample_data/ga4_events.csv"
    cleaned_csv = "output/cleaned_events.csv"
    metrics_csv = "output/daily_metrics.csv"

    process_ga4_events(input_csv, cleaned_csv, metrics_csv)
