import re
from itertools import chain

lines = enumerate(open('day-16.input'))

rules = {}
my_ticket = []
nearby_ticket = []

## Parsing input code
line = None

min_rules = 5000
max_rules = 0

while True:
  line = next(lines)
  line = line[1].strip()
  if line == '':
    break
  name, value = line.split(': ')
  value = re.split('-| or', value)
  value = [int(r) for r in value]
  if min(value) < min_rules:
    min_rules = min(value)
  if max(value) > max_rules:
    max_rules = max(value)
  rules[name] = value

next(lines)
my_ticket = [int(val) for val in next(lines)[1].strip().split(',')]
next(lines)
next(lines)

while True:
  line = next(lines, None)
  if line == None:
    break
  line = line[1].strip()
  if line == '':
    break
  nearby_ticket.append([int(val) for val in line.split(',')])

print(min_rules)
print(max_rules)
# Solving problem

valid_values = set()

for rule in rules:
  a,b,c,d = rules[rule]
  for i in chain(range(a, b + 1), range(c, d + 1)):
    valid_values.add(i)

error_rate = 0
for ticket in nearby_ticket:
  for value in ticket:
    if value not in valid_values:
      error_rate += value

print(error_rate)