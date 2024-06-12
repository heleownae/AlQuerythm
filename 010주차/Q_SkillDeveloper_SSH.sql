with temp as (
select case when (group_concat(name) like '%Python%') and max(category) = 'Front End' then "A"
            when group_concat(name) like '%C#%' then "B"
            when max(category) = 'Front End' then "C" end as Grade,
    id, min(email) email
from developers d join skillcodes s on d.skill_code & s.code = s.code
group by id
    )

select grade, id, email
from temp
where grade is not null
order by grade, id
