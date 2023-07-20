1. DDL VS DML 
   
DDL stands for Data Definition Language.
DDL statements are used to create, remove or modify database objects like table. You do not need to commit the changes after running DDL commands.
CREATE statement can be used to create any database objects like tables, views, functions, procedures, triggers etc.
DROP statement can be used to remove any database objects like tables, views, functions, procedures, triggers etc.
ALTER statement can be used to modify the structure of a database objects.
TRUNCATE statement can be used to remove all the data from a table at once. 

Data Manipulation Language. 
DML statements are used to add, remove or modify data from database tables. It is mandatory to run the COMMIT command after running a DML statement so as to save the changes to the database (some tools may have auto commit on so you don’t have to manually run the commit command). 
INSERT statement will add rows or records to a table.
UPDATE statement will modify the data in the table.
DELETE statement will remove one or multiple rows from a table.
MERGE statement will either do an update or insert to a table based on the available data. 


2. DELETE vs TRUNCATE
Truncate is much faster 
Truncate cannot have a where statement.
DDL Language so no commit is required.

DELETE is comparitively slower 
We need to commit changes 
Comparitively slower

3. CASE STATEMENT 
   THis is an If else statement 

4. JOINS 
   - LEFT 
   - RIGHT 
   - FULL OUTER JOIN 
   - INNER JOIN 
   - Natural Join - WE do not use ON. The column names should be the same. 
   - SELF JOIN - WHEN you join a table to itself 

5. DISTINCT and GROUP BY  
    - It just llays out the entities that are distinct in a table 

    - Group by gives you all the occurances of the distinct values in a table 

6. What are the rules to follow when using UNION operator?
Both queries must return same same no of columns.
The columns in both the queries must be in same order.
Data type of all the columns in both the queries must be same.

7. What are aggregate functions? Name and explain different types of aggregate functions in SQL?
SUM 
AVG
MIN
MAX
COUNT 

8. Ranks 1,2,2,4,5
   Dense Ranks 1,2,2,3,4
   Row numbers 1,2,3,4,5


10. Date function 
    SELECT DATE_FORMAT('31-01-2021', '%d-%m-%Y') as date_value;

    PostgreSQL:
    SELECT TO_DATE('31-01-2021', 'DD-MM-YYYY') as date_value;

11. Fetching the first name.
    SELECT SUBSTRING(full_name, 1, INSTR(full_name, ' ', 1, 1) - 1) as first_name FROM dual;
    Select substring_index(full name,' ',1)

13. SUBQueries  
    It is not a good practice. Can we resolved by using the WITH clause. 

14. WHERE vs HAVING 
    WHERE can be used with the 