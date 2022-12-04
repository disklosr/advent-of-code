lines = open('input.txt')
prios = {}
for c in range(97, 97+26):
    prios[chr(c)] = c - 96

for c in range(65, 65+26):
    prios[chr(c)] = c - 38

common = []
group = []
gid = 0
for line in lines:
    line = line.strip()
    group.append(line)
    gid += 1

    if gid == 3:
        common.append(list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0])
        gid = 0
        group = []

print(len(common))
result = sum([prios[t] for t in common])
print(result)
