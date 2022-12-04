import numpy as np
from queue import Queue
from itertools import product
from collections import defaultdict
from tqdm import tqdm

cost = np.genfromtxt('input.txt', dtype='i', delimiter=[1]*100)
dim = len(cost)

print(cost.shape)

max_cost = cost.sum()
state = defaultdict(lambda: max_cost)

def get_neighbours(point, dim):
    x,y = point
    for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
        if 0 <= x+dx < dim and 0 <= y+dy < dim: 
            yield (x+dx, y+dy)

def get_item_to_explore(state, explored):
    return min([(v,k) for k,v in state.items() if k not in explored])[1]

start = (0,0)
target = (len(cost) -1, len(cost) - 1)

state[start] = 0
explored = set()
to_explore = get_item_to_explore(state, explored)
print(to_explore)

with tqdm(total=dim*dim) as pbar:
    while to_explore != target:
        #print(to_explore,sep='',end='\r',flush=True)
        neighbours = get_neighbours(to_explore, len(cost))
        curr_cost = state[to_explore]
        for n in neighbours:
            state[n] = min(state[n], curr_cost + cost[n])
        explored.add(to_explore)
        to_explore = get_item_to_explore(state, explored)
        pbar.update(1)
    
print('')
print(state[target])





