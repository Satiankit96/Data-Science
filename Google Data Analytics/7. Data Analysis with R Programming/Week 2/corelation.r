install.packages("Tmisc")
library(Tmisc)
data("quartet")
View(quartet)

quartet%>%
  group_by(set)%>%
  summarise(mean(x),sd(x),mean(y),sd(y),cor(x,y))

penguins%>%
  filter(island != "Torgersen")
