# 틀림
SELECT HISTORY_ID, FLOOR(((END_DATE-START_DATE+1)*DAILY_FEE) *
       CASE WHEN (END_DATE - START_DATE + 1) BETWEEN 7 AND 29 THEN 0.95
            WHEN (END_DATE - START_DATE + 1) BETWEEN 30 AND 89 THEN 0.93
            WHEN (END_DATE - START_DATE + 1) >= 90 THEN 0.90
            ELSE 1
            END) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS CAR
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS HIS
ON CAR.CAR_ID = HIS.CAR_ID
WHERE CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC
