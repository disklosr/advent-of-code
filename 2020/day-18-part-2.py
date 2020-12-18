import re
from collections import deque
lines = open('day-18.input')

res = 0
def prod(x):
  return str(p([int(i) for i in re.split(r'\(|\)|\*', x.group(0))[1:-1]]))

def sum(match):
  return str(int(match.group(1)) + int(match.group(2)))

def p(l):
  res = 1
  for i in l:
    res *= i
  return res


for line in lines:
  t = line.strip()

  while not t.isdigit():
    t = re.sub(r'(\d+) \+ (\d+)', sum, t) # a + b
    t = re.sub(r'\(\d+(?: \* \d+)* \* \d+\)', prod, t) # (a * b * ... * e)
    t = re.sub(r'\((\d+)\)', lambda x: x.group(1), t) # (a)
    if '+' not in t:
      t = re.sub(r'(\d+) \* (\d+)', lambda x: str(int(x.group(1)) * int(x.group(2))), t) # a * b

  res += int(t)
print(res)