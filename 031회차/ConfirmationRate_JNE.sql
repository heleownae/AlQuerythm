SELECT s.user_id,
       ROUND(
           CASE 
               WHEN COUNT(c.action) = 0 THEN 0 
               ELSE SUM(c.action = 'confirmed') / COUNT(c.action) 
           END, 
           2) AS confirmation_rate
FROM Signups s LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id
