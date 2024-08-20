SELECT a.id
FROM weather a, weather b 
WHERE datediff(a.recorddate, b.recorddate) = 1 and a.temperature > b.temperature
