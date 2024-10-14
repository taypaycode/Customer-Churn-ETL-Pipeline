from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.extract_data import extract_data
from src.transform_data import transform_data
from src.load_data import load_data_to_bigquery

def extract():
    extract_data('../data/customer_churn.csv')

def transform():
    transform_data(df)

def load():
    load_data_to_bigquery(df, 'your_project.your_dataset.customer_churn')

with DAG('etl_customer_churn', start_date=datetime(2024, 1, 1), schedule_interval='@daily') as dag:
    extract_task = PythonOperator(task_id='extract', python_callable=extract)
    transform_task = PythonOperator(task_id='transform', python_callable=transform)
    load_task = PythonOperator(task_id='load', python_callable=load)

    extract_task >> transform_task >> load_task
