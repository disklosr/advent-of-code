from tqdm import tqdm
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

monkeys2 = [
    (
        [79, 98], 
        lambda x: x * 19, 
        lambda x: 2 if x%23 == 0 else 3
    ),
    (
        [54, 65, 75, 74], 
        lambda x: x + 6, 
        lambda x: 2 if x%19 ==0 else 0
    ),
    (
        [79, 60, 97], 
        lambda x: x * x, 
        lambda x: 1 if x%13 ==0 else 3
    ),
    (
        [74], 
        lambda x: x + 3, 
        lambda x: 0 if x%17 ==0 else 1
    ),
]

result = [0 for i in monkeys]

for idx, (items,a,b) in enumerate(monkeys):
    print((idx, items))

for r in range(20):
    #print(f'####### Round {r+1} #######')
    for idx, turn in enumerate(monkeys):
        (items, worryf, targetf) = monkeys[idx]
        result[idx] += len(items)
        #print(items)
        for item in items:
            picked = item
            picked = worryf(picked)
            picked = picked // 3
            target = targetf(picked)
            #print((picked, target))
            monkeys[target][0].append(picked)

        monkeys[idx] = ([], worryf, targetf)

    #for idx, (items,a,b) in enumerate(monkeys):
        #print((idx, items))


result.sort()
print(result)
print(result[-1] * result[-2])