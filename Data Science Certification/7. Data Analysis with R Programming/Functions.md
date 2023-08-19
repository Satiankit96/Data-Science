library(package) - Everytime we need to use a package we need to load it to the worspace
#Comment
?functionname() - This will share some help if we know some relative funtion iof other language and will try to find an alternative in R.

print("")
summary(penguins) - Summary about the Package
typeof(x)
length(x) - Len of a list 
is.logical(), is.double(), is.integer(), is.character() - Boolean check
as.logical(), as.integer(), as.double(), or as.character() - Type conversion

names (x) <- c("a","b","c") (if we are missing a value it would be represented by NA, however the opposite will throw an error)
str(z) - This will be used to see the structures and the types of elements a list has. $ represents a nested list

data("ToothGrowth") - Loading a data set 
View(ToothGrowth) -Viewing the dataset 

Capitals
View(penguins) - Views the contents of the Package

Package 
1. dplyr
filter -    filtered_tg <- filter(ToothGrowth,dose ==0.5)
arrange(filtered_tg,len)

