lines = open('input.txt')

pairs = []
tmp = []

# Parsing loop
for line in lines:
    line = line.strip()
    if line == '':
        pairs.append((tmp[0], tmp[1]))
        tmp = []
    else:
        tmp.append(eval(line))

pairs.append((tmp[0], tmp[1]))

print(len(pairs))

# Compare the case when right and left are both arrays
def comp_arr(left, right):
    if len(right) == len(left) == 0:
        return None
    for i in range(len(left)):
        if i >= len(right):
            return False
        c = comp(left[i], right[i])
        if c != None:
            return c
    
    if len(right) > len(left):
        return True
    else:
        return None

# Compare genral case
def comp(left, right):
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
    if comp(l,r) == True:
        right_order_idx.append(idx + 1)

print(sum(right_order_idx))