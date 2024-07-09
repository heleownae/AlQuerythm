select year(SALES_DATE) YEAR,
       month(SALES_DATE) MONTH,
       count(distinct user_id) PUCHASED_USERS,
       # 월별 구매자 수 / 2021 전체 가입자 수
       round(count(distinct user_id) / (select count(*) from USER_INFO where year(joined) = '2021'), 1) PUCHASED_RATIO
from ONLINE_SALE
# 2021에 가입한 사람의 user_id 선별
where user_id in (select user_id from USER_INFO where year(joined) = '2021')
group by year(SALES_DATE), month(SALES_DATE)
order by year(SALES_DATE), month(SALES_DATE)
