import pandas as pd
import numpy as np
csv_path='file.csv'
df = pd.read_csv(csv_path)
df.head()# First 5 results 

#Unique
df['Released'].unique()
#Pandas
# https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstUFkwMTAxRU4tU2tpbGxzTmV0d29yay9sYWJzL2xhYi9tb2R1bGVfNC93cml0ZV9maWxlX3dpdGhfb3Blbl9yZWFkaW5nLm1kIiwidG9vbF90eXBlIjoiaW5zdHJ1Y3Rpb25hbC1sYWIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTY5Njk3NDcxOH0.pAbY0tXv6dgSlWceY5r3HKXG_AMos8CWeYWfmCZ_CzA
# iloc - index location
# loc - value location

