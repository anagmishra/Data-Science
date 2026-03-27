import numpy as np
a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a2 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
l3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a1 *= 5
l = l1 * 5
a = a1+a2
l4 = l1+l2
for i in range(len(l1)-1):
    l3[i] = l1[i] + l2[i]
    l5[i] = l1[i] * 5
    i+=1

print(a1)
print(l)
print(a)
print(l4)
print(l3)
print(l5)
