with temp as
(
select name, marks,
           case when marks<9 then 1
                    when marks>=90 then 10
                    when marks between 10 and 89 then  substr(marks, 1, 1)+1 end as grade
from students
)
select  if(grade >=8, name, Null) as name,
            grade,
            marks
from temp
order by  CAST(grade AS UNSIGNED) desc, name asc, marks asc
