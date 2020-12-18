import re
from collections import deque

file = open('day-7.input')

result = 0

bags = {}

for line in file:
  res = re.findall('(?:(\d) )?(\w+ \w+)', line)
  parent = None
  for (amount, kind) in res:
    if kind == 'bags contain' or kind == 'no other':
        continue   
    else:
      if kind not in bags:
        bags[kind] = [] 
      
      if amount == '':
        #parent
        parent = kind
      else:
        #content
        bags[parent].append((int(amount), kind))

result = 0
q = deque()

q.append((1, 'shiny gold'))

while len(q) > 0:
  item = q.popleft()
  for bag in bags[item[1]]:
    result += bag[0] * item[0]
    q.append((bag[0] * item[0], bag[1]))


print(result)

