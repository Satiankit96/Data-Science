ggplot2 - Grammar of Graphics 
Used to create multiple types of plots 

Key components 
- Aesthetics - Visual property of the plot
- Geoms - Geometric Object to show our analysis 
- Facets - Lets us discuss the small groups and 
- Labels and annotations

ggplot(data = penguins)
We always begin with the ggplot() function. It loads the data and adds an coordinate system for our analysis.
+ <- This lets us add an extra layer to our analysis.   For a complex visual, at times we might need more than one layer.
geom_point - This is used to create scatterplots. The general sysntax in the end.
geom_bar - For bar graph and so on 

aes(x= flipper_length_mm, y= body_mass_g)
Aes tells us about the value of a point over the graph in our x:y coordinate system 

3 step rule 
- start with the ggplot() and choose a dataset to work with 
- Add a geom_functionname to display your data 
- map the coordinates to the parts you want to check in the aes finction 
  
ggplot(data = penguins) + geom_point(mapping = aes(x= flipper_length_mm, y= body_mass_g))

ggplot(data = penguins) + geom_point(mapping = aes(x= bill_length_mm, y= bill_depth_mm))
