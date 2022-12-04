import os

lines = open('input.txt', 'r')

position = (0,0)

for command in lines:
    (move, units) = command.split(' ')
    (move, units) = (move, int(units))

    if move == 'forward':
        position = (position[0] + units, position[1])

    if move == 'down':
        position = (position[0], position[1] + units)

    if move == 'up':
        position = (position[0], position[1] - units)

print(position[0]*position[1])