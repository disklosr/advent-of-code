import numpy as np
import math
from collections import deque, defaultdict
import matplotlib.pyplot as plt

lines = open('input.txt')

# Map adjacent nodes finding helper
def find_adj(w, cur):
    for m in [(-1,0),(1,0),(0,-1),(0,1)]:
        if -1<cur[0] +m[0]<ws[0] and -1<cur[1]+m[1]<ws[1]:
            point = (cur[0] +m[0], cur[1]+m[1])
            if ord(w[point]) <= ord(w[cur]) + 1:
                yield point

# Manhattan distance between two nodes
def man_dis(cur, dest):
    i,j = cur
    a,b = dest
    return abs((a-i)) + abs((b-j))

### End of helpers

# world map
w = []
end = None

# Parse input and find S (start) and E (end) nodes
for idx, line in enumerate(lines):
    line = [c for c in line.strip()]
    if 'E' in line:
        end = (idx, line.index('E'))

    if 'S' in line:
        start = (idx, line.index('S'))

    w.append(line)

# Represent world as np array
w = np.array(w)
ws = w.shape

# Normalize input
w[start] = 'a'
w[end] = 'z'

# Find all nodes with 'a' so we can try them all
src=[]
for r in range(ws[0]):
    for c in range(ws[1]):
        if w[(r,c)] == 'a':
            src.append((r,c))


# For each possible starting node k
res = []
for k in src:
    # Init A* algo global variables
    c = defaultdict(lambda: math.inf)
    c[k] = 0
    p = defaultdict(None)
    p[k] = None
    to_visit = [k]
    visited = set()

    # Starting A*
    while len(to_visit) > 0:
        to_visit.sort(key=lambda u: c[u] + man_dis(u, end), reverse=True)
        cur = to_visit.pop()

        # Already visited, skip
        if cur in visited:
            continue

        # We reach destination, stop    
        if cur == end:
            break

        # Update cost of adj nodes if a shorter path is found
        adjs = find_adj(w, cur)
        for adj in adjs:
            if c[cur] + 1 < c[adj]:
                c[adj] = c[cur] + 1
                p[adj] = cur
            to_visit.append(adj)


        visited.add(cur)
    # A* finished for current starting point k

    # If we didn't reach the end ignore the path for 
    # the current starting point
    if end not in p:
        continue

    # Else reconstruct the found path
    path = [end]
    cur = end
    while True:
        if p[cur] == None:
            break
        path.append(p[cur])
        cur = p[cur]

    path.reverse()
    # Update res array with the found path's length
    res.append(len(path) - 1)

print(min(res))