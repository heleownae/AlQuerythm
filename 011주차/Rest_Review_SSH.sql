with temp as (
select member_id, rank() over (order by counts desc) as ranks
from (select member_id, count(review_id) as counts
      from rest_review
      group by member_id
     ) a
      )

select member_name, review_text,
       date_format(review_date, '%Y-%m-%d') as review_date
from rest_review rr join member_profile p using(member_id)
where rr.member_id in (select member_id
                       from temp
                       where ranks = 1)
order by review_date, review_text
