import math

lines = open('day-13.input').readlines()
nbf = int(lines[0])
buses = lines[1].strip().split(',')
rules = []

for index, bus in enumerate(buses):
  if bus != 'x':
    rules.append((int(bus), int(index)))


rules = rules[0:9]
print(rules)

last = 0

inc = 1950893191 #found by solving rules[0:6]
t = 2053245269 #found by solving rules[0:6]

while True:  
  broke = False
  for rule in rules:
    if ((t + rule[1]) % rule[0]) != 0:
      broke = True
      break

  if not broke:
    print(t)
    print('+' + str(t - last))
    last = t
    exit()

  t += inc


## This problem can be easily solved using dp :)
## Each subproblem gives a period that helps finding its super problem