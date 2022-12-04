lines = open('input.txt')

max = 0
sum = 0

for l in lines:
    l = l.strip()
    if l == '':
        if max < sum:
            max = sum
        sum = 0
        continue
    else:
        sum += int(l)

print(max)