import math
import re

score = 0

matchings = {}
cards = {}

for idx, line in enumerate(open('input.txt')):
    (_, win, choice) = re.split('[:|\|]',line.strip())
    
    win = [int(k) for k in win.split()]
    choice = [int(k) for k in choice.split()]
    
    matches = len(list(set(win) & set(choice)))
    matchings[idx] = matches
    cards[idx] = 1

for k,v in cards.items():
    for i in range(matchings[k]):
        cards[k+1+i] += v


print(sum(cards.values()))