select date(order_purchase_timestamp) purchase_date, 
       sum(case when order_estimated_delivery_date >= order_delivered_customer_date then  1 else 0 end) success,
       sum(case when order_estimated_delivery_date < order_delivered_customer_date then 1 else 0 end) fail

--no such function: if 에러로 안됨 / sum 안에 if 사용 못하는지?
--select date(order_purchase_timestamp) purchase_date, 
--       sum(if(order_estimated_delivery_date >= order_delivered_customer_date, 1, 0)) success,
--       sum(if(order_estimated_delivery_date < order_delivered_customer_date, 1, 0)) fail       

from olist_orders_dataset
where date(order_purchase_timestamp) between '2017-01-01' and '2017-01-31'
group by 1
order by 1
