SELECT *
FROM Cinema
WHERE id % 2 = 1
AND description != 'boring'  --not은 안돼--
ORDER BY rating DESC;
