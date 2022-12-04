import numpy as np

lines = open('input.txt')

start, rules = ''.join(list(lines)).split('\n\n')

start = start.strip()
rules = {k[0]: k[1] for k in [d.split(' -> ') for d in rules.splitlines()]}

letters = list(set(rules.values()))
print(letters)
rules = {(letters.index(k[0]), letters.index(k[1])): letters.index(v) for k,v in rules.items()}

freq = np.zeros((10,10), dtype='i')
print(start)
start = ''.join([str(letters.index(t)) for t in start])
print(start)
# initial counting of pairs
for i in range(len(start) - 1):
    freq[(int(start[i]), int(start[i+1]))] += 1

print(freq)

for step in range(40):
    next_freq = np.zeros((10,10), dtype='i')
    for idx in [(x,y) for x in range(10) for y in range(10) if freq[(x,y)] > 0]:
        rule = rules[idx]
        next_freq[(rule, idx[1])] += freq[idx]
        next_freq[(idx[0],rule)] += freq[idx]
    freq = next_freq
    print(freq)
    input()


print(freq)


