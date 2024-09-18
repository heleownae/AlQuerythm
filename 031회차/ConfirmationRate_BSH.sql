SELECT SI.user_id
       -- INFULL 없으면 NULL 떠서 추가 --
       , IFNULL(ROUND(SUM(CO.action = 'confirmed') / COUNT(CO.action),2),0) AS confirmation_rate
FROM Signups AS SI
LEFT JOIN Confirmations AS CO ON SI.user_id = CO.user_id
GROUP BY SI.user_id
