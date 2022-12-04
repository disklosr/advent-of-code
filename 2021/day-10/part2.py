from collections import deque

charmap = {
    '{': '}',
    '<': '>',
    '[': ']',
    '(': ')',
}

scoremap = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

scores = []

for line in open('input.txt'):
    line = line.strip()
    stack = deque()
    for char in line:
        if char in charmap.keys(): #openning char
            stack.append(char)
        elif char in charmap.values(): #closing char
            current = stack.pop()
            if charmap[current] != char: #corrupted
                break
    else:
        score = 0
        while (len(stack) > 0):
            char = stack.pop()
            line += charmap[char]
            score = score * 5 + scoremap[charmap[char]]
        scores += [score]

scores.sort()
print(scores[int(len(scores) // 2)])