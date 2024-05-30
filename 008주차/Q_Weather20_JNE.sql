# 틀린 답임
# 근데 푸는 방법이 더 이상 생각 안남
SELECT ROUND(AVG(LAT_N), 4) AS median
FROM (
  SELECT LAT_N
  FROM (
    SELECT LAT_N, 
           -- 각 행에 번호 할당
           ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num,
           -- 전체 행 수
           COUNT(*) OVER() AS total_count
    FROM STATION
  ) AS with_row_numbers
-- 중앙값 선택
-- FLOOR 함수는 주어진 숫자 이하 중 가장 큰 정수를 반환하는 함수
  WHERE row_num IN (FLOOR((total_count + 1) / 2), FLOOR((total_count + 2) / 2))
) AS final_selection;
