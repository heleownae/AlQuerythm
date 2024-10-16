With first AS(
SELECT customer_id,
       MIN(order_date) first_order
FROM Delivery
GROUP BY customer_id
),
immediate AS(
SELECT d.customer_id
FROM Delivery d JOIN first f ON d.customer_id = f.customer_id 
                             AND f.first_order = d.order_date
WHERE d.customer_pref_delivery_date = d.order_date
) 

SELECT ROUND((count(*) * 100 / (SELECT distinct count(*) FROM first)), 2) immediate_percentage
FROM immediate
