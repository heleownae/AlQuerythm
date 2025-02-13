WITH FirstLogin AS (
    SELECT player_id, 
           MIN(event_date) first_login_date
    FROM Activity
    GROUP BY player_id
), NextDayLogin AS (
    SELECT A.player_id
    FROM Activity A
    JOIN FirstLogin F ON A.player_id = F.player_id
    WHERE A.event_date = DATE_ADD(F.first_login_date, INTERVAL 1 DAY)
)

SELECT ROUND(COUNT(DISTINCT N.player_id) / COUNT(DISTINCT F.player_id), 2) fraction
FROM FirstLogin F LEFT JOIN NextDayLogin N ON F.player_id = N.player_id;
