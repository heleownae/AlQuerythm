SELECT CUSTOMER_ID, PRODUCT_KEY
FROM CUSTOMER
WHERE PRODUCT_KEY IN (SELECT PRODUCT_KEY FROM PRODUCT);
