select case when g.grade < 8 then 'NULL'
           else s.name end,
           g.grade, 
           s.marks
from students s left join grades g on s.marks between g.min_mark and g.max_mark
order by 2 desc, case when g.grade>=8 then s.name  when g.grade<8 then s.marks end asc           
