#Unique
# df['Released'].unique()
#Pandas
# https://author-ide.skills.network/render?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZF9pbnN0cnVjdGlvbnNfdXJsIjoiaHR0cHM6Ly9jZi1jb3Vyc2VzLWRhdGEuczMudXMuY2xvdWQtb2JqZWN0LXN0b3JhZ2UuYXBwZG9tYWluLmNsb3VkL0lCTURldmVsb3BlclNraWxsc05ldHdvcmstUFkwMTAxRU4tU2tpbGxzTmV0d29yay9sYWJzL2xhYi9tb2R1bGVfNC93cml0ZV9maWxlX3dpdGhfb3Blbl9yZWFkaW5nLm1kIiwidG9vbF90eXBlIjoiaW5zdHJ1Y3Rpb25hbC1sYWIiLCJhZG1pbiI6ZmFsc2UsImlhdCI6MTY5Njk3NDcxOH0.pAbY0tXv6dgSlWceY5r3HKXG_AMos8CWeYWfmCZ_CzA
# iloc - index location
# loc - value location

# Why Numpy over lists ?
# Faster than lists as it uses fixed data types.
# Lists uses a lot more information as compared to numpy.(Check type of each value in list)
# Numpy uses contiguous memory. Which means storage next to each other. (Lists uses a pointer to the memory)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a = np.array([1,2,3], dtype = 'int32') # To be more efficient it is always a good idea to mention the dtypes 
print(a)

b = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print(b)

# Printing the Dimensions 
print(a.ndim)

# Shape 
print(a.shape)
print(b.shape)
# type
print(a.dtype)

# Size 
print(a.itemsize)

# Number of elements in the array
print("Number of elemensts are", +a.size)

# Total Size (This is equal to number of bytes as well)
print (a.size * a.itemsize)

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a.shape)

# getting specific index [r,c]
print(a[1,5])

#Get a specific row 
print(a[0,:])

# Get a specific Column [3]
print(a[:,2])

# skipping the parts of the list [startindex:endindex:stepsize]
print(a[0,1:-1:2])

# changing the elements of the array 
a[1,2] = 69
print(a)

a[:,3] = [1,1]
print(a)


# Moving to the 3d arrays 
a = np.array([[[1,2],[3,4]],
              [[5,6],[7,8]]])
print(a)

# Accessing the elemets of the array - Move outside in 
print(a[1,0,0])

# Replacing a row

a[0,1,:] = [20,15]
print(a)  

# numbers 
a = np.ones((4,2,2),dtype='int32') 
print (a)

a = np.zeros((4,2,2),dtype='int32') 
print(a)

# Any other number np.full 
print(np.full((2,2),99))

# Random
print(np.random.random_sample(a.shape))

print(np.random.rand(4,2))

# ?Random integer value. max values up until 9. 
print(np.random.randint(9, size=(3,3)))

#  Copying an array 

a = [1,2,3]
# b = a
b = a.copy()
b[0] = 100
print(b)
print(a) 


# Mathematics

a = np.array([1,2,3,4])
# Arthematics are performed on each element 
print(a - 2)
print(a * 2)
print(a / 2)
b = np.array([1,0,1,0])
print(a + b)
print(a ** 2)

# Linear algebra 
## Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)


# Stats 
stats = np.array([[1,2,3],[4,5,6]])
np.min(stats)
np.max(stats, axis=1)
np.sum(stats, axis=0)


print (np.linspace(-2, 2, num=10))
x= 1
y = np.sin(x)
print(plt.plot(x, y))