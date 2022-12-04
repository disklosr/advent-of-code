map = [[int(j) for j in i.strip()] for i in open('input.txt')]

print(len(map), len(map[0]))

def get_adjacent_masks(point):
    return [c for c in [(0,-1), (0,1), (-1,0), (1,0)] if (0 <= point[0]+c[0] < len(map)) and (0 <= point[1]+c[1] < len(map))]

total_risk = 0

for line in range(len(map)):
    for column in range(len(map)):
        adjascents = get_adjacent_masks((line,column))
        for a in adjascents:
            point = (line + a[0],column + a[1])
            print(point)
            if map[point[0]][point[1]] <= map[line][column]:
                break
        else:
            total_risk += 1 + map[line][column]


print(total_risk)
