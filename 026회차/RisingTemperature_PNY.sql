SELECT W1.ID
FROM WEATHER AS W1 JOIN WEATHER AS W2 ON W2.RECORDDATE = SUBDATE(W1.RECORDDATE, 1)
WHERE W1.TEMPERATURE > W2.TEMPERATURE;
