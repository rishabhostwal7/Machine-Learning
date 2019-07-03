import numpy as np
a = np.array( [1,2,3,4] )
print("a+1 = ", a+1)
print("a = ", a)
print("a**2", a**2)

# aLL arithmetic operates elementwise
a = np.array([1,2,3,4])
b = np.ones(4) + 1
print(a)
print(b)
print("a-b : ", a-b)    # Element by element broadcasting
print("a*b : ", a*b)    # Element by element broadcasting

j=np.arange(5)
print( 2**(j+1)-j)