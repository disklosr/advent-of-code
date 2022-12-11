from tqdm import tqdm
import math
monkeys = [
    (
        [89,95,92,64,87,68], 
        lambda x: x * 11, 
        lambda x: 7 if x%2 ==0 else 4
    ),
    (
        [87,67], 
        lambda x: x +1, 
        lambda x: 3 if x%13 ==0 else 6
    ),    (
        [95, 79, 92, 82, 60], 
        lambda x: x + 6, 
        lambda x: 1 if x%3 ==0 else 6
    ),    (
        [67, 97, 56], 
        lambda x: x * x, 
        lambda x: 7 if x%17 ==0 else 0
    ),    (
        [80, 68, 87, 94, 61, 59, 50, 68], 
        lambda x: x * 7, 
        lambda x: 5 if x%19 ==0 else 2
    ),    (
        [73, 51, 76, 59], 
        lambda x: x + 8, 
        lambda x: 2 if x%7 ==0 else 1
    ),    (
        [92], 
        lambda x: x + 5, 
        lambda x: 3 if x%11 ==0 else 0
    ),    (
        [99, 76, 78, 76, 79, 90, 89], 
        lambda x: x + 7, 
        lambda x: 4 if x%5 ==0 else 5
    ),
]

modulo = math.prod([2,13,3,17,19,7,11,5])

result = [0 for i in monkeys]

for r in range(10000):
    for idx, turn in enumerate(monkeys):
        (items, worryf, targetf) = monkeys[idx]
        result[idx] += len(items)
        for item in items:
            picked = worryf(item)
            target = targetf(picked)
            picked = picked % modulo
            monkeys[target][0].append(picked)

        monkeys[idx] = ([], worryf, targetf)

print()
print(result)
result.sort()
print(result[-1] * result[-2])