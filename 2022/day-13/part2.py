import functools

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

# Compare the case when right and left are both arrays
def comp(left, right):
    if type(left) == int and type(right) == int:
        return None if left == right else left < right
    elif type(left) == int and type(right) == list:
        return comp_arr([left], right)
    elif type(left) == list and type(right) == int:
        return comp_arr(left, [right])
    elif type(left) == list and type(right) == list:
        return comp_arr(left, right)

# Custom compare function adaptor so it works with Python
def pcomp(left, right):
    res = comp(left, right)
    return 1 if res == True else -1 if res is False else 0

right_order_idx = []
for idx, pair in enumerate(pairs):
    l,r = pair
    if comp(l,r) == True:
        right_order_idx.append(idx)

# Make pairs in right order
for idx in range(len(pairs)):
    if idx not in right_order_idx:
        l,r = pairs[idx]
        pairs[idx] = (r,l)

# Add divider packets to the mix
pairs.append(([[2]],[[6]]))

# Merge all pairs into one single list
merged = []
for pair in pairs:
    merged.append(pair[0])
    merged.append(pair[1])

# Sort merged list using adaptor function
merged.sort(key=functools.cmp_to_key(lambda a,b: pcomp(a, b)))

print(merged.index([[2]]) * merged.index([[6]]))