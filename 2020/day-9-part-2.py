from collections import deque
import itertools

file = open('day-9.input')
numbers = list(reversed([int(line) for line in file]))

result = None

for window in range(2, len(numbers)):
  for i in range(0,len(numbers) - window + 1):
    sub_array = numbers[i:i+window]
    if sub_array[0] > 675280050 or sub_array[-1] > 675280050:
      continue
    if sum(sub_array) == 675280050:
      print(min(sub_array) + max(sub_array))
      exit()
