import math
file = open('day-6.input')

result = 0

group = None
for line in file:
  line = line.strip()
  if line == '':
    result += len(group)
    group = None
  else:
    if group  == None:
      group = set(line)
    else:
      group = group.intersection(set(line)) 



print(result)
