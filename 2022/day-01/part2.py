lines = open('input.txt')

sums = []
sum = 0

for l in lines:
    l = l.strip()
    if l == '':
        sums.append(sum)
        sum = 0
        continue
    else:
        sum += int(l)

sums.sort(reverse=True)
print(sums[0] + sums[1] + sums[2])