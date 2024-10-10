SELECT
    query_name,
    ROUND((SUM(rating/position))/COUNT(query_name),2) AS quality,
    ROUND((COUNT(IF(rating<3,1,NULL))/COUNT(*))*100,2) AS poor_query_percentage
FROM
    Queries
GROUP BY
    query_name;

-- ROUND(((SELECT COUNT(query_name) FROM Queries WHERE rating<3)/COUNT(query_name))*100,2) 서브쿼리써서 QUERY_NAME 구분이 안됐던 문제
