FUnctions 
1. Count 
SELECT COUNT (emp_id)
FROM Employee;

2. Female employees 
SELECT COUNT (emp_id)
FROM Employee
WHERE sex = 'F';

3. Employees AFter 1970
SELECT COUNT (emp_id)
FROM Employee 
WHERE SEX = 'F' AND birth_date > '1970-01-01'

4. AVerage of salaries 
SELECT AVG (salary)
FROM Employee
WHERE sex = 'm';

5. Number of sex 
SELECT COUNT (sex),sex
FROM employee
GROUP BY sex;

6. Each employee sales 
SELECT SUM (total_sales),emp_id
FROM Works_With
GROUP BY emp_id;

7. Each client spend 
SELECT SUM (total_sales) AS Total,client_id
FROM Works_With
GROUP BY client_id
ORDER BY Total DESC;



__________________________________________________________________________________________________________________

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

__________________________________________________________________________________________________________________
Unions -
They should have the same data types 
Same number of columns can be imported at a time 

SELECT first_name
FROM employee
UNION
SELECT branch_name
FROM Branch
UNION
SELECT client_name 
FROM client;