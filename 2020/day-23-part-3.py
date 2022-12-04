from tqdm import tqdm

initial_state = [int(i) for i in list(open('day-23.input'))[0].strip()]
initial_state = [3,8,9,1,2,5,4,6,7]

circle_len = len(initial_state)
circle = list(initial_state)
current_index = 0
current_cup = circle[current_index]

def get_next(source, idx):
        return (idx + 1) % len(circle)

for move in range(100):
    print(circle)
    print(f'current: {current_cup}')
    # step 1: pick up 3 cups

    held_cups = []
    idx = get_next(circle, current_index)
    for _ in range(3):
        held_cups.append(circle.pop(idx))

    print(f'pick up: {held_cups}')

    # step 2: select destination cup
    dest_cup = current_cup - 1
    if dest_cup == 0:
        dest_cup = 9
    while (dest_cup in held_cups):
        dest_cup = dest_cup - 1
        if dest_cup == 0:
            dest_cup = 9

    print(f'destination: {dest_cup}')
    # step 3: place held cups into destination cup
    dest_index = circle.index(dest_cup)
    input()

    idx = get_next(circle, dest_index)
    for cup in held_cups[::-1]:
        circle.insert(idx, cup)

    # step 4: select new current cup
    current_index = (current_index + 1) % circle_len
    current_cup = circle[current_index]


print(circle)
    

    

    
