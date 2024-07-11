select year(s.sales_date) as year,
       month(s.sales_date) as month,
       count(distinct s.user_id) as purchased_users,
       round(count(distinct s.user_id)/(select count(distinct user_id) from user_info where joined like '2021%'),1) as purchased_ratio
from online_sale s join user_info i using(user_id)
where i.joined like '2021%'
group by 1, 2
order by 1, 2
