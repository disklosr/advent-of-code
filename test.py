import numpy as np

a = np.zeros((5,5))
a[2,2] = 9
a[0,] = a[:,0] = a[-1,] = a[:,-1] = 1 
print(a)

print(a[a > 0])