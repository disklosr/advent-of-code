lines = open('input.txt')
prios = {}
for c in range(97, 97+26):
    prios[chr(c)] = c - 96

for c in range(65, 65+26):
    prios[chr(c)] = c - 38

common = []
for line in lines:
    line = line.strip()
    size = len(line)//2
    common += list((set(line[0:size]).intersection(set(line[size:]))))

print(prios)
result = sum([prios[t] for t in common])
print(result)

