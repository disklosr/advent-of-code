import numpy as np


# create array of dimension n*m

res = np.zeros((15,15), dtype=int)

res = np.ones((15,15), dtype=int)

res = np.empty((2,3), dtype=int)

res = np.random.randint(100, size=(15,15))
print(res)

# Flatten array
res = np.arange(100)
res.resize((25,4)) #in place
res = res.reshape((25,4)) #doesn't change original array


# Iterate over all elements
res = np.arange(50).reshape((10,5))
[i for i in res.flat]

# flatten array
res = np.arange(50).reshape((10,5))
res.ravel()

# Get column

res = np.arange(50).reshape((10,5))
res[2:4,2:4] # lines 2 and 3 with columns 2 and 3

# Plot 3d array
from matplotlib import pyplot as plt
t = np.ones((5,5,5))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
z,x,y = t.nonzero()
ax.scatter(x, y, z, c=z, alpha=1)
plt.show()