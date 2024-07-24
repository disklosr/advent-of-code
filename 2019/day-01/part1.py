total=0

for line in open('input.txt'):
    mass = int(line.strip())
    fuel_req = mass // 3 - 2
    total += fuel_req

print(total)
