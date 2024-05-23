SELECT DATE(order_purchase_timestamp) AS purchase_date
     , SUM(CASE WHEN order_estimated_delivery_date >= order_delivered_customer_date THEN 1 ELSE 0 END) AS success
     , SUM(CASE WHEN order_estimated_delivery_date < order_delivered_customer_date THEN 1 ELSE 0 END) AS fail
FROM olist_orders_dataset
WHERE order_purchase_timestamp LIKE '2017-01%'
GROUP BY DATE(order_purchase_timestamp)
ORDER BY DATE(order_purchase_timestamp)
