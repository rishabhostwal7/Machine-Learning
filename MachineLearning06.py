"""list1 = [1, 2, 3]
print("list1 * 4 : ", list1*4)"""
# basic array do not support operation broadcasting so to solve this problem we use numpy array as

import numpy as np
nparr = np.array([1, 2, 3])
print(nparr)
"""print("nparr * 4 : ", nparr*4)
print("nparr + 4 : ", nparr+4)
print("nparr / 2 : ", nparr/2)
print("nparr / 2.0 : ", nparr/2.0)
print("nparr // 2.0 : ", nparr//2.0)
print("nparr // 2: ", nparr//2)
"""
a=10
print(type(a))
a=12.5
print((type(a)))

print(type(nparr))
print("nparr.dtype = ", nparr.dtype)

print("nparr.size = ", nparr.size)

# What is numpy ? numpy is an n-dimensional array