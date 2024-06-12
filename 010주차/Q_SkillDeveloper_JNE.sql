WITH SkillSets AS (
    SELECT D.ID,
           D.EMAIL,
  -- 스킬을 가지고 있는지에 따라 1, 0 출력하여 1만 뽑
           MAX(CASE WHEN S.CATEGORY = 'Front End' THEN 1 ELSE 0 END) AS HasFrontEnd,
           MAX(CASE WHEN S.NAME = 'Python' THEN 1 ELSE 0 END) AS HasPython,
           MAX(CASE WHEN S.NAME = 'C#' THEN 1 ELSE 0 END) AS HasCSharp
    FROM DEVELOPERS D JOIN SKILLCODES S ON (D.SKILL_CODE & S.CODE) <> 0
    GROUP BY D.ID, D.EMAIL),
Grades AS (
    SELECT ID,
           EMAIL,
  -- 기술 갖고 있는 사람들 등급매기
           CASE WHEN HasFrontEnd = 1 AND HasPython = 1 THEN 'A'
           WHEN HasCSharp = 1 THEN 'B'
           WHEN HasFrontEnd = 1 THEN 'C'
           ELSE NULL
           END AS GRADE
    FROM SkillSets)
SELECT GRADE,
       ID,
       EMAIL
FROM Grades
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID;
