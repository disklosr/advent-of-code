import os

lines = open('input.txt', 'r')

last = next(lines)

result = 0
for line in lines:
    if int(line) > int(last):
        result += 1
    last = line

print(result)