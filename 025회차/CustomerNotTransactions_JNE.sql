SELECT v.customer_id,
       count(v.customer_id) count_no_trans
FROM visits v LEFT JOIN transactions t ON v.visit_id = t.visit_id
WHERE v.visit_id not in (SELECT visit_id FROM transactions)
GROUP BY v.customer_id
