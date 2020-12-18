lines = open('day-14.input')

mask = ['X' for i in range(0, 36)]
mem = {}

def apply_mask(value):
  value = list(value)
  for i in range(0, 36):
    if mask[i] != 'X':
      value[i] = mask[i]

  return ''.join(value)


for line in lines:
  tokens = line.strip().split(' ')
  if tokens[0] == 'mask':
    mask = tokens[2]
  else:
    address = tokens[0][4:-1]
    value = tokens[2]
    value = format(int(value), '036b')
    
    masked_value = apply_mask(value)
    mem[int(address)] = masked_value

result = 0

for key in mem:
  result += int(mem[key], 2)

print(result)
  
  