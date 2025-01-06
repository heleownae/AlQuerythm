WITH Totalweight AS (
    SELECT
        person_name,
        weight,
        SUM(weight) OVER(ORDER BY turn) AS total # 누적합 sum over
    FROM
        Queue)

SELECT
    person_name
FROM
    Totalweight
WHERE
    total <= 1000 # 1000과 같거나 작은 이름부터 내림차순
ORDER BY
    total DESC
LIMIT
    1;
