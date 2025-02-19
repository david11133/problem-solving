SELECT user_id, last_login_date
FROM users
WHERE last_login_date >= CURRENT_DATE - INTERVAL '30 days';
