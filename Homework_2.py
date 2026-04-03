import numpy as np

a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(a1[0:5])
print(a1[15:20])
print(a1[::3])
print(a1[-1:-21:-1])

m1 = np.arange(49).reshape(7,7)
m2 = m1[2:5, 2:5]
m3 = m1[0, :]
m4 = m1[ :, 6]
print(m1)
print(m2)
print(m3)
print(m4)

a2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(a2[a2<8])
print(a2[a2>=10])
print(a2[a2%2==1])

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for i in range(len(l1)):
    l1[i] = l1[i] + 5
    i+=1
print(a3+5)
print(l1)
print(a3*3)
print(a3-2)

m5 = np.random.permutation(np.arange(9)).reshape(3, 3)
m6 = np.random.permutation(np.arange(9)).reshape(3, 3)
print(m5)
print(m6)
print(m5*m6)
print(np.dot(m5, m6))