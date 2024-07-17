SELECT name
FROM Customer
WHERE name not in (SELECT name FROM Customer WHERE referee_id = 2)
