import numpy as np
from itertools import product

arr = np.genfromtxt('input.txt', dtype='i', delimiter=[1]*10)
shape = arr.shape
flashed = 0

for steps in range(100):
    
    
    arr += 1
    while (arr == 10).any():
        for i in product(range(shape[0]), range(shape[1])):
            if arr[i] == 10:
                arr[i] += 1
                for t in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if 0 <= i[0] + t[0] < shape[0] and 0 <= i[1] + t[1] < shape[1]:
                        if arr[i[0] + t[0], i[1] + t[1]] <= 9:
                            arr[i[0] + t[0], i[1] + t[1]] += 1
    for i in product(range(shape[0]), range(shape[1])):
        if arr[i] > 10:
            arr[i] = 0
            flashed += 1

print(flashed)

            