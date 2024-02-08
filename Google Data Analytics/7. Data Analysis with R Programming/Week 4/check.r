install.packages("palmerpenguins")
install.packages("ggplot2")
install.packages("tidyverse")
loaded_packages <- search()
library(palmerpenguins)
library(ggplot2)
library(tidyverse)

ggplot (data = penguins) + geom_point(mapping = aes(x= flipper_length_mm, y= body_mass_g))

ggplot(data = penguins) + geom_point(mapping = aes(x= bill_length_mm, y= bill_depth_mm))

