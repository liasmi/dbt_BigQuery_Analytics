from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define your paths (use the WSL paths)
DBT_PROJECT_DIR = "/mnt/c/Users/pc/Documents/Trainings/dbt/dbt_BigQuery_Analytics/dbt_shop"
DBT_PROFILES_DIR = "/mnt/c/Users/pc/.dbt"

with DAG(
    "ismail_shop_transformation",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["dbt", "finance", "ismail_shop"]
) as dag:

    # Task 1: Run Staging Models
    run_stg_customer = BashOperator(
        task_id="dbt_run_staging_customer",
        bash_command=f"dbt run --select tag:staging_customer --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}"
    )

        # Task 1: Run Staging Models
    run_stg_order = BashOperator(
        task_id="dbt_run_staging_order",
        bash_command=f"dbt run --select tag:staging_order  --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}"
        # bash_command=f"dbt build --select tag:staging_orders --vars '{{\"start_date\": \"{{ ds }}\"}}' --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}"
    )

    # Task 2: Build Marts
    build_marts = BashOperator(
        task_id="dbt_build_marts",
        bash_command=f"dbt build --select tag:finance --project-dir {DBT_PROJECT_DIR} --profiles-dir {DBT_PROFILES_DIR}"
    )

    run_stg_customer >> run_stg_order >> build_marts