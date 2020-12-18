import math

lines = open('day-12.input')

direction = 'east'

wx = 10
wy = 1

x = 0
y = 0

right = {'east': 'south', 'south':'west', 'west': 'north', 'north':'east'} #clockwise
left = {'east': 'north', 'north': 'west', 'west': 'south', 'south': 'east'}

for line in lines:
  print(line)
  ins = line[0]
  by = int(line[1:-1])

  if ins == 'N':
    wy += by
  elif ins == 'S':
    wy -= by
  elif ins == 'E':
    wx += by
  elif ins == 'W':
    wx -= by
  elif ins == 'L':
    for i in range(0,int(by / 90)):
      (wx, wy) = (-wy, wx)
  elif ins == 'R':
    for i in range(0,int(by / 90)):
      (wx, wy) = (wy,-wx)
  elif ins == 'F':
    x += by * wx
    y += by * wy

  print((x,y))

print(abs(x) + abs(y))