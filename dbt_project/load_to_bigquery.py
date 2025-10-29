from google.cloud import bigquery
import pandas as pd

def load_csv_to_bigquery(csv_path, dataset_id, table_name, project_id):
    client = bigquery.Client(project=project_id)

    # Load the CSV
    df = pd.read_csv(csv_path)

    # Define BigQuery table reference
    table_ref = f"{project_id}.{dataset_id}.{table_name}"

    # Load config
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",  # replace existing
        autodetect=True,
    )

    # Load the data
    print(f"Uploading {csv_path} to {table_ref}...")
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()  # Wait for completion
    print("Upload complete!")

if __name__ == "__main__":
    project_id = "assessment-476418"
    dataset_id = "dbt_sneha"
    table_name = "stg_ga4_events"
    csv_path = "output/cleaned_events.csv"

    load_csv_to_bigquery(csv_path, dataset_id, table_name, project_id)
