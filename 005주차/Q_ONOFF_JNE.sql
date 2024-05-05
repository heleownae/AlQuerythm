SELECT date_format(SALES_DATE, '%Y-%m-%d') SALES_DATE,
       PRODUCT_ID,
       USER_ID,
       SALES_AMOUNT
from ONLINE_SALE
where date_format(SALES_DATE, '%Y-%m') = '2022-03'
union all
select date_format(SALES_DATE, '%Y-%m-%d') SALES_DATE,
       PRODUCT_ID,
       if(OFFLINE_SALE_ID is not null, null, OFFLINE_SALE_ID) USER_ID,
       SALES_AMOUNT
from OFFLINE_SALE
where date_format(SALES_DATE, '%Y-%m') = '2022-03'
order by 1, 2, 3