WITH sort AS(
SELECT person_name,
       weight,
       SUM(weight) OVER (ORDER BY turn) AS accumulate
FROM Queue
)
SELECT person_name
FROM sort
WHERE accumulate <= 1000
ORDER BY accumulate desc
LIMIT 1;
