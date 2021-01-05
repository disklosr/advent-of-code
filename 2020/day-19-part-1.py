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


#print(rules)
#print(messages)

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
        r = rules[self.id]
        if '"' in r:
            return [r[1]]
        elif '|' in r:
            options = r.split('|')
            res = []
            for option in options:
                 res += self.flatten_simple_rule(option)
            return res
        else:
            return self.flatten_simple_rule(r)

h = set(rule(0).flatten())

res = 0
for message in messages:
    if message in h:
        res += 1

print(res)