import numpy as np
'''na = np.array( [ [1, 2, 3], [4, 5, 6] ] )

print("na = ", na)
print("na.transpose() = ", na.transpose())
print("na = ", na)
print("np.eye() = ", np.eye(6))

a = np.ones( [3,3] )
a=a*3
a[2,2] = 4
I=np.eye(3)
b=np.dot(a,I)
print(a)
print("\n")
print(I)
print("\n")
print(b)
'''
na = np.array( [ [1,2],
                 [5,6] ] )

print("na = ", na)
print("-"*15)
print("np.dot(na, na = \n", np.dot(na, na))