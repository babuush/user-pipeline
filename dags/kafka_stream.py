from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

defualt_args ={
    'owner': 'babuush',
    'start_date': datetime(2023, 9, 3, 10, 00)
}

def stream_data():
    import json
    import requests

    res = requests.get("https://randomuser.me/api/")

with DAG('user_automation', 
         default_args=defualt_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )