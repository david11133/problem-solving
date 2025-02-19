SELECT user_id, COUNT(*) AS email_count,
       RANK() OVER (ORDER BY COUNT(*) DESC) AS activity_rank
FROM emails
GROUP BY user_id;
