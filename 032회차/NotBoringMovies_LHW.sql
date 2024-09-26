SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 = 1 AND description NOT LIKE '%boring%'
ORDER BY rating DESC;
