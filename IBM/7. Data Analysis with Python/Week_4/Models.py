import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.sparse.linalg import lsqr as sparse_lsqr
from sklearn.linear_model import LinearRegression


url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
# df = pd.read_csv(url) # This  Assumes that we have an header. In our case we need to do this.
df = pd.read_csv(url, header=None)
# print(df.head(5))
# print(df.tail(5))

# Setting the headers in our case 
headers = ["symboling","normalized_losses","make","fuel_type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb_weight","engine-type",
         "num_of_cylinders", "engine_size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city_mpg","highway_mpg","price"]
print(headers)
df.columns = headers
df1=df.replace('?', np.NaN) 
newdf = df1.dropna()

sns.regplot(x="horsepower", y="price", data = newdf)

# lm = LinearRegression()

# X= newdf[['highway-mpg', 'curb_weight', 'engine_size','horsepower']]
# lm.fit(X,newdf['prize'])
# Yhat=lm.predict(X)
# print(Yhat)
# df_sorted = newdf.sort_values(by = ["fuel_type", "price"], ascending= [True,True])
# if ("fuel_type" == "diesel"):
#     print(df_sorted.head(100))
# print(df_sorted)

# plt.scatter(df.highway_mpg, df.price)
# plt.scatter(df.city_mpg, df.price)
# plt.scatter(df.highway_mpg,df.price, color = "Black")
# plt.scatter(df.city_mpg,df.price, color = "Blue")

# plt.show()

# def gradient_descent(m_now, b_now, points, Learn):
#     m_gradient =0
#     b_gradient =0

#     n = len(points)

#     for i in range (n):
#         x = points.iloc[i].horsepower
#         y = points.iloc[i].price

#         m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
#         b_gradient += -(2/n) * (y - (m_now * x + b_now))

#     m = m_now - m_gradient * Learn
#     b = b_now - b_gradient * Learn

#     return m,b

# m = 0 
# b = 0
# Learn = 1
# epochs = 200

# for i in range(epochs):
#     if i % 50 == 0:
#         print(f"epoch{i}")
#     m,b = gradient_descent(m,b,df, Learn)

# print(m,b)
# plt.scatter(df.horsepower,df.price, color = "pink")
# plt.plot(list(range(20,80)), [m*x+b for x in range (20,80)], color = "Green")
# plt.show()