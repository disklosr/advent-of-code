import numpy as np
from itertools import cycle

jets = [1 if p == '>' else -1 for p in next(open('input.txt'))]
w = np.array(['#']*7, dtype=str)

print(w)

jets = cycle(jets)

# real = col, imag = row
shapes = [
    [0,1,2,3],
    [1,1j,1+1j,2+1j,1+2j],
    [2,2+1j,2+2j,2j,1+2j],
    [0,1j,2j,3j],
    [0,1,1j,1+1j]
]

heights = [
    1,
    3,
    3,
    4,
    2
]

def move(shape, dir, w):
    new_shape = [p + dir for p in shape]
    try:
        for p in new_shape:
            if p.imag < 0 or p.real < 0:
                return shape
            if w[(int(p.imag), int(p.real))] == '#':
                return shape
        return new_shape
    except:
        return shape

def freeze(shape, w):
    for p in shape:
        assert(int(p.imag) >= 0)
        assert(int(p.real) >= 0)
        w[(int(p.imag), int(p.real))] = '#'

def display(w):
    print(str(w[:-1])
        .replace('\'', '')
        .replace(' ', '')
        .replace('[[', '[')
        .replace(']]', ']')
    )
    input()

bottom_row = 0
fallen = 0
result = 0
for i in cycle([0,1,2,3,4]):
    if fallen == 2022:
        print(w.shape, bottom_row)
        result = w.shape[0] - bottom_row
        break
    w = w[bottom_row:]
    to_stack = np.array(['.'] * 7 * (heights[i] + 3)).reshape(((heights[i] + 3),7))
    bottom_row = to_stack.shape[0]
    w = np.vstack((to_stack, w))
    shape = move(shapes[i], 2, w)
    for action in cycle([1,2]):
        if action == 1: #push
            shape = move(shape, next(jets), w)
        else: #fall
            new_shape = move(shape, 1j, w)
            if new_shape == shape:
                freeze(shape, w)
                bottom_row = min(int(shape[0].imag), bottom_row)
                fallen += 1
                #display(w)
                break
            else:
                shape = new_shape

print(result - 1)