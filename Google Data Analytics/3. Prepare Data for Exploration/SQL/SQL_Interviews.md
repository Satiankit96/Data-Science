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
    HAVING can be used with Aggregated objects. (GROUP BY) 

15. Indexes USed in a column 
    Basically, Index creates a pointer to each value in the column which in turn helps in finding any specific value from this column in a much faster way.     
    Please note, different indexes have different functionalities and will behave differently from each other but in a nutshell index is used to identify any value faster from the table column(s).

16. What are steps you would take to tune a SQL query?
- Check the SQL Query. 
  - Avoid any repeated subqueries by using a WITH clause. 
  - Make sure all the table joins are correct and all the filter conditions are applied as intended. 

- Check if index is created for the desired columns.
  - Make sure correct indexes are created on the desired columns. Following the correct type of indexes.
  - Avoid creating unnecessary indexes. 

17. Primary key - Unique values without any null values 
    Unique key - Unique values that can have null values 
    Foreign key -USed to create links within tables. Primary key in some other table. 

18. What is the difference between a view and a synonym?
    - View - This is like giving name to a returned SQL Querry 
    - Synonym - Synonym on the other hand is just an alias or an alternate name that you can provide to any database objects such as tables, views, sequences, procedures etc.  
    - A view looks and acts just like a real table, but is always created on-the-fly as required, so it is always up to date. A synonym is an alias for a table.


19. When can a function NOT be called from SELECT query?


    - If the function includes DML operations like INSERT, UPDATE, DELETE etc then it cannot be called from a SELECT query. Because SELECT statement cannot change the state of the database.

20. What is a trigger?

    Trigger is a database object which is similar to a stored procedure which will automatically get invoked or executed when the specified event occurs in the database.

21. Materialized views vs Views 
    Similar to views, materialized views are also database objects which are formed based on a SQL Query however unlike views, the contents or data of the materialized views are periodically refreshed based on its configuration.


22. What is MERGE statement?


Merge is part of the DML commands in SQL which can be used either perform INSERT or UPDATE based on the data in the respective table.

If the desired data is present then merge will update the records. If desired data is not present then merge will insert the records. 

Sample merge statement is shown below. Here if the managers and directors table have matching records based the ID field then UPDATE command will be run else if there are no matching records then INSERT statement will be executed.

MERGE INTO managers m

  USING directors d  ON (m.id = d.id)
WHEN MATCHED THEN 

	  UPDATE SET name = 'TEST' 
WHEN NOT MATCHED THEN 

	  INSERT VALUES (d.id, d.name, 0);

23. Yesterdays Date 
    SELECT DATE_SUB(SYSDATE(), INTERVAL 1 DAY) as previous_day; 
    mysql> SELECT DATE_ADD(SYSDATE(), INTERVAL 1 DAY)

24. Function vs Procedure 
    Function should always return a value whereas for a procedure it’s not mandatory to return a value.

25. Google sheets formula -https://blog.golayer.io/google-sheets/google-sheets-formulas
26. Tips - https://www.benlcollins.com/spreadsheets/google-sheets-formulas-techniques
