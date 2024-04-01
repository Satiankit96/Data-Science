import numpy as np 
import matplotlib.pyplot as plt
a = np.array([1,2,3,4,56], dtype ='int')
print(a)

b = np.random.rand(4,2)
print(b)
print(b.dtype)

b = np.array([2.3,4.5,7.8])
print(b.dtype)

# Vector addition 
u = [23,23]
v = [0,1]
z = []
for n,m in zip(u,v):
    z.append(n+m)
print(z)

# same in numPy
u = np.array([1,2])
v = np.array([0,2])
print(u+v)

print(np.dot(u,v))

# Linespace 
# Equally spaced numbers in a given space 
print (np.linspace(-2, 2, num=10))

x = np.linspace(0,2*np.pi, 100)
y = np.sin(x)

plt.plot(x,y)

# 2D Arrays 
a=np.array([-1,1])
b=np.array([1,1])
print(np.dot(a,b)) 
# https://www.coursera.org/learn/python-for-applied-data-science-ai/ungradedWidget/Pm4xn/cheat-sheet-working-with-data-in-python
a=np.array([[1,0,1],[2,2,2]]) 
out=a[0:2,2]
print(out)

X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
print(np.dot(X,Y))