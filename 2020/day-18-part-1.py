import re
from collections import deque
lines = open('day-18.input')

def find_idx_matching_parenthesis(expr, idx):
  assert expr[idx] == '('
  q = deque()
  for i in range(idx, len(expr)):
    if expr[i] == '(':
      q.append(1)
    if expr[i] == ')':
      q.pop()
      if len(q) == 0:
        return i


def solve(expr):
  i = 0
  res = 0
  op = '+'
  while True:
    if i == len(expr):
      return res
    token = expr[i]
    if re.match(r'^\d+$', token):
      if op == '+':
        res += int(token)
      else:
        res *= int(token)
      i += 1
    elif token in ['+', '*']:
      op = token
      i += 1
    elif token == '(':
      #find idx of matching parenthesis
      j = find_idx_matching_parenthesis(expr, i)
      if op == '+':
        res += solve(expr[i + 1:j])
      else:
        res *= solve(expr[i:j + 1])
      i = j + 1

sum = 0
for line in lines:
  line = line.strip()
  expr = [r.strip() for r in re.split(r'(\*|\+|\(|\))', line) if r.strip() != '']
  res = solve(expr)
  print(res)
  sum += res

print(sum)