import numpy as np
import math

lines = open('input.txt')
moves = []

for line in lines:
    (dir, count) = line.strip().split()
    moves += [dir for k in range(int(count))]

head = ((5,5))
tail = ((5,5))

res_set = set()
res_set.add(tail)

for m in moves:
    #move head
    if   m == 'R':
        head = (head[0], head[1] + 1)
    elif m == 'L':
        head = (head[0], head[1] - 1)
    elif m == 'U':
        head = (head[0] - 1, head[1])
    elif m == 'D':
        head = (head[0] + 1, head[1])

    #update tail
    dist_row = head[0] - tail[0]
    dist_col = head[1] - tail[1]

    if abs(dist_row) <= 1 and abs(dist_col) <= 1:
        pass

    else:
        if abs(dist_row) >= 1:
            tail = (tail[0] + np.sign(dist_row), tail[1])
        if abs(dist_col) >= 1:
            tail = (tail[0], tail[1] + np.sign(dist_col))
        res_set.add(tail)

    #w = np.ones((11,11), dtype=int)
    #w[tail] = 7
    #w[head] = 8
    #print(w)

print(len(res_set))