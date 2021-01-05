from collections import deque
lines = open('day-22.input')

player1 = deque()
player2 = deque()

#top = left, right = bottom
curr_player = None

for line in lines:
    line = line.strip()
    if line.startswith('Player 1'):
        curr_player = player1
    elif line.startswith('Player 2'):
        curr_player = player2
    elif line == '':
        continue
    else:
        curr_player.append(int(line))


print(player1)
print(player2)

total = len(player2) + len(player1)

while len(player2) > 0 and len(player1) > 0:
    top1 = player1.popleft()
    top2 = player2.popleft()

    if top1 > top2:
        player1.append(top1)
        player1.append(top2)
    else:
        player2.append(top2)
        player2.append(top1)

winner = player2 if len(player1) == 0 else player1
print(winner)

mult = 1
res = 0
while len(winner) != 0:
    res += winner.pop() * mult
    mult += 1

print(res)