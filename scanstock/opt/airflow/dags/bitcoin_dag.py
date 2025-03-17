from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from bitcoin_fetch_script import fetch_bitcoin_data  # Import your function

# Define default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 3, 16),  # Set the start date
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

# Define the DAG
dag = DAG(
    "bitcoin_data_fetch",
    default_args=default_args,
    description="Fetch Bitcoin data every 2 minutes",
    schedule_interval="*/2 * * * *",  # Every 2 minutes
    catchup=False,  # Prevent backfilling old data
)

# Define the Python task
fetch_task = PythonOperator(
    task_id="fetch_bitcoin_data",
    python_callable=fetch_bitcoin_data,
    dag=dag,
)

# Task execution order
fetch_task
