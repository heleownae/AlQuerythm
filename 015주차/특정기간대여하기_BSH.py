# CTE: 세단과 SUV 할인 비율
WITH RATE AS (SELECT car_type, discount_rate
              FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
              WHERE (CAR_TYPE = '세단' OR CAR_TYPE = 'SUV')
              AND (duration_type = '30일 이상'))
              
# 메인 쿼리: 타입, 대여기간, 할인적용가
SELECT CAR.CAR_ID, CAR.car_type, FLOOR(CAR.DAILY_FEE*30*((100-DISCOUNT_RATE)*0.01)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS CAR
JOIN RATE
ON CAR.car_type = RATE.car_type
WHERE (CAR.CAR_TYPE = '세단' OR CAR.CAR_TYPE = 'SUV')
AND CAR.CAR_ID not IN (SELECT CAR_ID
                       FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                       WHERE (DATE(start_date) <= '2022-11-30' AND DATE(end_date) >= '2022-11-01'))
AND (FLOOR(CAR.DAILY_FEE*30*((100-DISCOUNT_RATE)*0.01)) BETWEEN 500000 AND 1999999)
ORDER BY FEE DESC, CAR.car_type, CAR.CAR_ID DESC
