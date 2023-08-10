SELECT column1,column2, column1+column2 AS sum_of_1_&_2
FROM table_name

Same for others
SELECT column1,
       column2,
       column3, 
       (column1+column2)*column3 AS columnX

These are the same as functions.
Aggregate functions
Modulo - %- Remainder()

SELECT Date,
       Region,
       Small_Bags,
       Large_Bags,
       XLarge_Bags,
       Total_Bags,
       (Small_Bags+Large_Bags+XLarge_Bags) AS check_total,
       ROUND((Small_Bags/Total_Bags)*100,3 )AS percent_of_small_bags
FROM `stellar-chemist-390605.Employee_data.avocado` 
WHERE Total_Bags <> 0


Calculations with Other commands 
GROUP BY
-----EXTRACT - lets us extract a particular part of date or time from a given column 

SELECT EXTRACT(YEAR FROM STARTTIME) AS year,
COUNT(*) AS number_of_rides
FROM `bigquery-public-data.new_york_citibike.citibike_trips` 
GROUP BY year
ORDER BY year