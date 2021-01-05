from tqdm import tqdm

line = open('day-23.input')

init_state = line.readlines()[0].strip()
print(init_state)

#==> cloclwise
# 335634567345

cups = [int(c) for c in init_state]

add_cups = 1000000
total_moves = 10000000

for i in range(max(cups) + 1, add_cups + 1):
    cups.append(i)

print(cups[-1])

cups_len = len(cups)

def set_curr_cup(idx):
    global curr_label
    global curr_idx

    curr_idx = idx
    curr_label = cups[curr_idx]

set_curr_cup(0)
min_label = min(cups)
max_label = max(cups)
move = 0

def next_idx_clockwise(idx):
    return (idx + 1) if idx + 1 < len(cups) else 0


def find_label(label, cups):
    #print(f'findin index of {dest_label} in {cups[0:curr_idx + 10]}')

    return cups.index(label)

print(f'Running with {total_moves} moves')
pbar = tqdm(total=total_moves)

while move < total_moves:
    if move % 356 == 0:
        cups[curr_idx] = f'({str(curr_label)})'
        print(cups[:20])
        cups[curr_idx] = int(curr_label)

    #Select three cups immediately after curr_cup
    held_cups = []
    
    for k in [0,1,2]:
        index = next_idx_clockwise(curr_idx)
        held_cups.append(cups[index])
        del cups[index]
    
    #Select destination cup (curr_label -1)
    dest_label = curr_label - 1

    if dest_label < min_label:
        dest_label = max_label 

    while dest_label in held_cups:
        #print(f'dest_label = {dest_label}')
        dest_label -= 1
        if dest_label < min_label:
            dest_label = max_label

   


    #place just picked up cups
    #dest_label_idx = find_label(dest_label, cups) #expensive 
    #print((max(curr_idx - 5000, 0),min(curr_idx + 5000 + 1, cups_len)))

    try:
        dest_label_idx = cups.index(dest_label)
    
    except ValueError as ex:
        print(move)
        print(held_cups)
        print(ex)
        print('oops')
        exit()
    #if(dest_label_idx) > curr_idx:
    #    print(f'{dest_label_idx} > {curr_idx}')

    for cup in reversed(held_cups):
        cups.insert(next_idx_clockwise(dest_label_idx), cup) #expensive insert
    
    #Select new curr cup

    while cups[curr_idx] != curr_label:
        curr_idx = next_idx_clockwise(curr_idx)

    curr_idx = next_idx_clockwise(curr_idx)

    move += 1
    pbar.update(1)
pbar.close()

idx_of_1 = cups.index(1)
print(cups[next_idx_clockwise(idx_of_1)], cups[next_idx_clockwise(next_idx_clockwise(idx_of_1))])