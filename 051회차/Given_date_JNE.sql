WITH sub AS (
    SELECT product_id,
           new_price,
           change_date,
           RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rank_date 
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT p.product_id,
       IFNULL(MAX(s.new_price), 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN sub s ON p.product_id = s.product_id AND s.rank_date = 1
GROUP BY p.product_id;
