-- The Report (이해원)
select if(g.Grade < 8, 'NULL', s.Name), g.Grade, s.Marks
from Students s left join Grades g on s.Marks between g.Min_Mark and g.Max_Mark
order by g.Grade desc, if(g.Grade < 8, s.Marks, s.Name) asc;