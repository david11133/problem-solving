SELECT user_id, MIN(stream_start_date) AS first_stream_date
FROM streamers
WHERE user_id IN (SELECT user_id FROM viewers)
GROUP BY user_id;
