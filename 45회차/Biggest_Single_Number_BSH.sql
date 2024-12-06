SELECT 
    CASE WHEN COUNT(num) > 0 THEN MAX(num)
         ELSE NULL
    END AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) sub;
