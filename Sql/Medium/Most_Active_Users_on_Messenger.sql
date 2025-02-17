SELECT sender_id, COUNT(*) AS message_count
FROM messages
GROUP BY sender_id
ORDER BY message_count DESC
LIMIT 5;
