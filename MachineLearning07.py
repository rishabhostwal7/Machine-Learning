import numpy as np

print("--------------------------------------")
ddarr = np.array( [ [1, 2, 3], [4, 5, 6] ])

print("ddarr.ndim = ", ddarr.ndim)
print("ddarr.shape = ", ddarr.shape)    # Anser of shpae will always comes in round braces ie tuples
print("ddarr.size = ", ddarr.size)
print("ddarr.dtype = ", ddarr.dtype)
print(ddarr)

print("********************************************")
print("ddarr[0,1]", ddarr[0,1])
print("ddarr[0]", ddarr[0])
print("ddarr[: , 0]", ddarr[:, 0])
print("ddarr[1, :]", ddarr[1, :])
