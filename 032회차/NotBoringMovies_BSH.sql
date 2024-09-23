SELECT *
FROM Cinema
WHERE id % 2 = 1
AND description != 'boring'  --not말고 not in--
ORDER BY rating DESC;
