import numpy as np
from queue import Queue
from itertools import product
from collections import defaultdict
from tqdm import tqdm

np.set_printoptions(linewidth=np.inf,threshold=2500)

cost = np.genfromtxt('input.txt', dtype='i', delimiter=[1]*100)
dim = len(cost)

def p(arr):
    for r in arr:
        print(''.join([str(i) for i in r]))


def add_one(arr, times):
    t = np.copy(arr)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            t[(i,j)] += 1*times
            if t[(i,j)] >= 10:
                t[(i,j)] = 1 + t[(i,j)] - 10
    return t

original = np.copy(cost)

#p(cost)
for i in range(4):
    cost = np.hstack((cost, add_one(original, i+1)))

#p(cost)

original = np.copy(cost)
for i in range(4):
    cost = np.vstack((cost, add_one(original, i+1)))

#p(cost)

max_cost = cost.sum()
state = defaultdict(lambda: max_cost)

def get_neighbours(point, dim):
    x,y = point
    for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
        if 0 <= x+dx < dim and 0 <= y+dy < dim: 
            yield (x+dx, y+dy)

def dist(point, target):
    xs, ys = point
    xt, yt = target
    return xt - xs + yt - ys

def get_item_to_explore(state, explored):
    for k in state.keys():
        if k not in explored:
            return k 
    #return min([(v,k) for k,v in state.items() if k not in explored])[1]



start = (0,0)
target = (len(cost) -1, len(cost) - 1)

state[start] = 0
explored = set()
to_explore = get_item_to_explore(state, explored)
print(to_explore)

with tqdm(total=dim*dim*25) as pbar:
    while to_explore != target:
        #print(to_explore,sep='',end='\r',flush=True)
        neighbours = get_neighbours(to_explore, len(cost))
        curr_cost = state[to_explore]
        for n in neighbours:
            state[n] = min(state[n], curr_cost + cost[n])
        explored.add(to_explore)
        to_explore = get_item_to_explore(state, explored)
        #print(to_explore)
        pbar.update(1)
    
print('')
print(state[target])





