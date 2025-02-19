SELECT country, product_id, 
       VARIANCE(RANK() OVER (PARTITION BY country ORDER BY sales DESC)) AS rank_variance
FROM product_sales;
