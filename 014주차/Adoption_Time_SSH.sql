set @hour := -1;
select (@hour := @hour + 1) as hour,
       (select count(*)
        from animal_outs
        where hour(datetime) = @hour) as count
from animal_outs
where @hour < 23



with recursive temp as (
select 0 as hour
union all
select hour + 1
from temp
where hour <23)


select t.hour, count(animal_id) as count
from temp t left join animal_outs a on t.hour = hour(a.datetime)
group by t.hour
order by t.hour


