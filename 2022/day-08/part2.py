import math
lines = open('input.txt')

dim = 0
map = []
for line in lines:
    line = line.strip()
    dim = len(line)
    map.append([int(i) for i in line])

result = 0

def score(dis_arr, reverse=False):
    if reverse:
        dis_arr = list(reversed(dis_arr))
    
    idx = 0

    if len(dis_arr) == 0:
        return 0

    if len(dis_arr) == 1:
        return 1

    while idx < len(dis_arr):
        if dis_arr[idx] == 1:
            idx += 1
            continue

        if dis_arr[idx] != 1:
            return idx + 1

    return idx

for i in range(1,dim-1):
    for j in range(1,dim-1):
        curr = map[i][j]

        left = [1 if k < curr else -1 if k == curr else 0 for k in map[i][0:j]]

        right = [1 if k < curr else -1 if k == curr else 0 for k in map[i][j+1:]]

        up = [1 if k[j] < curr else -1 if k[j] == curr else 0 for k in map[0:i] ]

        down = [1 if k[j] < curr else -1 if k[j] == curr else 0 for k in map[i+1:]]

        score_arr = [
            score(left, True),
            score(right), 
            score(up, True), 
            score(down)
        ]

        curr_score = math.prod(score_arr)

        if curr_score > result:
            result  = curr_score



print(result)