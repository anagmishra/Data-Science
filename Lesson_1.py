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