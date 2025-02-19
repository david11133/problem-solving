SELECT user_id, SUM(distance) AS total_distance
FROM trips
GROUP BY user_id
ORDER BY total_distance DESC
LIMIT 10;
