SELECT DISTINCT num ConsecutiveNums
# 서브쿼리에서 LAG 함수를 사용하여 현재 행의 num 값과 이전 두 행의 num 값
FROM (SELECT num,
             LAG(num, 1) OVER (ORDER BY id) num1,
             LAG(num, 2) OVER (ORDER BY id) num2
      FROM Logs) subquery
WHERE num = num1 AND num = num2;
