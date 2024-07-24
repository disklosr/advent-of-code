memory = [int(i) for i in next(open('input.txt')).split(',')]


def run(mem, noun, verb):
    memory = [m for m in mem]
    memory[1] = noun
    memory[2] = verb
    ins_pointer = 0
    while(True):
        ins = memory[ins_pointer]
        match ins:
            case 99:
                return memory[0]
            case 1:
                in1,in2 = (memory[ins_pointer + 1], memory[ins_pointer + 2])
                out = memory[ins_pointer + 3]
                memory[out] = memory[in1] + memory[in2]
                ins_pointer += 4
            case 2:
                in1,in2 = (memory[ins_pointer + 1], memory[ins_pointer + 2])
                out = memory[ins_pointer + 3]
                memory[out] = memory[in1] * memory[in2]
                ins_pointer += 4
    

for noun in range(0,100):
    for verb in range(0,100):
        output = run(memory, noun, verb)
        if output == 19690720:
            print(100 * noun + verb)