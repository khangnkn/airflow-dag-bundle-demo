"""Schedule a one-executor Spark Pi job on this Kubernetes cluster."""

from datetime import datetime

from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import (
    SparkKubernetesOperator,
)
from airflow.sdk import DAG

SPARK_PI = {
    "apiVersion": "sparkoperator.k8s.io/v1beta2",
    "kind": "SparkApplication",
    "spec": {
        "type": "Python",
        "mode": "cluster",
        "image": "apache/spark:3.5.9-python3",
        "imagePullPolicy": "IfNotPresent",
        "mainApplicationFile": "local:///opt/spark/examples/src/main/python/pi.py",
        "sparkVersion": "3.5.9",
        "restartPolicy": {"type": "Never"},
        "driver": {
            "cores": 1,
            "memory": "512m",
            "serviceAccount": "spark-operator-spark",
        },
        "executor": {
            "cores": 1,
            "instances": 1,
            "memory": "512m",
        },
    },
}

with DAG(
    dag_id="spark_pi",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example", "spark"],
) as dag:
    SparkKubernetesOperator(
        task_id="spark_pi",
        namespace="spark",
        image="apache/spark:3.5.9-python3",
        code_path="local:///opt/spark/examples/src/main/python/pi.py",
        template_spec=SPARK_PI,
        startup_timeout_seconds=900,
        delete_on_termination=True,
    )
