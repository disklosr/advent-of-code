memory = [int(i) for i in next(open('input.txt')).split(',')]
memory[1] = 12
memory[2] = 2

ins_pointer = 0

while(True):
    ins = memory[ins_pointer]
    match ins:
        case 99:
            break
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
    
print(memory[0])