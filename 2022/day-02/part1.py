rounds = open('input.txt')

score = 0
choice_score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
outcomes = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,

    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,

    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

for round in rounds:
    a,b = round.strip().split()
    score += outcomes[(a,b)]
    score += choice_score[b]

print(score)