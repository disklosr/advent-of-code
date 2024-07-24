def is_part(pos, engine):
    adjs = [1j,1+1j]
    for k in range(3):
        for d in adjs[-2:]:
            adjs.append(d * 1j)

    tl = len(engine)
    tc = len(engine[0])

    for delta in adjs:
        t = pos + delta
        if 0 <= t.real < tl and 0 <= t.imag < tc:
            if engine[int(t.real)][int(t.imag)] not in "0123456789.":
                return True

    return False


res = 0

engine = []

for line in open('input.txt'):
    engine.append(line.strip())

tl = len(engine)
tc = len(engine[0])


cur = ''
part = False
for l in range(tl):
    if part:
        res += int(cur)
    cur = ''
    part = False
    for c in range(tc):
        #print((l,c))
        if engine[l][c] not in "1234567890":
            if part:
                res += int(cur)
            cur = ''
            part = False
        else:
            cur += engine[l][c]
            if not part:
                part = is_part(complex(l,c), engine)
            


print(res)