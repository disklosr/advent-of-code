from collections import deque
import itertools

file = open('day-9.input')

result = None

def is_valid(curr, queue):
  preamble = list(queue)
  for comb in itertools.combinations(preamble, 2):
    if curr == comb[0] + comb[1] and comb[0] != comb[1]:
      return True
  return False

q = deque()
for line in file:
  if len(q) < 25:
    q.append(int(line))
    continue
  else:
    curr = int(line)
    if is_valid(curr, q):
      q.popleft()
      q.append(curr)
      continue
    else:
      result = curr
      break

print(result)
