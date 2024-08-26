SELECT W1.id
FROM Weather AS W1
WHERE W1.temperature > (
    SELECT W2.temperature
    FROM Weather AS W2
    WHERE DATEDIFF(W1.recordDate, W2.recordDate)=1
)
