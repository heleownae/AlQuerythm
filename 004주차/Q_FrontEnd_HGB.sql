select distinct a.id, a.email, a.first_name, a.last_name
from developers as a join skillcodes as b on a.skill_code & b.code
where b.category = 'front end'
order by a.id
