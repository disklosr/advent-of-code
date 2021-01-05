import re
from itertools import cycle

lines = open('day-21.input')

problem = {}
foods = []
allergenes = {}

for line in lines:
    line = line.strip()
    (food, allergies) = line.split('(contains ')
    ingredients = re.findall(r'\w+', food)
    allergies = re.findall(r'\w+', allergies)
    foods.append((ingredients, allergies))
    for a in allergies:
        if a not in allergenes:
            allergenes[a] = []
        allergenes[a].append(set(ingredients))

    
    for ingredient in ingredients:
        if ingredient not in problem:
            problem[ingredient] = []
        problem[ingredient].append((food, allergies))

solved = {}

for a in allergenes:
    allergenes[a] = allergenes[a][0].intersection(*allergenes[a])

print(allergenes)

cont  = True
while True:
    if not cont:
        break
    cont = False
    for i in allergenes.keys():
        if len(allergenes[i]) == 1:
            solved[i] = allergenes[i].pop()
            cont = True
        else:
            common = allergenes[i].intersection(set(solved.values()))
            if len(common) > 0:
                cont = True
                for c in common:
                    allergenes[i].remove(c)

res = [(solved[k], k) for k in solved]
res.sort(key=lambda x: x[1])
res = [t[0] for t in res]
print(','.join(res))


