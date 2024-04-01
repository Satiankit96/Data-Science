import pandas as pd
import numpy as np
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
# df = pd.read_csv(url) # This  Assumes that we have an header. In our case we need to do this.
df = pd.read_csv(url, header=None)


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
# drive_wheels_count = df["drive-wheels"].value_counts()
# drive_wheels_count.rename(colunms={'drive-wheels':'value_counts'})

# new_wheels = drive_wheels_count.index.name = 'drive-wheels'
# print(new_wheels)

# Making Pivot tables 

df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(grouped_test1)