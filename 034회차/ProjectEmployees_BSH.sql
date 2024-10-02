SELECT PR.project_id, ROUND(AVG(EM.experience_years),2) AS average_years
FROM Project AS PR
LEFT JOIN Employee AS EM
ON PR.employee_id = EM.employee_id
GROUP BY PR.project_id
