select t.student_id, t.student_name, s.subject_name, count(e.student_id) as attended_exams
from students t cross join subjects s left join examinations e on t.student_id = e.student_id and s.subject_name = e.subject_name
group by 1, 2, 3
order by t.student_id, s.subject_name
