with temp as (
select s.user_id,
       case when action = 'confirmed' then 1
            else 0 end as rate
from confirmations c right join signups s using(user_id)
)

select user_id, round(avg(rate),2) as confirmation_rate
from temp
group by user_id
