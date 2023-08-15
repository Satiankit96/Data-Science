Fundamentals in R
Functions - Same as any 
Comments - Same 
Variables - Same, also called objects
Data types - Same 
Vectors - A group of data elements of the same type stored in a sequence in R 
Pipes - Used to combine multiple functions. Sequence of multiple operations. "%>%"


Variable declation 
x <- 50 (50 assigns to X )

Vector Declation 
vec_1 <- c(13,48.71,101.5,2)
c() - Combine function. (This one is more like a list )

Pipes Declation - Its more like calling a function on another rather than a function within a function 
Toothgroqth %>% filter(dose == 0.5) %>% arrange(len)


Data structures in R 
Vectors - There are a total of 6 atomic vectors.
Logical 
Integer - c(1L, 5L, 15L)
Double - Floats
Character - Strings
Complex 
Raw

Lists - Used to store multiple data types

Working with date and time
library(tidyverse)
library(lubridate)

today() - date
now() - date and time

1. defining your format - The output format will always remain the same 
   
dmy("20-Jan-2021")
#> [1] "2021-01-20"

ymd(20210120)
#> [1] "2021-01-20"

mdy_hm("01/20/2021 08:01")
#> [1] "2021-01-20 08:01:00 UTC"


More data structures 
1. Data frames - Used to store columns similar to a spreadsheet
First, columns should be named. 
Second, data frames can include many different types of data, like numeric, logical, or character.
Finally, elements in the same column should be of the same type.

The data.frame() function takes vectors as input.
data.frame(x = c(1, 2, 3) , y = c(1.5, 5.5, 7.5))
X and Y are the column names 

2. Files
dir.create(""name)
filr.create("name.csv/docs/txt")

Deleting a file 
unlink (“some_.file.csv”)

