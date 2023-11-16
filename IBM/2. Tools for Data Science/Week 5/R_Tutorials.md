File 1 
x <- 10
y <- 20
result <- y-x
print(result)


File 2 (Plots)


File 3 
library(datasets)
data(mtcars)
head(mtcars,5)
tail(mtcars,10)
?mtcars - To get the information on the data 

library(datasets)
data(mtcars)
head(mtcars,5)
tail(mtcars,10)
?mtcars

library(ggplot2)

ggplot(aes(x=disp,y=mpg,),data=mtcars)+geom_point()+ggtitle("displacement vs miles per gallon")
mtcars$vs <- as.factor(mtcars$vs)
ggplot(aes(x=vs, y=mpg), data = mtcars) + geom_boxplot()

ggplot(aes(x=vs, y=mpg, fill = vs), data = mtcars) + 
  geom_boxplot(alpha=0.3) +
  theme(legend.position="none")
ggplot(aes(x=wt),data=mtcars) + geom_histogram(binwidth=0.5)
