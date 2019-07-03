import numpy as np
'''print("--Transcendental functions:---")
a=np.arange(0,6)

print(np.sin(a))
print(np.log(a))
print(np.exp(a))

# Shape mismatches : ERROR

a = np.arange(4)
# print(a + np.array([1,2]))  # ERROR
'''

x=np.array([1,2,3,4])
print("np.sum(x) : ", np.sum(x))
print("x.sum() : ", x.sum())

print("---Sum by rows and by columns:---")
x=np.array( [ [1,2], [3,4] ] )
print("x = \n", x)

# array( [ [1,2],
#          [3,4] ] )

print(x.sum())
print(x.sum(axis=0))    #  columns(first dimension)  "Not Compulsory"

# array( [4,6] )

print(x[:,0].sum(), x[:,1].sum())
print(x.sum(axis=1))    # rows(first dimension)   "Not Compulsory"
print(x[0,:].sum(), x[1,:].sum())

print("---------------------Extrema:---------------------")
x=np.array([1,3,2])
print(x.min())  # 1
print(x.max())  # 3

# Logical Operations
print(np.all([True, True, False]))  #False
print(np.any([True,True,False]))    #True

print("Numpy can be used ofr array comparisions")
a=np.zeros((10,10))
print("a = ", a)
print(np.any(a!=0))
print(np.all(a==a))

print("-----------------Statistics-----------------")
x = np.array([1,2,3,1,1])

print("x.mean() = ", x.mean())
print("np.median(x) = ", np.median(x))
print("x.std() = ", x.std())        # Full Population

