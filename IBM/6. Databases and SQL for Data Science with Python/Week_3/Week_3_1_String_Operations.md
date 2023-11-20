<!-- https://www.coursera.org/learn/sql-data-science/ungradedWidget/mloSg/sql-cheat-sheet-intermediate-like-order-by-group-by -->
<!-- CHEAT SHEET -->

Wildcards 
% -  ANy characters before the percentage sigh
_ - One character
SELECT *
FROM Client
WHERE client_name LIKE '%LLC';

IF LABEL IS PRESENT 
SELECT *
FROM Branch_Supplier
WHERE supplier_name LIKE "% Label%" ;

BORN IN A SPECIFIC MONTH 
SELECT *
FROM Employee 
WHERE birth_date  LIKE '____-10%'


______________________________________________________________________________________________________________ 
1. Sorting Datasets with SQL _Nothing new to learn here as well 
(By Default ASC)
Sorting using WHERE clause 

SELECT * 
FROM `stellar-chemist-390605.customer_data.Movies` 
WHERE Genre = 'Comedy'
ORDER BY Release_Date DESC

Using AND creating a better filter

SELECT * 
FROM `stellar-chemist-390605.customer_data.Movies` 
WHERE Genre = 'Comedy' AND Revenue > 30000000
ORDER BY Release_Date DESC


USE OF IF CLAUSE 

SELECT
  stn,
  date,
-- Use the IF function to replace 9999.9 values, which the dataset description explains is the default value when temperature is missing, with NULLs instead.
  IF(
     temp=9999.9,
     NULL,
     temp) AS temperature,
-- Use the IF function to replace 999.9 values, which the dataset description explains is the default value when wind speed is missing, with NULLs instead.
  IF(
     wdsp="999.9",
     NULL,
     CAST(wdsp AS Float64)) AS wind_speed,
-- Use the IF function to replace 99.99 values, which the dataset description explains is the default value when precipitation is missing, with NULLs instead.
  IF(
     prcp=99.99,
     0,
     prcp) AS precipitation


____________________________
Having vs WHERE 
WHERE Works for the entire DB 
SELECT *
WHERE ....

HAVING works particularly within the GROUPBY Clause 

SELECT *
FROM ...
GROUP BY country
HAVING COUNT(COUNTRY)>4