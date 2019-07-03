import numpy as np
zr = np.zeros( [3,4] )
print("Zero filled array zr = \n", zr)

ar = np.ones([4,4])
print("1's filled array ones = \n", ar)

print(ar*4)

print(ar.dtype)

# We can create numpy array from range
ar = np.arange(1,6)
print("ar = ", ar)
ar[3] = 16
print("ar = ", ar)
