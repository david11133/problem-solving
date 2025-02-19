SELECT user_id, 
       SUM(distance) AS total_distance, 
       SUM(amount_spent) AS total_spent, 
       SUM(distance) / NULLIF(SUM(amount_spent), 0) AS distance_per_dollar
FROM trips
GROUP BY user_id;
