#단순하게 해서 꿀빨려다 실패

select round((max(lat_n)+min(lat_n))/2, 4)
from station


#오라클 답
select round(median(lat_n), 4)
from station


with temp as
(
select percent_rank() over (order by lat_n) as ranking, lat_n
from station
    )
    
select round(lat_n, 4)
from temp
where ranking = '0.5'
