from collections import deque

charmap = {
    '{': '}',
    '<': '>',
    '[': ']',
    '(': ')',
}

scoremap = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

score = 0

for line in open('input.txt'):
    line = line.strip()
    stack = deque()
    for char in line:
        if char in charmap.keys(): #openning char
            stack.append(char)
        elif char in charmap.values(): #closing char
            current = stack.pop()
            if charmap[current] != char: #corrupted
                score += scoremap[char]


print(score)

