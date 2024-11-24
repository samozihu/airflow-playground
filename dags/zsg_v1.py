
from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG

from airflow.operators.bash import BashOperator

with DAG(
    "zsg_v1",
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple DAG",
    start_date=datetime(2021, 1, 1),
    schedule_interval=timedelta(minutes=1),
    catchup=False,
    tags=["zsg_test"],
) as dag:
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )

    t1.doc_md = dedent(
        """\
        lsliseise
        """
    )
    dag.doc_md = __doc__
    dag.doc_md = dedent(
        """\
        This is a documentation placed anywhere
        """
    )

    template_command = dedent(
        """
        {% for i in range(5) %}
            echo "{{ ds }}"
            echo "{{ macros.ds_add(ds, 7) }}"
        {% endfor %}
        """
    )

    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command=template_command,
    )

    t1 >> [t2, t3]
