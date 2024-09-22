SELECT *
FROM Cinema
WHERE description not in ('boring') and id % 2 = 1
ORDER BY rating desc
