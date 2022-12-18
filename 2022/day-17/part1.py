import numpy as np
from itertools import cycle

jets = [1 if p == '>' else -1 for p in next(open('input.txt'))]
w = np.array(['#']*7, dtype=str)

jets = cycle(jets)

# real = col, imag = row
shapes = [
    [0,1,2,3],
    [1,1j,1+1j,2+1j,1+2j],
    [2,2+1j,2+2j,2j,1+2j],
    [0,1j,2j,3j],
    [0,1,1j,1+1j]
]

# Index of highest (row) point for each shape
heights = [1,3,3,4,2]

# Move the shape by dir, return updated coordinates if success
# or old coordinates if move is not possible (either we hit
# the horizontal edge of the map or an ealier freezed shape)
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

# Draw the shape's coordinates into the world map
# so it can act as an obstacle for next falling shapes
def freeze(shape, w):
    for p in shape:
        w[(int(p.imag), int(p.real))] = '#'

bottom_row = 0
fallen = 0

# Main tetris loop
for i in cycle([0,1,2,3,4]):
    if fallen == 2022:
        print(w.shape[0] - bottom_row - 1)
        exit()
    # Make sure current shape is spaced 3 distance units away from the highest obstacle in world
    w = w[bottom_row:]
    to_stack = np.array(['.'] * 7 * (heights[i] + 3)).reshape(((heights[i] + 3),7))
    bottom_row = to_stack.shape[0]
    w = np.vstack((to_stack, w))

    # Make sure current shape is spaced 2 distance units away from left edge of the world
    shape = move(shapes[i], 2, w)
    
    # Alternate actions: push and fall
    for action in cycle(['push','fall']):
        if action == 'push':
            shape = move(shape, next(jets), w)
        else:
            new_shape = move(shape, 1j, w)

            # We can't fall further
            if new_shape == shape:
                freeze(shape, w)
                bottom_row = min(int(shape[0].imag), bottom_row)
                fallen += 1
                break
            else:
                shape = new_shape