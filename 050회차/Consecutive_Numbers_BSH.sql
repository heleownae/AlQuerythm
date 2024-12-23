SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT num, 
           COUNT(*) OVER (PARTITION BY num, grp) AS consecutive_count
    FROM (
        SELECT num,
                --- 연속적이지 않은 숫자를 가려낸다.---
               ROW_NUMBER() OVER (ORDER BY id) - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
        FROM logs
    ) subquery1
) subquery2
WHERE consecutive_count >= 3;
