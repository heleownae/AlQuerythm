SELECT ROUND(AVG(LAT_N), 4)
FROM (
    SELECT ROW_NUMBER() OVER (ORDER BY LAT_N) AS RN, COUNT(*) OVER () AS C, LAT_N  -- LAT_N으로 정렬 후 행 번호 부여 (RN), 전체 행 개수 (C), LAT_N
    FROM STATION
) AS ST
WHERE RN IN (C/2, (C/2)+1, (C+1)/2);     -- 전체 행이 짝수 개인 경우 C/2와 (C/2)+1 를 가져와서 SELECT에서 평균 값 반환 / 홀수 개인 경우 (C+1)/2 반환
