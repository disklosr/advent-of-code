rounds = open('input.txt')

score = 0
action_score = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

choice_score = {
    'A': 1,
    'B': 2,
    'C': 3
}

outcomes = {
    ('A', 'X'): 'C',
    ('A', 'Y'): 'A',
    ('A', 'Z'): 'B',

    ('B', 'X'): 'A',
    ('B', 'Y'): 'B',
    ('B', 'Z'): 'C',

    ('C', 'X'): 'B',
    ('C', 'Y'): 'C',
    ('C', 'Z'): 'A',
}

for round in rounds:
    a,b = round.strip().split()
    score += action_score[b]
    score += choice_score[outcomes[(a,b)]]

print(score)