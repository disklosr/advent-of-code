lines = open('input.txt')

def is_inside(first, second):
    if int(first.split('-')[0]) <= int(second.split('-')[0]) and int(first.split('-')[1]) >= int(second.split('-')[1]):
        return True
    return False

sum = 0

for line in lines:
    left,right = line.strip().split(',')
    if is_inside(left, right) or is_inside(right, left):
        sum += 1

print(sum)


