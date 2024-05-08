SELECT *
FROM ( SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS SALES_DATE,
              product_id,
              user_id,
              sales_amount
       FROM online_sale
       WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-03'
         UNION ALL
       SELECT DATE_FORMAT(sales_date, '%Y-%m-%d') AS SALES_DATE,
              product_id,
              NULL user_id,
              sales_amount
       FROM offline_sale
       WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-03' ) DATE_SET
ORDER BY SALES_DATE, product_id, user_id
