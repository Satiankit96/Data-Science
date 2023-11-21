# Importing Data with pandas
# Two Things to keep in mind
# 1. Format 
# 2. Path

import pandas as pd
import numpy as np
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
# df = pd.read_csv(url) # This  Assumes that we have an header. In our case we need to do this.
df = pd.read_csv(url, header=None)
print(df.head(5))
print(df.tail(5))

# Setting the headers in our case 
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print(headers)
df.columns = headers
print(df.head(5))

df1=df.replace('?', np.NaN) 


# In pandas axis = 0 refers to horizontal axis or rows and axis = 1 refers to vertical axis or columns.

df=df1.dropna(subset=["price"], axis=0)
df.head(20)
print(df.head(5))
print(df.describe())

# Specific columns 
print(df[['length', 'compression-ratio']].describe())

df.info()
# Pandas Cheat sheet 
# https://www.coursera.org/learn/data-analysis-with-python/ungradedWidget/cp3Fx/module-1-cheat-sheet-importing-data-sets