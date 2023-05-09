SQL 
These are helpful to tackle large data sets.
There are many DB that understands different types of SQL. Some of them are mentioned below.
1. Oracle
2. MySQL
3. Postgre SQL
4. Microsoft SQL server 

SQL Query structure 
2. SELECT - The row or column in question 
1. FROM - THE SPECIFIC DATA SET 
3. WHERE - The condition that needs to be met 
   
Example - 
SELECT first_Name, Last_Name, Customer_ID
FROM Dataset.csv
WHERE first_Name = 'Ankit' AND Last_Name = 'Sati' AND Customer_ID > 0

Conditions
WHERE field1 = 'Chavez'
WHERE field1 LIKE 'Ch%' - This  one will show all the phrases that begin with ch in the column 

Comment 
Syntax - To add description
 /* and */, or after two dashes (--)

 Alias - This is to circumvent the comments and make the commands more readable 
  field_1 AS first_name
  Table AS Customer_Data 

Example 
Query to select all the employees with low salaries and taking out the interns from the equation.
  SELECT *
  FROM Employees
  WHERE 
    jobcode <> 'INT'
    AND salary <= 30000

Helpful links 
Postgre SQL - https://towardsdatascience.com/sql-cheat-sheet-776f8e3189fa

EXAM = 100/100