Cleaning data in spreadsheets 
1. Conditional formatting - Use This after setting up the formula. This will highlight the results quicker
2. Remove duplicate - Data > Data cleanup > RM duplicate 
3. date - select column - formatting - Number - date 
4. Split - select column - data - split (This can also resolve errors between numbers and text)

Deliminitor - ENd of the data column 
5. =COUNTIF(B2:B71, "!=6")
6. =LEN(A71)
7. =Left(A2,5) (5 from left)
8. =Right(A2,4)
9. =MID(Column Name, Starting letter, number of middle elements)
=MID(D2,4,2)
10. =CONCATENATE(H2," ",I2)//Better Practice 
11. TRIM (LTRIM,RTRIM)

_________________________________________________________________________________________
Workflow automation 
This means to automate some parts of the program using scripts. 
We have already done something similar 

_________________________________________________________________________________________

Different data perspectives 
1. Sorting and filtering - ALready gone over them 
2. Pivot Tables 
   Select Data - Insert - Pivot Tables 
   Add from Row, and set order 
   Keep adding entities that are needed 

3. VLOOKUP - This function is made to look for some values that might reside in some other table/sheet. Vertical look up
   =VLOOKUP(Cell whose value we want to look up, 'Sheet where that value resides' !(A1:b31 RAnge in that sheet),Column where the needed value resides,False(For an exact match ))
   =VLOOKUP(A2,'Sheet2'!A1:B31,2,false) 

4. Plotting - Visual aid
   - Select row - Plot a column chart - Look for anamolies 

_________________________________________________________________________________________

More Data Cleaning 
Data Mapping - How the data is moved within an organisation. This helps us with many aspects and what needs to be moved. 
Schema - The way of describing how something is organized 