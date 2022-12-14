import math
lines = open('input.txt')


obstacles = set()
abyss_row = 0

# Parse obstacles
for line in lines:
    line = line.split(' -> ')
    for edges in zip(line, line[1:]):
        src, dst = edges
        src = tuple([int(_) for _ in src.split(',')])
        dst = tuple([int(_) for _ in dst.split(',')])

        # same column (x)
        if src[0] == dst[0]:
            for k in range(min(dst[1],src[1]), max(dst[1],src[1]) + 1):
                if k > abyss_row:
                    abyss_row = k
                obstacles.add((src[0], k))

        # same row (y)
        if src[1] == dst[1]:
            for k in range(min(src[0],dst[0]), max(src[0], dst[0]) + 1):
                if src[1] > abyss_row:
                    abyss_row = src[1]
                obstacles.add((k, src[1]))

print('abyss:', abyss_row)
print('obstacles: ',len(obstacles))

# Given a sand in a cur position
# Computes its next possible position according
# to sand falling rules. If it can't move return
# current position
def move(cur, obstacles, sand):
    for dir in [(0,1),(-1,1),(1,1)]:
        nxt = (cur[0] + dir[0], cur[1] + dir[1])
        if nxt not in obstacles and nxt not in sand:
            return nxt

    return cur
# Start sand simulation
sand_src = (500,0)
sand = set()

while True:
    #print('Numbre of current sands', len(sand))
    #input()
    cur = sand_src
    nxt = move(cur, obstacles, sand)

    while nxt != cur and nxt[1] < abyss_row:
        cur = nxt
        nxt = move(cur, obstacles, sand)
    
    if nxt[1] >= abyss_row:
        break

    sand.add(cur)

print(len(sand))