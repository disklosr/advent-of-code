import re
from itertools import chain, cycle

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

print(len(nearby_ticket))

for ticket in nearby_ticket[:]:
  for value in ticket:
    if value not in valid_values:
      nearby_ticket.remove(ticket)
      break

print(len(nearby_ticket))

rule_positions = {}
found_rules = set()

for rule in rules:
  if rule not in rule_positions:
    rule_positions[rule] = []
  
  a,b,c,d = rules[rule]
  for i in range(0, len(nearby_ticket[0])):
    values = [ticket[i] for ticket in nearby_ticket if ticket[i] < a or b < ticket[i] < c or ticket[i] > d]
    if len(values) == 0:
      rule_positions[rule].append(i)

print(rule_positions)

for rule in cycle(rules):
  if len(found_rules) == len(rules):
    break
  if len(rule_positions[rule]) == 1:
    found_rules.add(rule_positions[rule][0])
  else:
    for i in found_rules:
      if i in rule_positions[rule]:
        rule_positions[rule].remove(i)

res = 1
for rule in rules:
  if rule.startswith('departure'):
    res *= my_ticket[rule_positions[rule][0]]

print(res)

