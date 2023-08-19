install.packages("Tmisc")
library(Tmisc)
data("quartet")
View(quartet)

quartet%>%
  group_by(set)%>%
  summarise(mean(x),sd(x),mean(y),sd(y),cor(x,y))
# A tibble: 4 × 6
  set   `mean(x)` `sd(x)` `mean(y)` `sd(y)` `cor(x, y)`
  <fct>     <dbl>   <dbl>     <dbl>   <dbl>       <dbl>
1 I             9    3.32      7.50    2.03       0.816
2 II            9    3.32      7.50    2.03       0.816
3 III           9    3.32      7.5     2.03       0.816
4 IV            9    3.32      7.50    2.03       0.817

Bias function in R 
Close to 0 is a good data 

bias(clolumn_1,column_2)
0 - Good 
-number_big  - Over 
+Giant - under 