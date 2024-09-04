SELECT t.student_id, t.student_name, s.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students t
CROSS JOIN Subjects s
LEFT JOIN Examinations e
ON t.student_id = e.student_id
AND s.subject_name = e.subject_name
GROUP BY t.student_id, t.student_name, s.subject_name
ORDER BY t.student_id, s.subject_name;
