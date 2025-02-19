SELECT winery, AVG(rating) AS avg_rating
FROM wines
GROUP BY winery
ORDER BY avg_rating DESC
LIMIT 3;
