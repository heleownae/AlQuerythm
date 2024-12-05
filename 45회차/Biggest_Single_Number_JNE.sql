WITH counts as(
SELECT num,
       COUNT(num) counting
FROM MyNumbers
GROUP BY num
HAVING COUNT(num) = 1
)
SELECT CASE WHEN COUNT(num) > 0 THEN MAX(num)
       ELSE NULL
       END AS num
FROM counts;
