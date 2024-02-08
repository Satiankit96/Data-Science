Data Aggregation - Collecting all the data into a single place 
VLOOKUP - It searches for a certain value within a column and returns the values corresponsding to it.
This is primarily used to connect data between two sources

- This is generally used to look for data between different spreadsheets.
- The data between the two spreadsheets should be consistent for this feature to work 
- In order to achieve this clean data, we have to do the below 
1. =Value(A2) - Converts the text string to a numerical value 
2. =TRIM(Cell) - Trims the extra spaces in a cell 
3. Remove duplicates using the function across the sheets. 

VLOOKUP(ValueToSearch,Range,column,false)
False - Exact match 
True- Result like that 
=VLOOKUP(103,A2:B26,2,FALSE)

Common VLOOKUP Errors 
- Vlookup only returns the data to the right. SO you can do is keep your main search to the extreme left.
- =VLOOKUP(A2,'Employee Rates'!$A1:$B5,2,FALSE) USe absolute values $.
- Protect your primary key. The key that you use for matching we can protect by nmoy giving the access to everyone. DATA -> Sheets and range-> Access 
- Use False.

Creating a Pivot Table 
=VLOOKUP(A2,Sheet2!$A$2:$D$6,4,FALSE)
Then amrk all the values 
Insert pivot table- Add rows - Then add values in these rows 

