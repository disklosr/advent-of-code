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
        bags[kind].append(parent)

result = []
q = deque()

q.append('shiny gold')

while len(q) > 0:
  item = q.popleft()
  result += bags[item]
  for bag in bags[item]:
    q.append(bag)


print(len(set(result)))

