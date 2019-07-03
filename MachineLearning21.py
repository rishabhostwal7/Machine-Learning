import numpy as np

n4 = np.array( [10,-1,0,90,300,3,-6,2] )
print(n4)

n4.sort()
print("After Sorting : ", n4)        # We will get the data in sorted but we will lose original data

n4 = np.array( [10,-1,0,90,300,3,-6,2] )

print("n4 = ", n4)
print("n4.argsort() = ", n4.argsort())
print("n4 = ", n4)

for i in n4.argsort():      # [6 1 2 7 5 0 3 4]
    print(n4[i], end = " ")

print("\n")
    # Shortest method
print(n4[n4.argsort()])