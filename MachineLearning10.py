import numpy as np
arr = np.array( [11, 22, 33, 0., 44, 55] )

print("arr.sum() = ", arr.sum())
print("arr.std() = ", arr.std())
print("arr.mean() = ", arr.mean())
print("arr.max() = ", arr.max())
print("arr.min() = ", arr.min())
print("arr.size = ", arr.size)      # rest all sum(),astd() etc.. are functions but size is an attribute

# following line will print ( index of non zero)
print("arr.nonzero() = ", arr.nonzero())
print("arr.dtype = ", arr.dtype)

# Are all elements greater than zero
print( np.all( [1,2,3,4] ))     # are all the values non-zero    Ans= True
print( np.all( [1,2,0,3,4] ))   # are all the values non zero    Ans= False

# is any elements greater than zero
print( np.any( [1,2,3,4] ))     # True
print( np.any( [1,2,0,3,4] ))   # True
print( np.any( [0,0,0.,0,0] ))  # False
print( np.any( [0,0,0,0.,0,1])) # True

n1 = np.array([4,5,6])
n2 = np.array([1,2,3])

print("\n\n")
print("n1 = ", n1)
print("n2 = ", n2)
print("n1 + n2 = ", n1+n2)
print("n1 - n2 = ", n1-n2)

'''n3 = np.array([4,5,6,7])
print(n1 + n3)'''

