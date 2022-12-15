import numpy as np
import re
from tqdm import tqdm

def man_dist(src, dst):
    a,b = src
    k,m = dst

    return abs(a-k) + abs(b-m)


B = set()
S = set()
dts = dict()

lines = open('input.txt')
for line in lines:
    line = line.strip()
    line = re.split(', |:|=', line)
    source = (int(line[1]),int(line[3]))
    beacon = (int(line[5]), int(line[7]))
    S.add(source)
    B.add(beacon)
    dts[source] = man_dist(source, beacon)

print(max)
no_beacon = set()
minx = 6_000_000
maxx = -4_000_000


#min:-671176  max:4208796



def get_candidates(s, dist):
    x,y = s

    cc = [
            (x + dist + 1, y),
            (x - dist - 1, y),
            (x, y + dist + 1),
            (x, y - dist - 1)
        ]

    for item in cc:
        if 0 <= item[0] <= 4000000 and 0 <= item[1] <= 4000000:
            if item not in S and item not in B:
                yield item

    for i in range(1, dist + 1):
        cc = [
            (x - i, y + (dist - i + 1)),
            (x - i, y - (dist - i + 1)),
            (x + i, y + (dist - i + 1)),
            (x + i, y + (dist - i + 1))
        ]
        for item in cc:
            if 0 <= item[0] <= 4000000 and 0 <= item[1] <= 4000000:
                if item not in S and item not in B:
                    yield item

# Find candidates
candidates = set()

for s in tqdm(S):
    for c in get_candidates(s, dts[s]):
        candidates.add(c)

print(len(candidates))

result = None
for c in tqdm(candidates):
    if all([man_dist(s, c) > dts[s] for s in S]):
        result = c
        break

print(result)