import numpy as np

w = set()
mx, my, mz = (0,0,0)
for line in open('input.txt'):
    x,y,z = line.strip().split(',')
    x,y,z = (int(x), int(y), int(z))
    w.add((x,y,z))
    mx, my, mz = (max(mx, x), max(my, y), max(z,mz))

print((mx+1,my+1,mz+1))

t = np.zeros((mx + 1,my + 1,mz + 1))
for p in w:
    t[p] = 1

exposed = 0
for p in w:
    # left right up down front back
    for dir in [(-1,0,0), (1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
        test = (p[0] + dir[0], p[1] + dir[1], p[2] + dir[2])
        if test not in w:
            exposed += 1

        
print(exposed)