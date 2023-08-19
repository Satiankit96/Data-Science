id <- c(1:10)

name <- c("John Mendes", "Rob Stewart", "Rachel Abrahamson", "Christy Hickman", "Johnson Harper", "Candace Miller", "Carlson Landy", "Pansy Jordan", "Darius Berry", "Claudia Garcia")

job_title <- c("Professional", "Programmer", "Management", "Clerical", "Developer", "Programmer", "Management", "Clerical", "Developer", "Programmer")

employee <- data.frame(id, name, job_title)

print(employee)

#separate function - SPLIT the column 
separate(employee,name,into = c("first_name","last_name"), ' ')

#unite function () - Concate

print(employee)

unite(employee,'empl_id', id, name, sep = '-')

new_column <- penguins%>%
  mutate(weight_in_kg = body_mass_g/1000)%>%
  drop_na()
print(new_column)


penguins%>% group_by(island)%>% drop_na() %>% summarize(avg_bill_length_mm = min(bill_length_mm))

penguins%>%
print(penguins)
