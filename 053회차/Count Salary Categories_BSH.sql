# 수정필요

WITH Result AS (
SELECT
    CASE
        WHEN income < 20000 THEN 'Low Salary'
        WHEN 20000 <= income AND income <= 50000 THEN 'Average Salary'
        WHEN income > 50000 THEN 'High Salary'
    END AS category,
    income
FROM
    Accounts)

SELECT
    category,
    COUNT(*) AS accounts_count
FROM
    Result
GROUP BY
    category
