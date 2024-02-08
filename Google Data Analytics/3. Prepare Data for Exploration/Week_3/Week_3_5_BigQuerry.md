BigQuery is a data warehouse on Google Cloud that data analysts can use to query, filter large datasets, aggregate results, and perform complex operations. 
Download links 
MySQL - https://dev.mysql.com/doc/mysql-getting-started/en/
Server - https://docs.microsoft.com/en-us/sql/relational-databases/tutorial-getting-started-with-the-database-engine?view=sql-server-ver15
postgreSQL - https://www.postgresql.org/docs/10/tutorial-start.html
SQLite - https://www.sqlite.org/quickstart.html

TUtorial 
1. Open SQL workspace 
2. Click add and choose a DB 
3. While choosing a DB we can check in some of the tables to see if it is of any use or not. 
- SELECT *  FROM `bigquery-public-data.sunroof_solar.solar_potential_by_postal_code` LIMIT 1000
- bigquery-public-data - This is the name of the database and whatever follows after the dot is the name of the table. 

Query Examples 

SELECT *
FROM `city_data.Cities`
WHERE avg_temp between 45 and 65
  AND avg_commute < 60

  Challenge 1 

SELECT *
  -- COUNT(*) as num_of_Trips
FROM bigquery-public-data.london_bicycles.cycle_hire
WHERE duration >=1200;

1. 42
2. 21014
3. 487
4. Park Lane , Hyde Park
5. Total results -  5987982 

SELECT DISTINCT bike_id
FROM bigquery-public-data.london_bicycles.cycle_hire
WHERE duration > 2400

Distint Values - 31637

Question 2 
East Village, Queen Elizabeth Olympic Park

QUestion 3 
Top 5 baby names for boys 
SELECT 
  name,
  count
From babynames.names_2014
WHERE 
  gender= 'M'
ORDER BY
  count DESC
LIMIT
  5

Review the SQL documentations 
1. Use of ' ' vs " "
We use "" when there is an ' in the string itslef. (Same as any programming language).

2. Comments : Use -- or #
   For multiline comments use : /* 

   */

3. Snake_case - Same naming convention of a new column as we have used in creating folders for these files.
   CamelCase - This is another naming convention WhereEveryNewWordStartsWithCapital. It is better to use the snake_case. 
   SUM (tickets)                              - f0 (Default name for an column)
   SUM (tickets) AS total_tickets             - Here the new added column would be named as total_Tickets.

Note - It is always a good idea to create column headers when working in excel using snake_case. 
