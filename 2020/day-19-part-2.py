lines = open('day-19.input')

rules= {}
messages = []

parsing_rules = True
lines = enumerate(lines)
while True:
    line = next(lines, None)
    if line == None:
        break

    line = line[1].strip()
    if line == '':
        parsing_rules = False
        continue

    if parsing_rules:
        tokens = line.split(':')
        rules[int(tokens[0])] = tokens[1].strip()

    else:
        messages.append(line)

def cart(old, new):
    res = []
    for i in range(len(old)):
        for j in range(len(new)):
            res.append(old[i] + new[j])
    return res

original_rule_8 = '42'
original_rule_11 = '42 31'


#print(rules)
#print(messages)

cache = {}

class rule:
    def __init__(self, id):
        self.id = id

    def flatten_simple_rule(self, rule_str):
        parts = [p for p in rule_str.split(' ') if p != ' ' and p != '']
        res = None
        for part in parts:
            if res == None:
                res = rule(int(part)).flatten()
            else:
                res = cart(res, rule(int(part)).flatten())
        return res
    
    def flatten(self):
        if self.id in cache:
            return cache[self.id]
            
        r = rules[self.id]
        if '"' in r:
            cache[self.id] = [r[1]]
            return [r[1]]
        elif '|' in r:
            options = r.split('|')
            res = []
            for option in options:
                 res += self.flatten_simple_rule(option)
            cache[self.id] = res
            return res
        else:
            cache[self.id] = self.flatten_simple_rule(r)
            return cache[self.id]

dim = len(rule(42).flatten()[0])
rule(31).flatten()

for rule in cache:
    cache[rule] = set(cache[rule])

res = 0
for msg in messages:
    if len(msg) % dim != 0:
        continue
    for i in cache[42]:
        for j in cache[31]:
            if msg.startswith(i) and msg.endswith(j):
                res += 1

print(len(messages))
print(res)

possibilities = []
for i in range(1, 20, 1):
    for j in range(2, 20, 2):
        if i + j < 13:
            possibilities.append((i,j))

def matches_possibility(message, possibility):
    i = possibility[0]
    j = possibility[1]
    m = message

    #check if msg matches i * 42
    for ii in range(i):
        if len(m) < dim:
            return False
        if m[0:dim] not in cache[42]:
            return False # message does not match this possibility
        else:
            m = m[dim:]
    
    #check if msg matches j/2 * 42
    for jj in range(int(j/2)):
        if len(m) < dim:
            return False
        if m[0:dim] not in cache[42]:
            return False # message does not match this possibility
        else:
            m = m[dim:]

    #check if msg matches j/2 * 31
    for jj in range(int(j/2)):
        if len(m) < dim:
            return False
        if m[0:dim] not in cache[31]:
            return False # message does not match this possibility
        else:
            m = m[dim:]

    #if we arrive here means it's a match
    if len(m) == 0:
        return True
    return False

res = 0
for m in messages:
    for p in possibilities:
        if matches_possibility(m, p):
            res += 1
            break
    
print(res)
# 268 start with 42 and ends with 31

# 0: 8 11
# 8: 42 42 42 42 ...
# 11: 42 31 | 42 42 31 31

# 1,2
# 1,4
# 1,6
# 1,8