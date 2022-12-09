import numpy as np
import math

lines = open('input.txt')
moves = []

for line in lines:
    (dir, count) = line.strip().split()
    moves += [dir for k in range(int(count))]

rope = [(0,0) for k in range(10)]

res_set = set()
res_set.add(rope[0])

for m in moves:
    #update master head
    head = rope[-1]
    if   m == 'R':
        head = (head[0], head[1] + 1)
    elif m == 'L':
        head = (head[0], head[1] - 1)
    elif m == 'U':
        head = (head[0] - 1, head[1])
    elif m == 'D':
        head = (head[0] + 1, head[1])

    rope[-1] = head

    #update tails relative to their heads
    for i in reversed(range(9)):
        head = rope[i + 1]
        tail = rope[i]
        dist_row = head[0] - tail[0]
        dist_col = head[1] - tail[1]

        if abs(dist_row) <= 1 and abs(dist_col) <= 1:
            break

        else:
            if abs(dist_row) >= 1:
                tail = (tail[0] + np.sign(dist_row), tail[1])
            if abs(dist_col) >= 1:
                tail = (tail[0], tail[1] + np.sign(dist_col))

        rope[i + 1] = head
        rope[i] = tail

    res_set.add(rope[0])

print(len(res_set))