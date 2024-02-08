Here Package - Makes it easier to reference packages 
skimr and janitor - Theya re both used for data cleaning operations 

install.packages("here")
library(here)
install.packages("skimr")
library(skimr)
install.packages("janitor")
library(janitor)
library(dplyr)

head()
glimpse()

> skim_without_charts(penguins)

1. 
select() - To select a specific column 
penguins %>%
    select(-species) # The - sign will remove a specific column

1. rename()
penguins %>%
    rename(new value = old value) updating a column name 

1. rename_with
penguins%>%
  rename_with(tolower)

1. clean_names (penguins) -Cleans the headers 
________________________________________________________________________________________________________________________________________________________

Other importatnt opertaors 
%% - Modulus
%/% integer value after division 
^ To the power of 

Logical 
& - Element-wise logical AND
&& - Logical AND
| - Element-wise logical OR
|| - Logical OR 
! - Logical NOT

The main difference between element-wise logical operators (&, |) and logical operators (&&, ||) is the way they apply to operations with vectors. The operations with double signs, AND (&&) and logical OR (||), only examine the first element of each vector. The operations with single signs, AND (&) and OR (|), examine all the elements of each vector. 
________________________________________________________________________________________________________________________________________________________

Organize the data 
arrange()
groupby()
filter

Summarise() - This is generally used with a nested function to give a high level view of the O/P
- Average bill lenght
penguins%>% group_by(island)%>% drop_na() %>% summarize(mean_bill_length_mm = mean(bill_length_mm))
- Max Bill lenght
penguins%>% group_by(island)%>% drop_na() %>% summarize(avg_bill_length_mm = average(bill_length_mm))

penguins%>% group_by(species,island)%>% 
  drop_na() %>% 
  summarize(mean_bill_length_mm = mean(bill_length_mm),max_bill_length_mm = max(bill_length_mm))

penguins%>%filter(species == "Adelie")
________________________________________________________________________________________________________________________________________________________

Transforming the Data 
1. seperate() - SPlit
separate(employee,name,into = c("first_name","last_name"), ' ')
separate(employee,name,into = c("first_name","last_name"), sep = ' ')

2. unite() - Concat
unite(employee,'empl_id', id, name, sep = '-')

3. mutate - Adding a new column
new_column <- penguins%>%
  mutate(weight_in_kg = body_mass_g/1000, add new columns )%>%
  drop_na()
print(new_column)

4.  arrange(bill_length_mm) - Arranging in ascending order 
