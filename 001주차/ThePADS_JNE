-- Q1
select concat(name, '(', substr(occupation, 1, 1), ')')
from occupations
order by 1;

-- Q2
select concat('There are a total of ', count(occupation), ' ', lower(occupation), 's.')
from occupations
group by occupation
order by count(occupation);
