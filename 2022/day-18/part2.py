import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
from collections import defaultdict

points = set()
mx, my, mz = (0,0,0)
for line in open('input.txt'):
    x,y,z = line.strip().split(',')
    x,y,z = (int(x), int(y), int(z))
    points.add((x,y,z))
    mx, my, mz = (max(mx, x), max(mx, y), max(z,mz))

print((mx+1,my+1,mz+1))

t = np.zeros((mx + 1,my + 1,mz + 1), dtype=int)
for p in points:
    t[p] = 1

print('Shape of 3d array is', t.shape)
print('Length of 3d array is', t.size)

def prioritize(q: list):
    q.sort(key=lambda p: abs(p[0]) + abs[p[1]] + abs(p[2]), reverse=True)

def explore3d(point):
    # directions: left right up down front back
    for d in [(-1,0,0), (1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
        yield (point[0] + d[0], point[1] + d[1], point[2] + d[2])

def isedge(p):
    x,y,z = p
    if x != 0 and x != mx and y != 0 and y != my and z != 0 and z != mz:
        return False
    return True

reachable = set()
unreachable = set()

# First find unreachable points for each point in map
q = [(0,0,0)]
while len(q) > 0:
    cur = q.pop()
    reachable.add(cur)
    for n in explore3d(cur):
        if n[0] < 0 or n[1] < 0 or n[2] < 0:
            continue
        try:
            v = t[n]
            if v==0 and n not in reachable:
                q.append(n)
        except:
            continue

# An element is unreachable if:
# it is not a rock and not an edge and not reachable 
for idx, p in np.ndenumerate(t):
    if p == 0 and idx not in reachable and not isedge(idx):
        unreachable.add(idx)

exposed = 0
for p in points:
    for n in explore3d(p):
        if n not in points and n not in unreachable:
            exposed += 1

print(exposed)
