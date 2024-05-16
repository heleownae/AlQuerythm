SELECT rental_car.car_id
     , rental_car.car_type
     , round(rental_car.daily_fee*30 - (rental_car.daily_fee*30)*((rental_dc.discount_rate/100))) as FEE
FROM 
    (  
        SELECT car_id
             , start_date
             , end_date
        FROM car_rental_company_rental_history
    ) rental_date
INNER JOIN    
    ( 
        SELECT car_id
             , car_type
             , daily_fee
        FROM car_rental_company_car
    ) rental_car
ON rental_date.car_id = rental_car.car_id 
INNER JOIN
    (
        SELECT car_type
             , duration_type
             , discount_rate
        FROM car_rental_company_discount_plan
    ) rental_dc
ON rental_car.car_type = rental_dc.car_type
WHERE rental_car.car_id NOT IN 
    ( 
        SELECT car_id
        FROM car_rental_company_rental_history
        WHERE end_date > '2022-11-01' and start_date < '2022-12-01'
    ) AND rental_dc.duration_type = '30일 이상'
GROUP BY rental_car.car_id
HAVING rental_car.car_type IN ('SUV', '세단') 
    AND (FEE >=500000 and FEE<=2000000)     
ORDER BY fee DESC, car_type ASC, car_id DESC ;
