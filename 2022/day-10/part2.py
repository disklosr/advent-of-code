import numpy as np
lines = open('input.txt')

result = 0
lof = [20,60,100,140,180,220]
register = 1
queue = []
cycle = 0

crt = ['_' for i in range(240)]

def draw(crt):
    for i in range(6):
        print(''.join(crt[i*40:i*40 + 40]))

draw(crt)

for idx, line in enumerate(lines):
    line = line.strip()
    cycle += 1

    ins = line[0:4]
    cycles = 2 if ins == 'addx' else 1
    value = int(line[5:]) if ins == 'addx' else 0
    queue += [(ins, cycles, value)]

    # CRT draw
    crt[cycle - 1] = '#' if (cycle - 1) % 40 in [register -1, register, register + 1] else '.'

    if cycle in lof:
        print(('cycle', cycle))
        draw(crt)
    # Execute instruction
    if any(queue):
        (ins, remaining_cycles, value) = queue[0]
        if remaining_cycles == 2:
            queue[0] = (ins, remaining_cycles - 1, value)
        else:
            register += value
            del queue[0]

while any(queue):
    cycle += 1

# CRT draw
    crt[cycle - 1] = '#' if (cycle - 1) % 40 in [register -1, register, register + 1] else '.'

    if cycle in lof or (cycle -1) in lof or (cycle + 1) in lof:
        print(('cycle', cycle, 'register', register, 'signal',cycle * register))

    (ins, remaining_cycles, value) = queue[0]
    if remaining_cycles == 2:
        queue[0] = (ins, remaining_cycles - 1, value)
    else:
        register += value
        del queue[0]

draw(crt)

print(result)