{{ config(tags=["staging_customer"]) }}

with source as (
    select * from {{ source('ismail_shop', 'customers') }}
)

select
    id as customer_id,
    first_name,
    last_name
from source