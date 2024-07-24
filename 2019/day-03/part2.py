f = open('input.txt')
wire1 = next(f).split(',')
wire2 = next(f).split(',')

d1 = set()
d2 = set()

cur = 0
counter = 1
for move in wire1:
    di, value = (move[0], int(move[1:]))
    dxy = 1 if di == 'R' else 1j if di == 'U' else -1 if di == 'L' else -1j if di == 'D' else 0
    #print((di,value,dxy))
    #input()
    for i in range(value):
        d1.add((cur + dxy, counter))
        cur += dxy
        counter += 1

cur = 0
counter = 1
for move in wire2:
    di, value = (move[0], int(move[1:]))
    dxy = 1 if di == 'R' else 1j if di == 'U' else -1 if di == 'L' else -1j if di == 'D' else 0
    for i in range(value):
        d2.add(cur + dxy)
        cur = cur + dxy

res = min([abs(i.real) + abs(i.imag) for i in d1.intersection(d2)])
print(res)