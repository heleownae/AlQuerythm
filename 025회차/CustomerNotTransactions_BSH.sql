SELECT VI.customer_id, COUNT(*) AS count_no_trans
FROM Visits AS VI LEFT JOIN Transactions AS TR ON VI.visit_id = TR.visit_id
WHERE TR.transaction_id IS NULL
GROUP BY VI.customer_id;
