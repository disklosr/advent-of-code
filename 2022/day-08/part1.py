import numpy as np
lines = open('input.txt')

dim = 0
map = []
for line in lines:
    line = line.strip()
    dim = len(line)
    map.append([int(i) for i in line])

map = np.array(map)

visible = 2*dim + 2 * (dim-2)

for i in range(1,dim-1):
    for j in range(1,dim-1):
        curr = map[i][j]
        left = sum([1 if k >= curr else 0 for k in map[i][0:j]])

        if left == 0:
            visible += 1
            continue

        right = sum([1 if k >= curr else 0 for k in map[i][j+1:]])

        if right == 0:
            visible += 1
            continue
        
        up = sum([1 if k[j] >= curr else 0 for k in map[0:i] ])

        if up == 0:
            visible += 1
            continue
        
        down = sum([1 if k[j] >= curr else 0 for k in map[i+1:]])

        if down == 0:
            visible += 1
            continue


print(visible)