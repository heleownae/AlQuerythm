SELECT DATE(order_purchase_timestamp) AS purchase_date,
       COUNT(CASE WHEN (order_estimated_delivery_date >= order_delivered_customer_date) THEN 1 END) AS 'success',
       COUNT(CASE WHEN (order_estimated_delivery_date < order_delivered_customer_date) THEN 1 END) AS 'fail'
FROM olist_orders_dataset
WHERE DATE(order_purchase_timestamp) BETWEEN '2017-01-01' AND '2017-01-31'
AND order_status = 'delivered'
GROUP BY purchase_date
ORDER BY purchase_date
