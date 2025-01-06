WITH Totalweight AS(
    SELECT
        person_name,
        weight,
        SUM(weight) OVER(ORDER BY turn) AS total # 누적합 sum over
    FROM
        Queue
)
SELECT
    person_name
FROM
    Totalweight
WHERE
    total <= 1000
ORDER BY
    total DESC
LIMIT
    1;
