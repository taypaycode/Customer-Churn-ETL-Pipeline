# Customer-Churn-ETL-Pipeline

## Overview
This project demonstrates an end-to-end ETL pipeline for a customer churn dataset. The pipeline extracts raw customer data from CSV files, transforms it by calculating churn probabilities, and loads it into a Google BigQuery data warehouse.

## Tools Used:
- Python for ETL pipeline development
- Google BigQuery for data warehousing
- Apache Airflow for automation and orchestration

## Setup Instructions
1. Clone the repository.
2. Install required dependencies: `pip install -r requirements.txt`
3. Set up Airflow with Docker: `docker-compose up`
4. Add your Google Cloud credentials for BigQuery access.
5. Run the Airflow DAG to start the ETL pipeline.

## Pipeline Diagram
[Add your pipeline architecture diagram here]

## Future Work
- Implement real-time data streaming.
- Add support for additional data sources (e.g., APIs).
