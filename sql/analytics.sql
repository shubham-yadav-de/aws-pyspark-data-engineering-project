SELECT
    country,
    SUM(amount) AS total_amount
FROM sales_data
GROUP BY country
ORDER BY total_amount DESC;
