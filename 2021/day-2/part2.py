import os

lines = open('input.txt', 'r')

pos = (0,0,0)

for command in lines:
    (move, units) = command.split(' ')
    (move, units) = (move, int(units))

    if move == 'forward':
        pos = (pos[0] + units, pos[1] + pos[2] * units, pos[2])

    if move == 'down':
        pos = (pos[0], pos[1], pos[2] + units)

    if move == 'up':
        pos = (pos[0], pos[1], pos[2] - units)

print(pos[0]*pos[1])