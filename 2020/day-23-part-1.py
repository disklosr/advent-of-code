line = open('day-23.input')

init_state = line.readlines()[0].strip()
print(init_state)

#==> cloclwise
# 335634567345

cups = [int(c) for c in init_state]
curr_label = cups[0]
min_label = min(cups)
max_label = max(cups)
move = 0

def next_idx_clockwise(curr_idx):
    return (curr_idx + 1) % len(init_state)

while move < 100:
    print(f'#### Move {move + 1}')
    print(cups)
    print(curr_label)
    #Select three cups immediately after curr_cup
    curr_idx = cups.index(curr_label)
    held_cups = [cups[next_idx_clockwise(curr_idx + k)] for k in [0,1,2]]
    
    #Remove selected cups
    for cup in held_cups:
        cups.remove(cup)

    print(held_cups)
    
    dest_label = curr_label - 1
    #Select destination cup (curr_label -1)
    while dest_label not in cups:
        dest_label -= 1
        if dest_label < min_label:
            dest_label = max_label

    print(dest_label)

    #place just picked up cups
    dest_label_idx = cups.index(dest_label)

    for cup in reversed(held_cups):
        cups.insert(dest_label_idx + 1, cup)
    
    #Select new curr cup
    curr_label = cups[next_idx_clockwise(cups.index(curr_label))] 
    move += 1

print(cups)
idx_of_1 = cups.index(1)
idx = next_idx_clockwise(idx_of_1)
res = ''

while idx != idx_of_1:
    res += str(cups[idx])
    idx = next_idx_clockwise(idx)

print(res)

