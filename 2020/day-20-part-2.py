import re
import math
import random

tiles = {}
lines = open('day-20.input')
curr_tile = None

for line in lines:
    line = line.strip()
    if line.startswith('Tile'):
        curr_tile = int(re.findall('\d+', line)[0])
        tiles[curr_tile] = []
    if line == '':
        continue
    if '.' in line or '#' in line:
        tiles[curr_tile].append([0 if p == '.' else 1 for p in line])

dim = int(math.sqrt(len(tiles)))
print(dim)
print(len(tiles))

# for tile in tiles:
#     print(f'{tile}###################')
#     for line in tiles[tile]:
#         print(*['.' if p == 0 else '#' for p in line])

class Tile:
    def __init__(self, id):
        self.id = id
        self.top = tiles[id][0]
        self.down = tiles[id][len(tiles[id]) - 1]
        self.left = [p[0] for p in tiles[id]]
        self.right = [p[len(tiles[id]) - 1] for p in tiles[id]]
        self.content = tiles[id]


    def rotate(self, by):
        for i in range(by):
            self.plus_15_mn()

    def flip(self, by):
        if by == 1:
            #vertically
            (self.top, self.down, self.left, self.right) = (self.down, self.top, self.left[::-1], self.right[::-1])
            t = list(self.content)
            for j in range(10):
                for i in range(10):
                    t[j][i] = self.content[i][dim - j] 
    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)

    def print(self):
        print(f'top: {self.top}')
        print(f'right: {self.right}')
        print(f'down: {self.down}')
        print(f'left: {self.left}')


    def plus_15_mn(self):
        (self.top, self.down, self.left, self.right) = (self.left[::-1], self.right[::-1], self.down, self.top)

    
class Jigsaw:
    def __init__(self, base = None):
        self.puzzle = {} if base is None else base
        self.next_empty = self.get_next_empty(self.puzzle)
    
    def get_next_empty(self, puzzle):
        for j in range(dim):
            for i in range(dim):
                if (j,i) not in puzzle:
                    return (j,i)

    def can_place(self, tile):
        # if self.next_empty != (0,0):
        #     print(f'{list(self.puzzle.keys())[-1]} ==> {self.next_empty}')
        #top
        top = (self.next_empty[0] - 1, self.next_empty[1])
        if top in self.puzzle:
            if self.puzzle[top].down != tile.top:
                #if tile.id == 3079:
                    #print(f"cannot place {tile.id} down of {top}")
                return False 

        #right
        # right = (self.next_empty[0], self.next_empty[1] + 1)
        # if right in self.puzzle:
        #     if self.puzzle[right].left != tile.right:
        #         #if tile.id == 3079:
        #             #print(f"cannot place {tile.id} left of {right}")
        #         return False
        #connect down
        # down = (self.next_empty[0] + 1, self.next_empty[1])
        # if down in self.puzzle:
        #     if self.puzzle[down].top != tile.down:
        #         # if tile.id == 3079:
        #         #     print(f"cannot place {tile.id} top of {down}")
        #         return False
        #connect left
        left = (self.next_empty[0], self.next_empty[1] - 1)
        if left in self.puzzle:
            if self.puzzle[left].right != tile.left:
                # if tile.id == 3079:
                #     print(f"cannot place {tile.id} right of {left}")
                #     print(self.puzzle[left].right)
                #     print(tile.left)
                return False
        
        return True

    def place(self, tile):
        self.puzzle[self.next_empty] = tile

    def copy(self):
        return Jigsaw(self.puzzle.copy())

def solve(jigsaw, tiles_left):
    #print(jigsaw.puzzle)
    global m
    if len(tiles_left) == 0:
        return [jigsaw]
    
    sols = []
    for tile_id in tiles_left:
        new_left = tiles_left[:]
        new_left.remove(tile_id)
        for rotation in range(4):
            for f in range(2):
                t = Tile(tile_id)
                t.rotate(rotation)
                t.flip(f)
                if jigsaw.can_place(t):
                    new_jigsaw = jigsaw.copy()
                    new_jigsaw.place(t)
                    res = solve(new_jigsaw.copy(), new_left[:])
                    if res != []:
                        return res
                #else:
                    #print(f"cannot place {t.id} {rotation} in {jigsaw.next_empty}")


    return sols
            

jigsaw = Jigsaw()
tiles_left = list(tiles.keys())
tiles_left.sort()
# tiles_left.reverse()
# random.shuffle(tiles_left)
m = 0

res = solve(jigsaw, tiles_left)
print(len(res))
print(m)

if len(res) > 0:
    sol = res[0].puzzle
    print(sol)
    print(sol[(0,0)].id * sol[(0,dim-1)].id * sol[(dim-1,0)].id * sol[(dim-1,dim-1)].id)
