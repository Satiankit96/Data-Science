# https://www.coursera.org/learn/data-analysis-with-python/ungradedWidget/xZKrQ/module-2-cheat-sheet-data-wrangling
# 1. Dealing with missing values
# Could be represented as "", NaN, 0

import pandas as pd
import numpy as np
import matplotlib.pylab as plt


# Axis = 0 means the row
# Using inplace changes the df 
print(df.dropna(subset=["price"], axis=0, inplace = True ))

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)

# Finding Missing Data 
missing_data = df.isnull()
missing_data.head(5)

# Replacing the values with averages 
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

# Replacing Nan with average 
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

# Binning 