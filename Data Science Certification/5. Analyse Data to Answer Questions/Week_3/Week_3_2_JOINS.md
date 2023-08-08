JOIN 
Combining results from 2 tables (YOU define the condition of join when a clause is met. This clause is written in ON)

SELECT employees.name, departments.name
FROM Employee_data.employees
JOIN Employee_data.departments
ON  employees.department_id = departments.department_id
ORDER BY  employees.name ASC

LEFT AND RIGHT
Table mentioned first is Left and the second one is right.

INNER JOIN
The one above. This will have the matching values from both tables 

LEFT JOIN 
ALl the values from the left table would be included 

RIGHT JOIN 
ALL The numbers from the right side would be joined 

Full outer Join 
ALL of the values from both the tables are included 

SELECT employees.name, departments.name
FROM Employee_data.employees
FULL OUTER JOIN Employee_data.departments
ON  employees.department_id = departments.department_id
ORDER BY  employees.name ASC


IMPORTANT

SELECT 
    AVG(edu.value) average_value, summary.region
FROM 
    `bigquery-public-data.world_bank_intl_education.international_education` AS edu
INNER JOIN 
    `bigquery-public-data.world_bank_intl_education.country_summary` AS summary
ON edu.country_code = summary.country_code
WHERE summary.region IS NOT null
GROUP BY summary.region
ORDER BY average_value DESC


SELECT
 seasons.market AS university,
 seasons.name AS team_name,
 seasons.wins,
 seasons.losses,
 seasons.ties,
 mascots.mascot AS team_mascot
FROM
 `bigquery-public-data.ncaa_basketball.mbb_historical_teams_seasons` AS seasons
LEFT JOIN
 `bigquery-public-data.ncaa_basketball.mascots` AS mascots
ON
 seasons.team_id = mascots.id
WHERE
 seasons.season = 1984
 AND seasons.division = 1
 AND  seasons.market IS NOT NULL
ORDER BY
 seasons.market

________________________________________________________________________________________________________

COUNT - Count of a total number of queries returned 
COUNT DISTINT - Returns only distinct values 

Very important - If we use a function in the select clause we need to use the GROUP by clasue as well. If after using a function in select we have 3 columns. Group by 2 colums atkeast. (n-1)

SELECT warehouse.state AS state,
COUNT (DISTINCT order_id) AS total_states, warehouse_alias AS name
FROM warehouse_datasets.Orders AS orders 
JOIN warehouse_datasets.warehouse AS warehouse 
ON orders.warehouse_id = warehouse.warehouse_id
GROUP BY warehouse.state, name
LIMIT 100