from airflow import DAG
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

from datetime import datetime

with DAG(
    dag_id="dag1",
    description="dag1",
    start_date=datetime(2023,3, 1),
    schedule_interval="@once",
) as dag1:
    t1 = EmptyOperator(task_id="dummy")


