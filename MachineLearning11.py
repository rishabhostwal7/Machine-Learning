import numpy as np
n4 = np.array( [10, -1, 0, 90, 300, 3, -6, 2])

print(n4)
n4.sort()
print("After n4.sort() : ", n4)

n4 = np.array([10, -1, 0, 90, 300, 3, -6, 2])

print("n4 = ", n4)
print("n4.argsort(): ", n4.argsort())
print("n4 = ", n4)

for i in n4.argsort():
    print(n4[i], end = " ")