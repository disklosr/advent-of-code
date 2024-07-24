total=0

def compute_fuel_req(mass):
    req = mass // 3 - 2
    if req <= 0:
        return 0
    else:
        return req + compute_fuel_req(req)

for line in open('input.txt'):
    mass = int(line.strip())
    fuel_req = compute_fuel_req(mass)
    total += fuel_req

print(total)
