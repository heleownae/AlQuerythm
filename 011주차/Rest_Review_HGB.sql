select z.MEMBER_NAME,
       r.REVIEW_TEXT,
       date_format(r.REVIEW_DATE, '%Y-%m-%d')
from
    (SELECT r.MEMBER_ID,
            p.MEMBER_NAME,
            rank() over (order by count(*) desc) rk
     from REST_REVIEW r left join MEMBER_PROFILE p on p.MEMBER_ID = r.MEMBER_ID
     group by r.MEMBER_ID
     order by count(*) desc) z
     join REST_REVIEW r on z.MEMBER_ID = r.MEMBER_ID
     where z.rk = 1
     order by 3, 2
