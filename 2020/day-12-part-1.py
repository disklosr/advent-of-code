import math

lines = open('day-12.input')

direction = 'east'
x = 0
y = 0

right = {'east': 'south', 'south':'west', 'west': 'north', 'north':'east'} #clockwise
left = {'east': 'north', 'north': 'west', 'west': 'south', 'south': 'east'}

for line in lines:
  print(line)
  ins = line[0]
  by = int(line[1:-1])

  if ins == 'N':
    y += by
  elif ins == 'S':
    y -= by
  elif ins == 'E':
    x += by
  elif ins == 'W':
    x -= by
  elif ins == 'L':
    for i in range(0,int(by / 90)):
      direction = left[direction]
  elif ins == 'R':
    for i in range(0,int(by / 90)):
      direction = right[direction]
  elif ins == 'F':
    if direction == 'east':
      x += by
    elif direction == 'west':
      x -= by
    elif direction == 'north':
      y += by
    elif direction == 'south':
      y -= by

  print((x,y))

print(abs(x) + abs(y))