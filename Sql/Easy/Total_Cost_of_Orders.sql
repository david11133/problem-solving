SELECT c.customer_id, c.first_name, SUM(o.total_amount) AS total_cost
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name
ORDER BY c.first_name;
