from google.cloud import bigquery
import pandas as pd

def load_data_to_bigquery(df, table_id):
    # Initialize BigQuery Client
    client = bigquery.client()

    # Load Dataframe to BigQuery
    job = client.load_table_from_dataframe(df, table_id)

    job.result() # Wait for the Job to complete
    print(f"Loaded {df.shape[0]} rows to {table_id}")

if __name__ == "__main__":
    # Example Google BigQuery table ID
    table_id = "Your_project.your_dataset.customer_churn"

    # Load the Transformed data
    df = pd.read_csv()
    load_data_to_bigquery(df, table_id)
