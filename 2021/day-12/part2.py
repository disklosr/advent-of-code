from collections import defaultdict
lines = open('input.txt')

graph = defaultdict(lambda: [])

def is_small_cave(cave):
    return cave.lower() == cave

for line in lines:
    line = line.strip()
    n_from, n_to = line.split('-')
    graph[n_from].append(n_to)
    graph[n_to].append(n_from)


paths = []
queue = [('start',[],True)]    

while queue:
    curr = queue.pop()
    current_node, previous_path, can_visit_twice = curr    
    
    if current_node in previous_path and is_small_cave(current_node):
        if can_visit_twice:
            can_visit_twice = False
        else:
            continue
    for to in graph[current_node]:
        if to == 'start':
            continue
        if to == 'end':
            paths.append(previous_path + [current_node] + ['end'])
            continue
        queue.append((to, previous_path + [current_node], can_visit_twice))

print(len(paths))







