SELECT usertype,
CONCAT(start_station_name, " to ", end_station_name) AS Route,
COUNT(*) as num_trips,
ROUND(AVG(CAST(tripduration AS int64)/60),2) AS duration

FROM `bigquery-public-data.new_york_citibike.citibike_trips` 

GROUP BY
start_station_name,end_station_name,usertype
ORDER BY
num_trips DESC
LIMIT 10

Cliff notes 
- Group by is needed when there are multiple functions in SELECT clause. Then we have to group them by 
- And order type is a mus
- For some reason as in line 3 would not execute if written as "AS"


Functions used in spread sheets 
LEN(cell) - Lenght of all characters in a Cell
Right(cell,11) Extracted 11 characters from the right
LEFT (cell,8) 8 from left would be extracted
FIND (" ") - Finds the exact position of an entity within a cell 


CONCAT_WS
A function that adds two or more strings together with a separator
CONCAT_WS (‘ . ’, ‘www’, ‘google’, ‘com’)
*The separator (being the period) gets input before and after Google when you run the SQL function

CONCAT with +
Adds two or more strings together using the + operator
‘Google’ + ‘.com’