SELECT ifnull(u.unique_id, null) unique_id,
       e.name
FROM employees e LEFT JOIN EmployeeUNI u ON e.id = u.id
