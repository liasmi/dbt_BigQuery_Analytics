{{ config(tags=["staging_order"]) }}

with source as (
    select * from {{ source('ismail_shop', 'orders') }}
)

select
    id as order_id,
    user_id as customer_id,
    order_date,
    status
from source
-- where order_date >= '{{ var("start_date", "2018-01-01") }}'