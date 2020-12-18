lines = open('day-11.input')
import timeit

def get_map():
  return [list((char for char in line.strip())) for line in lines]

map = get_map()
dy = len(map)
dx = len(map[0])

print(str(dy) + 'x' + str(dx))


def copy_from(input):
  new_map = []
  for y in range(0, dy):
    line = []
    for x in range(0, dx):
      line.append(input[y][x])
    new_map.append(line)
  return new_map

def count_occupied_seats(input):
  sum = 0
  for y in range(0, dy):
    for x in range(0, dx):
      if input[y][x] == '#':
        sum += 1
  return sum

def count_occupied_adj_seats(input, y, x):
  sum = 0
  left = [(y, x-1)]
  right = [(y, x+1)]
  up = [(y-1, x)]
  down = [(y+1, x)]
  diag = [(y-1, x-1), (y-1, x+1), (y+1, x-1), (y+1, x+1)]
  adj = set(left + right + up + down + diag)

  for point in adj:
    if point[0] < 0 or point[0] >= dy or point[1] < 0 or point[1] >= dx:
      continue
    if input[point[0]][point[1]] == '#':
      sum += 1

  return sum


changed = True
while changed == True:
  changed = False
  new_map = copy_from(map)

  for y in range(0, dy):
    for x in range(0, dx):
      if map[y][x] == 'L':
        if count_occupied_adj_seats(map, y, x) == 0:
          new_map[y][x] = '#'
          changed = True
      elif map[y][x] == '#':
        if count_occupied_adj_seats(map, y, x) >= 4:
          new_map[y][x] = 'L'
          changed = True
  map = new_map

print(count_occupied_seats(map))



  

