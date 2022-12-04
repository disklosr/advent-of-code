from collections import Counter
from tqdm import tqdm

lines = open('input.txt')

start, rules = ''.join(list(lines)).split('\n\n')
start = start.strip()

rules = {k[0]: k[1] for k in [d.split(' -> ') for d in rules.splitlines()]}

print(start)
print(set(rules.values()))
iter_str = start
curr = start

for step in tqdm(range(10)):
    inserted = 0
    for i in range(len(iter_str) - 1):
        pair = iter_str[i:i+2]
        if pair in rules:
            curr = curr[0:inserted + i + 1] + rules[pair] + curr[inserted + i+ 1:]
            inserted += 1

    iter_str = curr

print(len(curr))

c = Counter(curr)
print(c)
result = max(c.values()) - min(c.values())
print(result)

