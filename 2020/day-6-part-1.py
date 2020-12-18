import math
file = open('day-6.input')

result = 0

group = set()
for line in file:
  line = line.strip()
  if line == '':
    result += len(group)
    group = set()
  else:
    for answer in list(line):
      group.add(answer)



print(result)
