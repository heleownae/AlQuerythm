-- 임시테이블 1
WITH T1 AS (
    SELECT LAT_N,
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS ROW_ASC,
           ROW_NUMBER() OVER (ORDER BY LAT_N DESC) AS ROW_DESC
    FROM STATION
),
-- 임시테이블 2
T2 AS (
    SELECT LAT_N
    FROM T1
    WHERE ROW_ASC = ROW_DESC
        -- 홀수개 행
        OR ROW_ASC + 1 = ROW_DESC
        -- 짝수개 행
        OR ROW_DESC + 1 = ROW_ASC
)
-- 소숫점 네 자리 중위값 추출
SELECT ROUND(AVG(LAT_N), 4) AS median_val
FROM T2;
