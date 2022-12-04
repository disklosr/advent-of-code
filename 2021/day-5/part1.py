import numpy as np
import re

lines = open('input.txt')

dim = 1
# horiz line: (*,5)
# vertical line: (5,*)

map = np.zeros((1,1), dtype='int16')
points = []

for line in lines:
    #62,963 -> 844,181
    line = line.strip()
    line = [s for s in re.split(' |,|-|>', line) if s]
    x1,y1 = (int(line[0]), int(line[1]))
    x2,y2 = (int(line[2]), int(line[3]))
    dim = max(x1,x2,y1,y2) if dim < max(x1,x2,y1,y2) else dim

    if x1 == x2 or y1 == y2:
        points.append([(x1,y1), (x2,y2)])


print(dim)

map = np.zeros((dim+1,dim+1))

for line in points:
    (x1,y1) = line[0]
    (x2,y2) = line[1]
    if x1 == x2:
        for i in range(min((y1,y2)), max((y1,y2)) + 1):
            map[x1,i] += 1
    if y1 == y2:
        for i in range(min((x1,x2)), max((x1,x2)) + 1):
            map[i,y1] += 1

map = map.transpose()

print(len(map[map > 1]))
    