SELECT
  USER_ID,
  COUNT(FOLLOWER_ID) AS followers_count
FROM
  FOLLOWERS
GROUP BY
  USER_ID
