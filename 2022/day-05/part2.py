lines = open('input.txt')

tmp_stacks = []
stacks = []
count = 0
instructions = []


# Parse stacks
for line in lines:
    line = line.replace('\n', '')

    if line[1] == '1':
        count = len(line.split())
        break
    else:
        tmp_stacks.append(line)

for i in range(count):
    stacks.append([])

for level in reversed(tmp_stacks):
    cur = 0
    for i in range(1,len(level),4):
            if level[i] != ' ':
                stacks[cur].append(level[i])
            cur += 1


# Parse instructions
for line in lines:
    line = line.strip()
    if line == '':
        continue
    else:
        tokens = line.split()
        ins = (int(tokens[1]), int(tokens[3]), int(tokens[5]))
        instructions.append(ins)

# Apply instructions

for ins in instructions:
    crate_set = []
    for i in range(ins[0]):
        crate_set.append(stacks[ins[1]-1].pop())
    stacks[ins[2]-1] += list(reversed(crate_set))

result = ''.join([l[-1] for l in stacks])
print(result)
