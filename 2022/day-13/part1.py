lines = open('input.txt')

pairs = []
tmp = []
for line in lines:
    line = line.strip()
    if line == '':
        pairs.append((tmp[0], tmp[1]))
        tmp = []

    else:
        tmp.append(eval(line))

pairs.append((tmp[0], tmp[1]))

print(len(pairs))

def comp_arr(left, right):
    if len(right) == len(left) == 0:
        print('Continue next comparaison')
        return None
    for i in range(len(left)):
        if i >= len(right):
            print('Right run out of items')
            return False
        c = comp(left[i], right[i])
        if c != None:
            return c
    
    if len(right) > len(left):
        print('Left run out of items')
        return True
    else:
        print('Continue next comparaison')
        return None


def comp(left, right):
    print('comparing', left, 'and', right)
    if type(left) == int and type(right) == int:
        return None if left == right else left < right
    elif type(left) == int and type(right) == list:
        return comp_arr([left], right)
    elif type(left) == list and type(right) == int:
        return comp_arr(left, [right])
    elif type(left) == list and type(right) == list:
        return comp_arr(left, right)

right_order_idx = []
for idx, pair in enumerate(pairs):
    l,r = pair
    print('########################')
    if comp(l,r) == True:
        print('Right order')
        right_order_idx.append(idx + 1)

print(right_order_idx)
print(sum(right_order_idx))