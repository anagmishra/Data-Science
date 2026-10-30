import numpy as np
#Numpy stands for numerical python which is an open source library used for numerical computing and scientific calculations. 
#It provides fast operations on large datasets using multi-dimensional arrays.
a = np.array([1, 2, 3, 4])
print(a)
print(type(a))
print(a*2)
#Doing mathematical operation in an array is far more easrier than that in a list.
#Multidimensional array:
a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a1.shape)

a2 = np.zeros((4, 5))
print(a2)
a3 = np.ones((3, 3))
print(a3)
a4 = np.arange(20).reshape(4, 5)
print(a4)
print("Dimensions", a2.ndim)
print("Shape", a2.shape)
print("Total elements", a2.size)
print("Memory", a2.nbytes)
print("Data Type", a2.dtype)
print("\n")

print("Dimensions", a3.ndim)
print("Shape", a3.shape)
print("Total elements", a3.size)
print("Memory", a3.nbytes)
print("\n")

print("Dimensions", a4.ndim)
print("Shape", a4.shape)
print("Total elements", a4.size)
print("Memory", a4.nbytes)
print("\n")

print(np.mean(a4))
print(np.sum(a4))
print(np.max(a4))
print(np.min(a4))
print(np.sqrt(a4))

a5 = np.array([1, 2, 3, 4])
a5.reshape((2, 2))
print(a5)

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print(np.dot(m1, m2))

# Conditional Selection of Elements
a6 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
evenarray = a6[a6%2==0]
print(evenarray)

boolarray = a6[a6==5]
print(boolarray)

print(a6[[2, 4, 6]])

m3 = np.random.permutation(np.arange(16)).reshape(4, 4)
m4 = np.random.permutation(np.arange(16)).reshape(4,4)
print(m3)
print(m4)
print(m3+m4)

def solve(k):
    return 2*k+3

x = np.array([1, 2, 3, 4, 5])
y = solve(x)
print(y)