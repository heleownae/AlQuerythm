SELECT
    YEAR(SALES_DATE) AS YEAR,
    MONTH(sales_date) AS MONTH,
    COUNT(DISTINCT SAL.USER_ID) AS PURCHASED_USERS,
    ROUND((COUNT(DISTINCT SAL.USER_ID)) / (SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED) = 2021),1) AS  PUCHASED_RATIO
FROM USER_INFO AS INF
RIGHT JOIN ONLINE_SALE AS SAL
ON INF.USER_ID = SAL.USER_ID
WHERE YEAR(JOINED) = 2021
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH
