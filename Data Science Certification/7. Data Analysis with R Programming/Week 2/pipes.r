#Calculations
sales_1 <- 8000
sales_2 <- 8000
total <- sales_1 + sales_2
total
sum(sales_2,sales_1)
library(tidyverse)
data("ToothGrowth")
View(ToothGrowth)
install.packages("dplyr")

filtered_tg <- filter(ToothGrowth,dose ==0.5)
View (filtered_tg)
arrange(filtered_tg,len)

#Nested function 
arrange(filter(ToothGrowth,dose==0.5),len)

#Pipes 
filtered_toothgrowth <- ToothGrowth %>%
  filter(dose==0.5)%>%
  group_by(supp)%>%
  summarize(mean_len = mean(len,na.rm = T), .group="drop")

View (filtered_toothgrowth)
