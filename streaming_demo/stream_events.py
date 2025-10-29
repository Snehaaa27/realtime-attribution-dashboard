# streaming_demo/stream_events.py
from google.cloud import bigquery
import time
import uuid
from datetime import datetime, timedelta

PROJECT = "assessment-476418"
DATASET = "dbt_sneha_staging"   # target staging dataset where dbt source points (adjust if different)
TABLE = "raw_events"       # table name in that dataset

client = bigquery.Client(project=PROJECT)
table_id = f"{PROJECT}.{DATASET}.{TABLE}"

def make_event(user_id, event_name, source, medium, campaign, ts):
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": str(user_id),
        "event_name": event_name,
        "source": source,
        "medium": medium,
        "campaign": campaign,
        "event_timestamp": ts.strftime("%Y-%m-%d %H:%M:%S")
    }

def stream_events(n=10, delay_seconds=1):
    now = datetime.utcnow()
    rows = []
    for i in range(n):
        # create synthetic events with varying users/sources
        uid = 200 + (i % 5)         # user ids 200..204
        ev = "page_view" if i % 3 != 0 else "purchase"
        src = ["google","facebook","email","direct","linkedin"][i % 5]
        medium = "cpc" if src=="google" else ("paid_social" if src=="facebook" else "organic")
        campaign = "stream_demo"
        ts = now - timedelta(minutes=(n-i))  # different timestamps
        rows.append(make_event(uid, ev, src, medium, campaign, ts))

        # stream in small batches
        if len(rows) >= 5:
            insert(rows)
            rows = []
            time.sleep(delay_seconds)

    if rows:
        insert(rows)

def insert(rows):
    job = client.load_table_from_json(rows, table_id)
    job.result()  # Wait for the job to complete
    print(f"Inserted {len(rows)} rows into {table_id} (via batch load)")


if __name__ == "__main__":
    stream_events(n=10, delay_seconds=1)
