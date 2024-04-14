select if(g.Grade < 8, 'NULL', s.Name), g.Grade, s.Marks
from Students s, Grades g
where s.Marks between g.Min_Mark and g.Max_Mark
order by g.Grade desc, case when g.Grade >= 8 then s.Name when g.grade <8 then s.Marks end asc;
