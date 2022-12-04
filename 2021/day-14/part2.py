from tqdm import tqdm
from collections import defaultdict

lines = open('input.txt')

start, rules = ''.join(list(lines)).split('\n\n')

start = start.strip()
rules = {k[0]: k[1] for k in [d.split(' -> ') for d in rules.splitlines()]}



# initial counting of pairs
state = defaultdict(int)
for i in range(len(start) - 1):
    state[start[i:i+2]] += 1

for step in tqdm(range(40)):
    new_state = defaultdict(int)
    for pair, count in state.items():
        new_state[pair[0] + rules[pair]] += count
        new_state[rules[pair] + pair[1]] += count
    state = new_state

# count frequencies of letters
counts = defaultdict(int)

for k in state.keys():
    counts[k[0]] += state[k]
    counts[k[1]] += state[k]

counts[start[0]] += 1
counts[start[-1]] += 1

counts = {k: v//2 for k, v in counts.items()}

# sort count of elements
counts = sorted(counts.values())

# compute max - min
result = counts[-1] - counts[0]

print(result)
