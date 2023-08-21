loaded_packages <- search ()
install.packages("ggplot2")
install.packages("palmerpenguins")
install.packages("tidyverse")

library(ggplot2)
library(palmerpenguins)
library(tidyverse)

ggplot(data = penguins) + geom_smooth(mapping = aes(x= flipper_length_mm, y= body_mass_g))+ 
  geom_point(mapping = aes(x= flipper_length_mm, y= body_mass_g))

ggplot(data = penguins) + geom_smooth(mapping = aes(x= flipper_length_mm, y= body_mass_g, linetype = species))

ggplot(data = diamonds) +geom_bar(aes(x=cut))
view(diamonds) 
ggplot(data = diamonds) + geom_smooth(mapping = aes (x=price,y=carat, color = cut))

