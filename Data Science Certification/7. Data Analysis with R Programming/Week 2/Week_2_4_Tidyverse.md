- ggplot2 - Visualisations. Various plots 
- tidyr - Data cleaning. Every part of data is cleaned 
- readr - This is to import the CSV file. 
- dplyr - data manupulations. Selecting variables, Finding filters

Other 4 packages 
tibble - works with data frames 
Purr - Works with functions and vectors and makes code more easier to write 
Stringr - Working with string 
Forcats - Works on Factors *(Data is organised within a group )

Pipes - These are functions called upon functions that make the code more readable.
%>%

filtered_tg <- filter(ToothGrowth,dose ==0.5)
View (filtered_tg)
arrange(filtered_tg,len)

#Nested function 
arrange(filter(ToothGrowth,dose==0.5),len)

#Pipes 
filtered_toothgrowth <- ToothGrowth %>%
  filter(dose==0.5)%>%
  arrange(len)
view(filtered_toothgrowth)

2. Summarize and mean function  
filtered_toothgrowth <- ToothGrowth %>%
  filter(dose==0.5)%>%
  group_by(supp)%>%
  summarize(mean_len = mean(len,na.rm = T), .group="drop")

View (filtered_toothgrowth)
