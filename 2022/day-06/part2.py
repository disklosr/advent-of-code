line = next(open('input.txt'))

result = 0
for i in range(0,len(line) - 14):
    if len(set(line[i:i+14])) == 14:
        result = i + 14
        break

print(result)
        



