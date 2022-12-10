import numpy as np
lines = open('input.txt')

lof = [20,60,100,140,180,220]
register = 1
queue = []
cycle = 0

crt = ['_' for i in range(240)]

# Prints the screen view
def view(crt):
    for i in range(6):
        print(''.join(crt[i*40:i*40 + 40]))

# As long as there are lines to read 
# or instructions in queue to execute
while (line := next(lines, None)) is not None or any(queue):
    cycle += 1

    if line is not None:
        line = line.strip()

        # Read instruction into queue
        ins = line[0:4]
        cycles = 2 if ins == 'addx' else 1
        value = int(line[5:]) if ins == 'addx' else 0
        queue += [(ins, cycles, value)]

    # CRT draw
    crt[cycle - 1] = '#' if (cycle - 1) % 40 in [register -1, register, register + 1] else '.'

    # Execute instructions from queue
    if any(queue):
        (ins, remaining_cycles, value) = queue[0]
        if remaining_cycles == 2:
            queue[0] = (ins, remaining_cycles - 1, value)
        else:
            register += value
            del queue[0]

view(crt)