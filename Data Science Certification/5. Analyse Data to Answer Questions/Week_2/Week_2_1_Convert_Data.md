Spreadspeet 

Type Casting 
Method 1 -> Select colum - Format - choose the Type
Method 2 -> =CONVERT(B2,"F","C") OR =CONVERT(-22, "C", "F")
IMP - It is always better to copy the reults in a new column and paste the results. (This is to remove the formula)

DATA validation  
Select Column - data validation - Add rule - Slect options and colors 
- Add dropdowns 
- Create check boxes and many more 
- Protect data and formula (The reject option - It throws an error)

Some other Basic type casts

IN SQL 
SELECT CAST(number AS FLOAT) 
FROM table_name
SELECT CAST(column_Name AS VARCHAR(20))
FROM table_name
