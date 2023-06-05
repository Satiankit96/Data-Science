Formulas - set of instructions to perform calculations. (begin with = )
Operators - Mathematical
Cell refference - Specific cell 
Range - This is a range of rows, columns or cells.

Any change in data will automatically update in the formula

Absolute referencing
These are the references to the cells whose values you do not want to change.
The autofill function will work on a fixed cell.
f2 / %f%8 - THE $ MARK WILL REMAIN CONSTANT.

Various functions 
COUNTIF(A1:A16,"7") - This counts the cells from A1 to A 16 and highlights the one that has the number 7 in them  
DATEDIF(B2,B4."D") - This tells the difference between the dates. (d - days, m - months, y - years)

Errors - 
1. https://www.benlcollins.com/spreadsheets/formula-parse-error/
2. https://support.microsoft.com/en-us/office/formulas-and-functions-294d9486-b332-48ed-b489-abe7d0f9eda9?ui=en-US&rs=en-US&ad=US#id0eaabaaa=errors
Div0!
#Error! - Parsing error (Look for missing indents)
#NA! = Data does not exist (Look for spelling mistakes)
#NAME! = function names or general mistakes in formulae 
#Value! = Type error 
#Ref! - Missing values. (Always better to us efunctions )

Error | Description | Example
--- | --- | --- 
#DIV/0! | A formula is trying to divide a value in a cell by 0 (or an empty cell with no value) | =B2/B3, when the cell B3 contains the value 0 
#ERROR! | (Google Sheets only)  Something can’t be interpreted as it has been input. This is also known as a parsing error. | =COUNT(B1:D1 C1:C10) is invalid because the cell ranges aren't separated by a comma
#N/A | A formula can't find the data | The cell being referenced can't be found 
#NAME? | The name of a formula or function used isn't recognized | The name of a function is misspelled 
#NUM! | The spreadsheet can't perform a formula calculation because a cell has an invalid numeric value | =DATEDIF(A4, B4, "M")  is unable to calculate the number of months between two dates because the date in cell A4 falls after the date in cell B4
#REF! | A formula is referencing a cell that isn't valid | A cell used in a formula was in a column that was deleted
#VALUE! | A general error indicating a problem with a formula or with referenced cells | There could be problems with spaces or text, or with referenced cells in a formula; you may have additional work to find the source of the problem.

Test score - 100