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

Errors 
Div0!
#Error! - Parsing error (Look for missing indents)
#NA! = Data does not exist (Look for spelling mistakes)
#NAME! = function names or general mistakes in formulae 
#Value! = Type error 
#Ref! - Missing values. (Always better to us efunctions )