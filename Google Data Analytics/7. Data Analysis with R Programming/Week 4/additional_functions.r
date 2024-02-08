#Facets 

ggplot(data = penguins) + geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color = "red"))+
  facet_wrap(~species)

ggplot(data = diamonds) + geom_bar(mapping = aes(x=cut),color = cut)

ggplot(data = penguins) + geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color = species))+
  facet_grid(sex~species)

