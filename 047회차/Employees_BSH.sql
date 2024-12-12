SELECT
  E1.employee_id,
  E1.name,
  COUNT(E2.employee_id) AS reports_count,
  ROUND(AVG(E2.age)) AS average_age
FROM
  EMPLOYEES AS E1
  LEFT JOIN EMPLOYEES AS E2
  ON E1.employee_id = E2.reports_to
WHERE
  E2.employee_id IS NOT NULL
GROUP BY
  E1.employee_id, E1.name;
