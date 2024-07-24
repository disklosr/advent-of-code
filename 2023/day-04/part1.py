import math
import re

score = 0
for line in open('input.txt'):
    (_, win, choice) = re.split('[:|\|]',line.strip())
    
    win = [int(k) for k in win.split()]
    choice = [int(k) for k in choice.split()]
    print(list(enumerate(set(win) & set(choice))))
    res = list(set(win) & set(choice))
    score += 0 if res == [] else (2 ** (len(res) - 1))

print(score)