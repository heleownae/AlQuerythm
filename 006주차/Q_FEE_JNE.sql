with c as (
    # 세단, SUV 차량 중 할인율이 30일 이상 대여 기간에 해당 하는 차량
    select c.car_id,
           c.car_type,
           c.daily_fee,
           p.discount_rate
    from CAR_RENTAL_COMPANY_CAR c 
    inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p on c.car_type = p.car_type
    where c.car_type in ('SUV', '세단') and p.duration_type = '30일 이상'),
h as (
    # 대여 시작, 종료일이 11월에 해당하는 차량 선별
    select distinct car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where ((start_date between '2022-11-01' and '2022-11-30') 
           or (end_date between '2022-11-01' and '2022-11-30') 
           or (start_date <= '2022-11-01' and end_date >= '2022-11-30')))
select c.CAR_ID, 
       c.CAR_TYPE,
       ROUND((c.DAILY_FEE * 30) * (1 - c.DISCOUNT_RATE / 100.0), 0) as FEE 
from c
    # h CTE에 해당하는 차량 제외
where c.car_id not in (select car_id from h)
    # 요금 계산 50만 이상, 200만 미만
      and ((c.daily_fee * 30) * (1 - c.DISCOUNT_RATE / 100.0) >= 500000) 
      and ((c.daily_fee * 30) * (1 - c.DISCOUNT_RATE / 100.0) < 2000000)
order by FEE desc, CAR_TYPE, CAR_ID desc