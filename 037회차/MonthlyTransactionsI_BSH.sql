SELECT
    DATE_FORMAT(trans_date, '%Y-%m') as month,
    country,
    COUNT(*) AS trans_count,
    COUNT(IF(state='approved',1,NULL)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state='approved',amount,NULL)) AS approved_total_amount
FROM
    Transactions
GROUP BY
    month, country;
