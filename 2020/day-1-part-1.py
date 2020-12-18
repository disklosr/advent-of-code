hash_set = set()
file = open('day-1.input', 'r')

for line in file:
  curr = int(line)
  if 2020 - curr in hash_set:
    print(curr * (2020-curr))
  else:
    hash_set.add(curr)
  
