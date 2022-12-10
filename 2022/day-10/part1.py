lines = open('input.txt')

result = 0
lof = [20,60,100,140,180,220]
register = 1
queue = []
cycle = 0

for idx, line in enumerate(lines):
    line = line.strip()
    cycle += 1

    ins = line[0:4]
    cycles = 2 if ins == 'addx' else 1
    value = int(line[5:]) if ins == 'addx' else 0
    queue += [(ins, cycles, value)]

    if cycle in lof:
        print(('cycle', cycle, 'register', register, 'signal',cycle * register))
        result += cycle * register

    if any(queue):
        (ins, remaining_cycles, value) = queue[0]
        if remaining_cycles == 2:
            queue[0] = (ins, remaining_cycles - 1, value)
        else:
            register += value
            del queue[0]

while any(queue):
    cycle += 1

    if cycle in lof:
        result += cycle * register

    if cycle in lof or (cycle -1) in lof or (cycle + 1) in lof:
        print(('cycle', cycle, 'register', register, 'signal',cycle * register))

    (ins, remaining_cycles, value) = queue[0]
    if remaining_cycles == 2:
        queue[0] = (ins, remaining_cycles - 1, value)
    else:
        register += value
        del queue[0]

    

print(result)

