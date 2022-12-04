import numpy as np

lines = ''.join(list(open('input.txt')))

dots, instructions = lines.split('\n\n')

dots = [(int(dot.split(',')[0]),int(dot.split(',')[1])) for dot in dots.splitlines()]
instructions = [line.split(' ')[-1] for line in instructions.splitlines()]
instructions = [(s.split('=')[0], int(s.split('=')[1])) for s in instructions]

arr = np.zeros((instructions[0][1]*2 + 1, instructions[1][1]*2 + 1), dtype='i')

for dot in dots:
    arr[dot] = 1

arr = arr.transpose()

for fold in instructions[0:1]:
    axis, location = fold
    if axis == 'x':
        arr = arr[:,0:location] + np.flip(arr[:,location+1:], 1) 
    else:
        arr = arr[0:location] + np.flip(arr[location+1:], 0)

print(len(arr[arr>0]))