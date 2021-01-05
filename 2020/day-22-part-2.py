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

cards = {1: player1, 2: player2}

def get_score(cards):
    cards = deque(cards)
    res = 0
    mult = 1
    while len(cards) != 0:
        res += cards.pop() * mult
        mult += 1
    print(res)

def play_game(cards, is_master_game=False):
    history = {1: set(), 2:set()}
    winner = None
    while len(cards[1]) != 0 and len(cards[2]) != 0:
        # Start of new round
        c1 = tuple(cards[1])
        c2 = tuple(cards[2])
        if c1 in history[1] or c2 in history[2]:
            if is_master_game:
                get_score(cards[1])
            return 1
        else:
            history[1].add(c1)
            history[2].add(c2)


        # No history match found, let's draw
        draw = {1: cards[1].popleft(), 2: cards[2].popleft()}
        
        if len(cards[1]) < draw[1] or len(cards[2]) < draw[2]:
            winner = 1 if draw[1] > draw[2] else 2
        else:
            cards_copy = {
                1: deque(list(cards[1])[0:draw[1]]),
                2: deque(list(cards[2])[0:draw[2]]),
            }
            winner = play_game(cards_copy)

        cards[winner].append(draw[winner])
        if winner == 1:
            cards[winner].append(draw[2])
        else:
            cards[winner].append(draw[1])

    # we have a game winner
    if len(cards[1]) == 0:
        if is_master_game:
            get_score(cards[2])
        return 2
    else:
        if is_master_game:
            get_score(cards[1])
        return 1
        
play_game(cards, True)
    
