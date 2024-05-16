


with rate as (select car_type, (1- (0.01*discount_rate)) rate
              from car_rental_company_discount_plan
              where duration_type = '30일 이상')

select distinct(h.car_id), c.car_type, round(c.daily_fee*30*r.rate) fee
from car_rental_company_rental_history h join car_rental_company_car c using(car_id) join rate r using(car_type)
where h.car_id not in (select distinct car_id
                 from car_rental_company_rental_history
                 where end_date >= '2022-11-01')
                                  and c.car_type in ('세단', 'SUV')
                                  and c.daily_fee*30*r.rate between 500000 and 2000000;
                                  
                                  



#전체적인 풀이 방식은 맞았으나 비용 계산시'(1- (0.01*p.discount_rate)' 이 부분을 빠뜨려서 헤맸음ㅠ                    
with temp as (
    select distinct(h.car_id), c.car_type, c.daily_fee
    from car_rental_company_rental_history h join car_rental_company_car c using(car_id)
    where h.car_id not in (select distinct car_id
                 from car_rental_company_rental_history
                 where end_date >= '2022-11-01')
                                  and c.car_type in ('세단', 'SUV')
    )
select t.car_id, t.car_type, t.daily_fee*30*(1- (0.01*p.discount_rate)) as fee
from car_rental_company_discount_plan p join temp t using(car_type)
where p.duration_type = '30일 이상' and t.daily_fee*30*(1- (0.01*p.discount_rate)) between 500000 and 2000000

