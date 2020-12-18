file = open('day-8.input')

program = []

for line in file:
  tokens = line.strip().split()
  program.append((tokens[0], tokens[1]))


# foreach ins
# if nop then jmp, if jmp then nop
# attempt to run
# if run until completion => good
# if not continue next patch


def run(code):
  pointer = 0
  acc = 0
  visited = set()

  while pointer < len(code):
    if pointer in visited:
      return 'loop'
    else:
      visited.add(pointer)

    (ins, arg) = (code[pointer][0], code[pointer][1])
    if ins == 'nop':
      pointer += 1
      continue
    elif ins == 'acc':
      acc += int(arg)
      pointer += 1
    elif ins == 'jmp':
      pointer += int(arg)
  
  print(acc)
  return 'end'

for i in range(len(program)):
  if program[i][0] == 'nop':
    new_program = program[:]
    new_program[i] = ('jmp', program[i][1])
    res = run(new_program)
    print(res)
    if res == 'end':
      print('acc before end: ' + res)
      break
  elif program[i][0] == 'jmp':
    new_program = program[:]
    new_program[i] = ('nop', program[i][1])
    res = run(new_program)
    if res == 'end':
      break