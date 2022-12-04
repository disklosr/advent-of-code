import numpy as np
from tqdm import tqdm

line = open('input.txt')
line = next(line).strip()

arr = [int(age) for age in line.split(',')]

for k in tqdm(range(80)):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] -= 1
        else:
            arr[i] = 6
            arr.append(8)

print(len(arr))

