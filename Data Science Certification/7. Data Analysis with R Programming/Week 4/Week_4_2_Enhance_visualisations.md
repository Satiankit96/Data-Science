ggplot(data = penguins) + geom_point(mapping = aes(x= flipper_length_mm, y= body_mass_g,color = species,shape = species, size = species))

Multi mapping 
color = species,shape = species, size = species
color = "red" (Every value goes the s[ecific color ])
alpha (Changes the denceness of a point)

Multiple Geoms 
ggplot(data = penguins) + geom_smooth(mapping = aes(x= flipper_length_mm, y= body_mass_g))+ 
  geom_point(mapping = aes(x= flipper_length_mm, y= body_mass_g))

Multiple line graphs 
ggplot(data = penguins) + geom_smooth(mapping = aes(x= flipper_length_mm, y= body_mass_g), linetype = species )

jitter - makes it easier to read the sctterplot 
ggplot(data = penguins) + geom_jitter(mapping = aes(x= flipper_length_mm, y= body_mass_g), linetype = species )
________________________________________________________________________________________________________________________________________________________________
Facet Functions 
They are used to show the subsets of the data 
1. facet_wrap()
2. facet_grid()

Wrap - Separate plot for each function
ggplot(data = penguins) + geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color = species))+
  facet_wrap(~species)

Grid - This is used to dicide a subset accross 2 further parameters. facet_grid(sex~species)(y,x)
ggplot(data = penguins) + geom_point(mapping = aes(x=flipper_length_mm,y=body_mass_g,color = species))+
  facet_grid(sex~species)
________________________________________________________________________________________________________________________________________________________________

Annotation Layers 

Addding notes to a Diagram or an document
label() - Used to add titles, sub titles and Captions
ggplot(data = diamonds) + geom_bar(mapping = aes(x=color,fill = cut)) +
  facet_wrap(~cut)+labs(title = "The Various cuts of diamonds", subtitle = "Whatever",caption = "Null use data")

Annotate 
Writting data to add more context some whew on the screen 