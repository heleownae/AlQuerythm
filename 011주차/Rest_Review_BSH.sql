WITH A AS ( # 이메일 별 리뷰 수
    SELECT MEMBER_ID, COUNT(REVIEW_ID) AS RESULT
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
),

B AS ( # 리뷰를 가장 많이 작성한 아이디와 카운트 수
    SELECT MEMBER_ID, RESULT # RESULFT가 3이어야 한다.
    FROM A
    GROUP BY MEMBER_ID
    HAVING RESULT = (
        SELECT MAX(RESULT)
        FROM A)
),

C AS ( # 이메일에 해당되는 회원 이름
    SELECT MEMBER_NAME
    FROM MEMBER_PROFILE
    WHERE MEMBER_ID IN (
        SELECT MEMBER_ID
        FROM B)
)

SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS M
JOIN REST_REVIEW R
ON M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_NAME IN (SELECT MEMBER_NAME
                        FROM C)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT
