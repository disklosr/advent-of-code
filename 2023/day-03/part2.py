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
            if engine[int(t.real)][int(t.imag)] == "*":
                return (True, t)

    return (False, None)

def add(pos, value, d):
    if pos not in d:
        d[pos] = []
    d[pos].append(value)

engine = []

for line in open('input.txt'):
    engine.append(line.strip())

tl = len(engine)
tc = len(engine[0])

d = {}

cur = ''
part = (False, None)
for l in range(tl):
    if part[0]:
        add(part[1], int(cur), d)
    cur = ''
    part = (False, None)
    for c in range(tc):
        #print((l,c))
        if engine[l][c] not in "1234567890":
            if part[0]:
                add(part[1], int(cur), d)
            cur = ''
            part = (False, None)
        else:
            cur += engine[l][c]
            if not part[0]:
                part = is_part(complex(l,c), engine)
            
res = 0
for k,v in d.items():
    if len(v) == 2:
        res += v[0] * v[1]

print(res)