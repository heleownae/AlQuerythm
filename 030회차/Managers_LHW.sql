SELECT a.name
FROM Employee a JOIN Employee b ON a.id = b.managerId
GROUP BY b.managerId
HAVING COUNT(b.managerId) >= 5;
