import numpy as np
import math
from collections import deque, defaultdict

lines = open('input.txt')

w = []
start = (0,0)
end = None

for idx, line in enumerate(lines):
    line = [c for c in line.strip()]
    if 'E' in line:
        end = (idx, line.index('E'))

    w.append(line)

w = np.array(w)
ws = w.shape
w[start] = 'a'
w[end] = 'z'

print(ws)

print(start, '-->', end)
print(w)

c = defaultdict(lambda: math.inf)
c[start] = 0

p = defaultdict(None)
p[start] = None

to_visit = [start]

visited = set()

def find_adj(w, cur):
    for m in [(-1,0),(1,0),(0,-1),(0,1)]:
        if -1<cur[0] +m[0]<ws[0] and -1<cur[1]+m[1]<ws[1]:
            point = (cur[0] +m[0], cur[1]+m[1])
            if ord(w[point]) <= ord(w[cur]) + 1:
                yield point


def man_dis(cur, dest):
    i,j = cur
    a,b = dest
    return abs((a-i)) + abs((b-j))


while len(to_visit) > 0:
    #to_visit.sort(key=lambda p: c[p] + man_dis(p, end), reverse=True)
    to_visit.sort(key=lambda p: c[p], reverse=True)
    cur = to_visit.pop()

    if cur in visited:
        continue

    if cur == end:
        continue

    adjs = find_adj(w, cur)
    for adj in adjs:
        if c[adj] > c[cur] + 1:
            c[adj] = c[cur] + 1
            p[adj] = cur
        to_visit.append(adj)


    visited.add(cur)

path = [end]
cur = end
while True:
    if p[cur] == None:
        break
    path.append(p[cur])
    cur = p[cur]

path.reverse()
#print([w[c] for c in path])
print(len(c))
print(w.size)