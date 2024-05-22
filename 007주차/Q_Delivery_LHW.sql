-- 배송 예정일 예측 성공과 실패
SELECT strftime('%Y-%m-%d', order_purchase_timestamp) as "purchase_date",
  SUM(CASE WHEN order_estimated_delivery_date >= order_delivered_customer_date THEN 1 ELSE 0 END) as "success",
  SUM(CASE WHEN order_estimated_delivery_date < order_delivered_customer_date THEN 1 ELSE 0 END) as "fail"
FROM olist_orders_dataset
WHERE strftime('%Y-%m-%d', order_purchase_timestamp) LIKE '2017-01%'
GROUP BY 1
ORDER BY 1 asc;
