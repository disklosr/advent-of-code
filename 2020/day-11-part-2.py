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
  left = [(y, i) for i in range(0,dx) if i >= 0 and i < x]
  left.sort(reverse=True)

  right = [(y, i) for i in range(0,dx) if i > x and i < dx]
  right.sort()


  up = [(i, x) for i in range(0, dy) if i >= 0 and i < y]
  up.sort(reverse=True)


  down = [(i, x) for i in range(0, dy) if i > y and i < dy]
  down.sort()
  
  dupleft = [(y-i, x-i) for i in range(0, max([dx, dy])) if x-i >= 0 and x-i < x and y-i >= 0 and y-i < y]
  
  dupright = [(y-i, x+i) for i in range(0, max([dx, dy])) if x+i > x and x+i < dx and y-i >= 0 and y-i < y]
  
  ddownleft = [(y+i, x-i) for i in range(0, max([dx, dy])) if x-i >= 0 and x-i < x and y+i > y and y+i < dy]

  dudownright = [(y+i, x+i) for i in range(0, max([dx, dy])) if x+i > x and x+i < dx and y+i > y and y+i < dy]

  for direction in [left, right, up, down, dupleft, dupright, ddownleft, dudownright]:
    for point in direction:
      if input[point[0]][point[1]] == '.':
        continue
      elif input[point[0]][point[1]] == 'L':
        break
      if input[point[0]][point[1]] == '#':
        sum += 1
        break

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
        if count_occupied_adj_seats(map, y, x) >= 5:
          new_map[y][x] = 'L'
          changed = True
  map = new_map

print(count_occupied_seats(map))



  

