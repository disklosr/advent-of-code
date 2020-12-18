from collections import deque  

lines = open('day-14.input')

mask = ['X' for i in range(0, 36)]
mem = {}

def apply_mask(value):
  expanded = []
  value = list(value)
  for i in range(0, 36):
    if mask[i] == '1':
      value[i] = '1'
    if mask[i] == 'X':
      value[i] = 'X'
  
  q = deque()
  q.append(''.join(value))

  while len(q) > 0:
    value = q.popleft()
    if 'X' in value:
      q.append(value.replace('X', '0', 1))
      q.append(value.replace('X', '1', 1))
    else:
      expanded.append(value)


  return expanded


for line in lines:
  tokens = line.strip().split(' ')
  if tokens[0] == 'mask':
    mask = tokens[2]
  else:
    address = tokens[0][4:-1]
    value = int(tokens[2])
    
    addresses = apply_mask(format(int(address), '036b'))
    for addr in addresses:
      mem[int(addr, 2)] = value

result = 0
for key in mem:
  result += mem[key]

print(result)
  
  