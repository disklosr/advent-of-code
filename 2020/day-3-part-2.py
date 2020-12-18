import re
file = open('day-3.input')

map = []

for line in file:
  line = line.strip()
  map.append([*line])



def get_number_of_trees(movex, movey):
  currx, curry = (0,0)
  number_of_trees = 0

  while curry < len(map):
      if map[curry][currx % len(map[0])] == '#':
        number_of_trees += 1
      curry += movey
      currx += movex

  return number_of_trees



print(get_number_of_trees(1,1) * get_number_of_trees(3,1) * get_number_of_trees(5,1) *  get_number_of_trees(7,1) * get_number_of_trees(1,2))

