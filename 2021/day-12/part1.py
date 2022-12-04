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
queue = ['start']

current_node = None
target_node = 'end'
current_path = []

while queue:
    current_node = queue[-1]
    if current_node == target_node:
        queue.pop()
        paths.append(list(current_path) + [target_node])
        continue
    if len(current_path) > 1 and current_node == current_path[-1]:
        # finished exploring current node
        queue.pop()
        current_path.pop()
        continue
    if is_small_cave(current_node) and current_node in current_path:
        # invalid path
        queue.pop()
        continue
    current_path.append(current_node)
    for to in graph[current_node]:
        queue.append(to)

print(len(paths))







