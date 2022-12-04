lines = [s.strip() for s in open('input.txt')]

ogr = 0
csr = 0

def find_mcb(lines, position, if_equal):
    count = [0,0] #0,1
    for line in lines:
        if line[position] == '0':
            count[0] += 1
        else:
            count[1] += 1

    return '0' if count[0] > count[1] else '1' if count[1] > count[0] else if_equal


ogr_lines = list(lines)
for i in range(0, len(lines[0])):
    mcb = find_mcb(ogr_lines, i, '1')
    ogr_lines = [line for line in ogr_lines if line[i] == mcb]
    #print((i, mcb))
    #print(ogr_lines[0:5])
    if len(ogr_lines) == 1:
        ogr = ogr_lines[0]
        break


csr_lines = list(lines)
for i in range(0, len(lines[0])):
    mcb = find_mcb(csr_lines, i, '1')
    lcb = '0' if mcb == '1' else '1'
    csr_lines = [line for line in csr_lines if line[i] == lcb]
    if len(csr_lines) == 1:
        csr = csr_lines[0]
        break

print((ogr, csr))
print(int(ogr, 2) * int(csr, 2))