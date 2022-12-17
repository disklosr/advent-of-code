import re
import math
from collections import namedtuple, defaultdict, OrderedDict


FR = dict()
NV = dict()

for line in open('input.txt'):
    line = [i for i in re.split(';|,| |\n|=', line) if i != '']
    FR[line[1]] = int(line[5])
    NV[line[1]] = line[10:]

# compute foreach valve the cost consisting of:
# (time_passed, cum_pressure_released)

# traverse as long as 
# time_passed <= 30 (from 1 to 30 inclusive)
# or all vales have been already open 

# State of the world
# (Valve states, time left, current flow rate)

def copydict(d):
    return {v[0]:v[1] for v in d.items()}

State = namedtuple('State', 'vstate cvalve timeleft cflowrate score vvcount')

def run(state: State, graph, scores):
    vstate, cvalve, timeleft, cflowrate, score, vvcount = state
    #print(state)
    #input()

    # if vvcount == ['DD', '_', 'CC', 'BB', '_', 'AA', 'II', 'JJ', '_', 'II', 'AA', 'DD', 'EE', 'FF', 'GG', 'HH', '_', 'GG', 'FF', 'EE', '_', 'DD', 'CC', '_', '.', '.', '.', '.', '.', '.' ]:
    #     print(vvcount, cflowrate, score, vvcount)
    #     input()

    if timeleft < 10 and cflowrate < 30:
        # skip exploring these
        return

    if scores[30][1] == 1651:
        print(vvcount)
        input()

    # Stop if clock runs out
    if timeleft == 0:
        if scores[30][1] < score:
            scores[30] = (cflowrate, score)
            #print(vvcount)
            print('new max score', score)
            #input()
        return

    # if score != 0 and scores[30 - timeleft][0] > cflowrate + 10 and scores[30 - timeleft][1] > score + 10:
    #     # we had better scores/flow rates at this time in another branch
    #     # abondon this exploration
    #     return
    # else:
    #     if score != 0:
    #         scores[30 - timeleft] = (cflowrate, score)

    # If all valves with non zero flow rate are open
    if all([v[1] == 1 or FR[v[0]] == 0 for v in vstate.items()]):
        #print('wait for time to end', state)
        #input()
        run((vstate, cvalve, 0, cflowrate, score + timeleft * cflowrate, vvcount + ['.']*timeleft), graph, scores)

    #print(state)

    #if can open valve
    if vstate[cvalve] == 0 and FR[cvalve] != 0:
        t = copydict(vstate)
        t[cvalve] = 1
        run((t, cvalve, timeleft - 1, cflowrate + FR[cvalve], score + cflowrate, vvcount + ['_']), graph, scores)
    
    # Try moving in all cases: choose next valve to go to
    for v in NV[cvalve]:
        if len([f for f in vvcount if f == v]) > 2:
            #print('loop detected, dont explore')
            continue
        else:
            run((vstate, v, timeleft - 1, cflowrate, score + cflowrate, vvcount + [v]), graph, scores)

    

istate = State({v[0]:0 for v in FR.items()}, 'AA', 30, 0, 0, [])

scores = defaultdict(lambda :(0,0))
result = run(istate, NV, scores)

print(scores[30])
# for t in OrderedDict(sorted(scores.items(), key = lambda x: x[0])).items():
#     print(t[0],t[1])


# Open or move or finish