WITH department as(
SELECT employee_id,
       department_id depart
FROM Employee
WHERE primary_flag = 'Y'
GROUP BY employee_id
)
SELECT e.employee_id,
       IF(count(e.employee_id) = 1, e.department_id, d.depart) department_id
FROM Employee e LEFT JOIN department d on e.employee_id = d.employee_id
GROUP BY e.employee_id
