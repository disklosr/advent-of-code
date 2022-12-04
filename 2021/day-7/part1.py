from tqdm import tqdm
from itertools import takewhile
line = open('input.txt')

positions = [int(pos) for pos in next(line).split(',')]

print(len(positions))
min_moves = -1

def move_cost(iterator, dest):
    for source in takewhile(lambda x: True, iterator):
        yield abs(dest - source)

for dest in tqdm(range(len(positions))):
    moves = sum(move_cost(iter(positions), dest))
    if min_moves == -1:
        min_moves = moves
    else:
        min_moves = min((min_moves, moves))

print(min_moves)