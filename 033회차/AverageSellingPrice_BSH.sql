SELECT US.product_id, ROUND(
                            SUM(US.units*PR.price) / SUM(US.units)
                            ,2) AS average_price
FROM UnitsSold AS US
LEFT JOIN Prices AS PR ON US.product_id = PR.product_id
AND US.purchase_date BETWEEN PR.start_date AND PR.end_date
GROUP BY US.product_id
