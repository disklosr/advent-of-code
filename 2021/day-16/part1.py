line = open('input.txt').readline()

def to_bin(hex):
    binary = ''
    for h in hex:
        binary += f'{int(h,16):b}'.rjust(4,'0')
    return binary

def read_b(bits, nxt, i):
    print(f'{(i,nxt)} --> {int(bits[i:i+nxt],2)}')
    return (int(bits[i:i+nxt],2), i+nxt)

def read_s(string, nxt, i):
    print(f'{(i,nxt)} --> {string[i:i+nxt]}')
    return (string[i:i+nxt], i+nxt)

line = 'D2FE28'
b = to_bin(line)
versions = 0
i = 0
print(b)

while i < len(b):
    # read packet from position i
    print('new packet')
    version, i = read_b(b, 3, i)
    type_id, i = read_b(b, 3, i)
    input()
    if type_id == 4: # literal value
        val = ''
        while True:
            bit = read_b(b, 1, i)
            if bit == 0:
                break
            part, i = read_s(b, 4, i)
            val += part
        part, i = read_s(b, 4, i)
        val += part
        print(f'literal value: {int(val,2)}')
    else: # operator packet
        l_type_id, i = read_b(b, 1, i)
        if l_type_id == 0:
            total_length, i = read_b(b, 15, i)
        else:
            sub_packets_nbr, i = read_b(b, 11, i)



print(versions)

