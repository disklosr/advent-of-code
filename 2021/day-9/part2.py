import queue

map = [[int(j) for j in i.strip()] for i in open('input.txt')]

def get_translations(point):
    return [c for c in [(0,-1), (0,1), (-1,0), (1,0)] if (0 <= point[0]+c[0] < len(map)) and (0 <= point[1]+c[1] < len(map))]

def map_at(location):
    return map[location[0]][location[1]]

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

# First, find all low points

low_points = []

for line in range(len(map)):
    for column in range(len(map)):
        for translation in get_translations((line,column)):
            point = add((line,column), translation)
            if map_at(point) <= map_at((line,column)):
                break
        else:
            low_points.append((line,column))


# Second, loop over low points and discover boundaries of basin
basins = []

for low_point in low_points:
    basin = set([low_point])
    q = queue.Queue()
    q.put(low_point)

    while not q.empty():
        current_point = q.get()
        for point in [add(current_point, translation) for translation in get_translations(current_point)]:
            if map_at(point) == 9:
                pass
            elif point in basin:
                pass
            elif map_at(point) >= map_at(current_point):
                basin.add(point)
                q.put(point)

    for b in basins:
        if b & basin:
            break
    else:
        basins.append(basin)


# find top 3 largest basins and multiply their lenghts
basins.sort(key=len, reverse=True)
basins = basins[0:3]
print(len(basins[0]) * len(basins[1]) * len(basins[2]))
