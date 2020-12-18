file = open('day-8.input')

program = []
pointer = 0
acc = 0
visited = set()

for line in file:
  tokens = line.strip().split()
  program.append((tokens[0], tokens[1]))
  

while pointer < len(program):
  if pointer in visited:
    print(acc)
    break
  else:
    visited.add(pointer)
    
  (ins, arg) = (program[pointer][0], program[pointer][1])
  if ins == 'nop':
    pointer += 1
    continue
  elif ins == 'acc':
    acc += int(arg)
    pointer += 1
  elif ins == 'jmp':
    pointer += int(arg)