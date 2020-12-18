import re
file = open('day-3.input')

map = []

for line in file:
  line = line.strip()
  map.append([*line])

print('x: ' + str(len(map[0])) + ' ,y: ' + str(len(map)))

currx, curry = (0,0)
number_of_trees = 0

while curry < len(map):
    if map[curry][currx % len(map[0])] == '#':
      number_of_trees += 1
    curry += 1
    currx += 3

print(number_of_trees)

