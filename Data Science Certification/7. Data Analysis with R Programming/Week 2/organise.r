install.packages("here")
library(here)
install.packages("skimr")
library(skimr)
install.packages("janitor")
library(janitor)
library(dplyr)

install.packages("palmerpenguins")
skim_without_charts(penguins)
penguins%>%
  rename_with(tolower)

#Data Organisation 
penguins %>% 
  arrange(bill_length_mm)#ASC ORDER, (-columns_name) FOR DESCENDING ORDER
# To save the above output 
penuins_view_1 <- penguins %>% 
  arrange(bill_length_mm)
View(penuins_view_1)

#Summarize - lets us get the high level information 
penguins%>% group_by(island)%>% drop_na() %>% summarize(mean_bil_mm = mean(bill_length_mm))
penguins%>% group_by(island)%>% drop_na() %>% summarize(max_bill_mm = max(bill_length_mm))

penguins%>% group_by(species,island)%>% 
  drop_na() %>% 
  summarize(mean_bill_length_mm = mean(bill_length_mm),max_bill_length_mm = max(bill_length_mm))

penguins%>%filter(species == "Adelie")
