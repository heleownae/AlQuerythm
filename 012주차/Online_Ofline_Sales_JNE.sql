SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
       PRODUCT_ID,
       USER_ID,
       SALES_AMOUNT
FROM ONLINE_SALE
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03'
UNION ALL
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
       PRODUCT_ID,
       # OFFLINE_SALE 테이블에는 USER_ID 칼럼이 없기 때문에 만들어 줘야함
       NULL as USER_ID,
       SALES_AMOUNT
FROM OFFLINE_SALE
WHERE DATE_FORMAT(SALES_DATE, '%Y-%m') = '2022-03'
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID
