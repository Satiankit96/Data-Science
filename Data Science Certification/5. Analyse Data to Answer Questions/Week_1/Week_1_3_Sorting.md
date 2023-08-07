1. Sorting Datasets in Spread sheets

Sheet sort - Entire sheet is sorted 
Range sort - Range of cells 

Sorting by menu - already done 

Sorting by formulae
=SORT(A2:D6,2,TRUE)
Range,number of column, TRUE - ASC
FALSE - DESC

Difference between formulae and menu 
The sort from a spreadsheet's Data tab overwrites the cells containing the unsorted data with the sorted data, while a written SORT function inserts the sorted data in a different cell range. 

2. Sorting Datasets with SQL _Nothing new to learn here as well 
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
FROM
  `bigquery-public-data.noaa_gsod.gsod2020`
WHERE
  stn="725030" -- La Guardia
  OR stn="744860" -- JFK
ORDER BY
  date DESC,
  stn ASC