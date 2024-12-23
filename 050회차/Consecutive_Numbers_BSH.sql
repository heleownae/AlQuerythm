SELECT DISTINCT num as ConsecutiveNums
FROM (
    SELECT num,
           --- 특정 범위의 같은 값을 지닌 행의 개수를 센다.---
           COUNT(*) OVER (PARTITION BY num, grp) AS consecutive_count
    FROM (
        SELECT num,
               --- 연속적이지 않은 숫자를 가려낸다.---
               ROW_NUMBER() OVER (ORDER BY id) - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
        FROM logs
    ) subquery1
) subquery2
WHERE consecutive_count >= 3;
