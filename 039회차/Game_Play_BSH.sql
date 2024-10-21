-- 각 플레이어의 첫 로그인 날짜를 구함.
WITH FirstLogin AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),

-- 첫 로그인한 다음 날 다시 로그인한 플레이어를 찾음.
NextDayLogin AS (
    SELECT f.player_id
    FROM FirstLogin AS f
    JOIN Activity AS a 
    ON f.player_id = a.player_id 
    AND DATEDIFF(a.event_date, f.first_login_date) = 1
)

-- 첫날 로그인하고 그다음 날에도 로그인한 플레이어 수를 전체 플레이어 수로 나눔.
SELECT 
    ROUND(COUNT(DISTINCT n.player_id) / COUNT(DISTINCT f.player_id), 2) AS fraction
FROM FirstLogin f
LEFT JOIN NextDayLogin n
ON f.player_id = n.player_id;
