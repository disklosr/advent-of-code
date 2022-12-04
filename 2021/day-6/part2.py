import numpy as np
from tqdm import tqdm

line = open('input.txt')
line = next(line).strip()

arr = [int(age) for age in line.split(',')]
m = {0: 0, 1: 0, 2:0, 3: 0, 4:0, 5:0, 6:0, 7:0, 8:0}
for age in arr:
    m[age] += 1

for k in range(256):
    m = {
        0: m[1] ,
        1: m[2],
        2: m[3],
        3: m[4],
        4: m[5],
        5: m[6],
        6: m[7] + m[0],
        7: m[8],
        8: m[0]
    }

print(sum(m.values()))
