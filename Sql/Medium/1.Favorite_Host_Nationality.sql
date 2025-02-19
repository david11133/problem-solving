SELECT host_nationality, AVG(review_rating) AS avg_rating
FROM airbnb_reviews
GROUP BY host_nationality
ORDER BY avg_rating DESC
LIMIT 1;
