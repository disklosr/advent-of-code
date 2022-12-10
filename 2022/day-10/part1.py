lines = open('input.txt')

result = 0
lof = [20,60,100,140,180,220]
register = 1
queue = []
cycle = 0

# As long as there are lines to read 
# or instructions in queue to execute
while (line := next(lines, None)) is not None or any(queue):
    cycle += 1
    
    if line is not None:
        line = line.strip()

        # Read instructions into queue
        ins = line[0:4]
        cycles = 2 if ins == 'addx' else 1
        value = int(line[5:]) if ins == 'addx' else 0
        queue += [(ins, cycles, value)]

    # Update result as we go
    if cycle in lof:
        result += cycle * register

    if any(queue):
        (ins, remaining_cycles, value) = queue[0]
        if remaining_cycles == 2:
            queue[0] = (ins, remaining_cycles - 1, value)
        else:
            register += value
            del queue[0]    

print(result)
