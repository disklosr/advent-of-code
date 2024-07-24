from tqdm import tqdm

def compute_target(curr, picked, maxi):
    while True:
        curr -= 1
        if curr == 0:
            curr = maxi
        if curr not in picked:
            return curr

cups = [5,8,3,9,7,6,2,4,1]
for i in range(10,1_000_001):
    cups.append(i)
# cups = [3,8,9,1,2,5,4,6,7]
maxi = max(cups)
picked = [1,1,1]
rightof = list(range(0,1_000_001))

for c in zip(cups, [*cups[1:], cups[0]]):
    rightof[c[0]] = c[1]

#pcups(rightof)
curr = cups[0]
for move in tqdm(range(10_000_000)):
    # pick up next three cups
    a = rightof[curr]
    b = rightof[a]
    c = rightof[b]
    picked[0] = a
    picked[1] = b
    picked[2] = c
    
    # update setup after pickup
    nxt_curr = rightof[c]
    rightof[curr] = nxt_curr

    # compute target cup
    nxt = compute_target(curr, picked, maxi)

    # put back three cups
    rightof[c] = rightof[nxt]
    rightof[nxt] = a

    # set nex curr
    curr = nxt_curr

#pcups(rightof)
print(rightof[1] * rightof[rightof[1]])
