1. Specific names (DISTINCT)

SELECT DISTINCT customer_id,name
FROM `customer_data.customer_address`
WHERE state = 'OH'
ORDER BY name ASC;


STring literals 
1. Length

SELECT country, customer_id
FROM `customer_data.customer_address`
WHERE LENGTH(country) > 2

2. SUBSTRING 
   SUBSTRING(string, start, length)

SELECT DISTINCT customer_id,country
FROM `customer_data.customer_address`
WHERE SUBSTR(country, 1 , 2) = 'US'
order by customer_id

3. TRIM - Blank spaces 

SELECT DISTINCT customer_id,name
FROM `customer_data.customer_address`
WHERE TRIM(state) = 'OH'


