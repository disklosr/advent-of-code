import os

lines = list(open('input.txt', 'r'))

window = 3
transformed = []

for i in range(0,len(lines) - 2):
    transformed.append(sum(int(k) for k in lines[i:i+window]))

last = transformed[0]
result = 0
for line in transformed[1:]:
    if int(line) > int(last):
        result += 1
    last = line

print(result)