import numpy as np
from itertools import product, count

arr = np.genfromtxt('input.txt', dtype='i', delimiter=[1]*10)
shape = arr.shape
current_step = 0
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def around(pos, arr, distance = 1, diagonal = True):
    for i in range(0-distance, 1+distance):
        for j in range(0-distance, 1+distance):
            if 0 <= pos[0] + i < arr.shape[0] and 0 <= pos[1] + j < arr.shape[1] and (i,j) != (0,0) and (diagonal == True or i != j):
                yield (pos[0] + i, pos[1] + j)


print(list(around((5, 5), arr)))

for steps in range(1000):
    current_step += 1    
    arr += 1
    while (arr == 10).any():
        for i in product(range(shape[0]), range(shape[1])):
            if arr[i] == 10:
                arr[i] += 1
                for t in around(i, arr):
                    if arr[t] <= 9:
                        arr[t] += 1
    for i in product(range(shape[0]), range(shape[1])):
        if arr[i] > 10:
            arr[i] = 0
    
    if (arr == 0).all():
        break

print(current_step)
            