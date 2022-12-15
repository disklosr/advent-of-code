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

no_beacon = set()

for y in [2_000_000]:
    for x in tqdm(range(-3_000_000,6_000_000)):
        p = (x,y)
        if p in B or p in S:
            continue

        for source in S:
            if man_dist(source, p) <= dts[source]:
                no_beacon.add(p)

print(len(no_beacon))





