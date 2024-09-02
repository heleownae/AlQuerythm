SELECT EM.name, BO.bonus
FROM Employee AS EM
LEFT JOIN Bonus AS BO
ON EM.empId = BO.empId
WHERE BO.bonus < 1000 OR BO.bonus IS NULL;
