select concat(name, '(', substr(occupation, 1, 1), ')') txt
from occupations
union
(
select concat("There are a total of ", count(*), ' ', lower(occupation), 's.') txt
from occupations
group by occupation
)
order by txt
