line = next(open('input.txt'))

result = 0
for i in range(0,len(line) - 4):
    if len(set(line[i:i+4])) == 4:
        result = i + 4
        break

print(result)
        



