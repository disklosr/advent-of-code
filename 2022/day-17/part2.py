import numpy as np
from itertools import cycle

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
        assert(int(p.imag) >= 0)
        assert(int(p.real) >= 0)
        w[(int(p.imag), int(p.real))] = '#'




def simulate(fallen_number):
    jets = [1 if p == '>' else -1 for p in next(open('input.txt'))]
    w = np.array(['#']*7, dtype=str)
    bottom_row = 0
    fallen = 0
    result = 0
    jets = cycle(jets)
    periods = []
    
    # Main tetris loop
    for i in cycle([0,1,2,3,4]):
        if fallen == fallen_number:
            height = w.shape[0] - bottom_row - 1
            return (height, periods) 
    
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

                    # Detect completely blocked bottom
                    if fallen > 10 and all([True if k == '#' else False for k in w[bottom_row]]):
                        periods.append(fallen)
                    break
                else:
                    shape = new_shape

# Run a simulation to witness the periodic pattern of the rocks falling
result = simulate(5000)
print('Height after 5000 rocks have fallen',result[0])
print('Periods witnessed at', result[1])
diff_periods = [k[1] - k[0] for k in zip(result[1], result[1][1:])]
print('Diff between periods', diff_periods)

offset = result[1][0]
period = diff_periods[0] + diff_periods[1]

print('Found offset', offset)
print('Found period', period)

# From previous simulation on my particulat input, we see that:
# First period starts after 456 rocks have fallen
# then subsequent periods happen every 800+910=1710 fallen rocks
# And each start of period coincides with the '+' shape

# Let H(N) be the actual height after N rocks have fallen
# Let dH(N) be the height increase after N rocks have fallen, starting from 
# a completely blocked bottom: dH(N) = H(N+465) - H(465)

# We can compute the height H(N) after N rocks have fallen:
# We first write N as 456 + 1710 * a + b = N
# We can then compute H(N) = H(456) + dH(1710) * a + dH(b)
# Which can be written as:
# H(N) = (H(1710 + 456) - H(465)) * a + H(b + 456)

def H(fallen):
    return simulate(fallen)[0]

N = 1000000000000

a = (N - offset) // period
b = (N - offset) % period

result = (H(period + offset) - H(offset)) * a + H(b + offset)
print('Puzzle answer', result)
