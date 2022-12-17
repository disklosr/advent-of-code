import numpy as np
from itertools import cycle

jets = [1 if p == '>' else -1 for p in next(open('input.txt'))]
w = np.array(['#']*7, dtype=str)

print(len(jets))

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

hh = []

for i in cycle([0,1,2,3,4]):
    if fallen == 634+456:
        #print(w.shape, bottom_row)
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
                if fallen > 10 and all([True if k == '#' else False for k in w[bottom_row]]):
                    # print('row filled at',bottom_row)
                    # print(fallen)
                    # print('next shape', (i + 1)%5)
                    hh.append(w.shape[0] - bottom_row - 1)
                    #display(w[:10])
                break
            else:
                shape = new_shape

print(w[:10])
print(result - 1)
#print(result - 1 + (1000000000000 // (800+910)) * (1273+1410))

# >>> a = [455,1255,2165,2965,3875,4675,5585,6385,7295,8095,9005,9805]
# >>> [k[1]-k[0] for k in zip(a,a[1:])]
# [800, 910, 800, 910, 800, 910, 800, 910, 800, 910, 800]

#every 800+900 fallen items, 
#we add 1237+1410 heights 
#and we can start from zero

#so we only need to compute height for 1090 items and add the rest

# after 456 + p*0 we are at height 714
# after 456 + p*1 we are at height 3361
# after 456 + p*2 we are at height 6008
# after 456 + p*2 we are at height 8655


#456 + 1710 * 584795321 + 634 = 1000000000000
#2647 * 584795321 + h(634+456)


#456 + 1710 * 5 + 17 = 13977
#2647 * 5 + 742 = 

# at 5000 height is 7744
