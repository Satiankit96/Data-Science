R data frames 
This is a collection of columns 
- Columns should be named (as they will be used as variables in the code)
- data frames could have multiple data types 
- Each column should have the same number of data items ideally 

Tibbles - streamlined data frames 
- The data types of the inputs always remain constant 
- Never create variable names 
- pprinting is easier
   
library(tidyverse) 
data(diamonds)
as_tibble(diamonds)

- First 10 rows of the data appear and it is good to look at 


 Tidy data 
 Fitting the data to a standard 
 Columns - Variables 
 Rows - values 
 Celss - not null 

Other Basic operations 

