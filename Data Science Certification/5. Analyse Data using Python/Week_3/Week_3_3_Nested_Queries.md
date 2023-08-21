Sub queries 
Inner most executes first 
Inner reults are used for the outer results
A SET command can’t have a nested subquery because it is used with UPDATE to adjust specific columns and values in a table.

1. Subquery nested in Select
SELECT product_name, 
       (SELECT SUM(quantity) 
       FROM orders 
       WHERE orders.product_id = products.product_id) AS total_quantity
FROM products;

SELECT product_name,SUM(order.quantity)
FROM orders
JOIN products
ON orders.product_id = products.product_id
GROUP BY product.product_name

1. Subquery nested in FROM
SELECT
  id,
  name,
  number_of_rides AS number_of_rides_starting_station
FROM
  (
    SELECT
      start_station_id,
      COUNT(*) AS number_of_rides
    FROM
      bigquery-public-data.london_bicycles.cycle_hire
    GROUP BY
      start_station_id
  )
  AS station_num_trips
  INNER JOIN
  bigquery-public-data.london_bicycles.cycle_stations ON id = start_station_id
  ORDER BY
    number_of_rides DESC

1. Subquery nested in WHERE
SELECT Employee.first_name, Employee.last_name
FROM EMployee 
WHERE EMployee.emp_id IN (
    SELECT Works_with.emp_id
    FROM Works_with 
    WHERE Works_with.total_sales > 30000
);



PART 2 - Using subqueries to aggregate data
We cannot do WHERE after GROUP BY.
Hence we use HAVING instead of WHERE 
CASE - This can be used for multiple IF and THEN statements 

CASE 
WHEN (Condition)
THEN "Message or operation"
WHEN (Condition )AND (Condition)