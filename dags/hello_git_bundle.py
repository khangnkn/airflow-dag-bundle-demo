"""DAG loaded by GitDagBundle from this repository."""

from datetime import datetime

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

with DAG(
    dag_id="hello_git_bundle",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example", "git-bundle"],
) as dag:
    BashOperator(
        task_id="say_hello",
        bash_command="echo hello from GitHub GitDagBundle",
    )
