lines = open('input.txt')

def overlaps(first, second):
    if len(set(first).intersection(set(second))) > 0:
        return True
    return False

sum = 0

for line in lines:
    left,right = line.strip().split(',')

    left = left.split('-')
    right = right.split('-')

    first = range(int(left[0]), int(left[1]) + 1)
    second = range(int(right[0]), int(right[1]) + 1)
    if overlaps(first, second):
        sum += 1

print(sum)


