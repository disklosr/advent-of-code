lines = open('input.txt')

zeroes = [0] * 12
ones = [0] * 12

for line in lines:
    line = line.strip()
    for i in range(0,len(line)):
        if line[i] == '0': 
            zeroes[i] += 1
        else:
            ones[i] += 1

gamma = ''
epsilon = ''

for i in range(0,12):
    if zeroes[i] > ones[i]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

result = int(gamma, 2) * int(epsilon, 2)

print(result)