-- If this query returns ANY rows, the test fails.
{{ config(
    enabled=false
) }}

select
    customer_id,
    lifetime_value
from {{ ref('dim_customers') }}
where lifetime_value < 0