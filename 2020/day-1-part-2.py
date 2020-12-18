input = []
file = open('day-1.input', 'r')

for line in file:
    input.append(int(line))

def matches_first_problem(num):
  s = set()
  for i in input:
    if num - i in s:
      return (num - i) * i
    else:
      s.add(i)
  return 0

for i in input:
  res = matches_first_problem(2020 - i)
  if  res != 0:
    print(i * res)


