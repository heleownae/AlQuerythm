SELECT DATE(order_purchase_timestamp) as purchase_date,
      SUM(CASE WHEN order_delivered_customer_date <= order_estimated_delivery_date THEN 1 ELSE 0 END) as success,
      SUM(CASE WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1 ELSE 0 END) as fail
FROM olist_orders_dataset
where date(order_purchase_timestamp) between '2017-01-01' and '2017-01-31'
GROUP BY 1;
