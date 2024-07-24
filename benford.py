from collections import defaultdict as dd
counter = dd(lambda : 0)
count = 0
for l in open('numbers.txt'):
    l = l.strip()
    if l == '0':
        continue
    counter[l[0]] += 1
    count += 1

print(len(counter))
for i in range(1,10):
    i = str(i)
    print(f'{i}: {counter[i]*100//count}%')