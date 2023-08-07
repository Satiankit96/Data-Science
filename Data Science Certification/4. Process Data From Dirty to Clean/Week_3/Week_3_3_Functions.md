1. CAST() - Just like type casting 

SELECT purchase_price  
FROM `stellar-chemist-390605.customer_data.customer_purchase` 
ORDER BY CAST(purchase_price AS FLOAT64) DESC

OR

SELECT CAST(purchase_price AS FLOAT64) 
FROM `stellar-chemist-390605.customer_data.customer_purchase` 
ORDER BY CAST(purchase_price AS FLOAT64) DESC

SELECT CAST (date AS DATE),CAST(purchase_price AS FLOAT64) 
FROM `stellar-chemist-390605.customer_data.customer_purchase` 
WHERE date >'2020-12-01' AND date <'2020-12-31'
ORDER BY CAST (date AS DATE) ASC

2. CONCAT - String joining 

SELECT CONCAT(product_code,product_color) AS new_product_code
FROM `stellar-chemist-390605.customer_data.customer_purchase` 
WHERE product = 'couch'
ORDER BY new_product_code ASC
   
3. COALESCE - Return non NUll values 