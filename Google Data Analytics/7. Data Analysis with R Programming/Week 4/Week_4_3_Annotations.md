Annotation Layers 

Addding notes to a Diagram or an document
label() - Used to add titles, sub titles and Captions
ggplot(data = diamonds) + geom_bar(mapping = aes(x=color,fill = cut)) +
  facet_wrap(~cut)+labs(title = "The Various cuts of diamonds", subtitle = "Whatever",caption = "Null use data")

Annotate 
Writting data to add more context some whew on the screen 

Exporting the final visualisations 
ggsave()