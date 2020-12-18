map = set()
(z,y,x) = (0,0,0)

def is_active(point, map):
  return point in map

def get_active_neighbors(point, map):
  (w,z,y,x) = point
  active_neighbors = 0
  for dw in [-1,0,1]:
    for dz in [-1,0,1]:
      for dy in [-1,0,1]:
        for dx in [-1,0,1]:
          if dx == 0 and dy == 0 and dz == 0 and dw == 0:
            continue
          else:
            if active_neighbors > 3:
              return active_neighbors
            if is_active((w + dw, z + dz,y + dy,x + dx), map):
              active_neighbors += 1
  return active_neighbors

y = 0
for line in open('day-17.input'):
  line = line.strip()
  for x in range(len(line)):
    if line[x] == '#':
      map.add((0,0,y,x))
  y += 1

dimw = 1
dimz = 1
dimx = y
dimy = y

rangew = (min([e[0] for e in map]) - 1, max([e[0] for e in map]) + 1)
rangez = (min([e[1] for e in map]) - 1, max([e[1] for e in map]) + 1)
rangey = (min([e[2] for e in map]) - 1, max([e[2] for e in map]) + 1)
rangex = (min([e[3] for e in map]) - 1, max([e[3] for e in map]) + 1)


for cycle in range(1, 7):
  curr_map = set(map)

  for w in range(rangew[0], rangew[1] + 1):
    for z in range(rangez[0], rangez[1] + 1):
      for y in range(rangey[0], rangey[1] + 1):
        for x in range(rangex[0], rangex[1] + 1):
          point = (w,z,y,x)
          active_neighbors = get_active_neighbors(point, map)
          if active_neighbors == 3 and not is_active(point, map):
            curr_map.add(point)
          elif active_neighbors not in [2,3] and is_active(point, map):
            curr_map.remove(point)

  rangew = (min([e[0] for e in curr_map]) - 1, max([e[0] for e in curr_map]) + 1)
  rangez = (min([e[1] for e in curr_map]) - 1, max([e[1] for e in curr_map]) + 1)
  rangey = (min([e[2] for e in curr_map]) - 1, max([e[2] for e in curr_map]) + 1)
  rangex = (min([e[3] for e in curr_map]) - 1, max([e[3] for e in curr_map]) + 1)

  dimw += 1
  dimz += 1
  dimy += 1
  dimx += 1
  map = curr_map
  print('After cycle ' + str(cycle))
  print(len(map))
