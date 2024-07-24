rgb = [12,13,14]

res = 0
for line in open('input.txt'):
    (game_id, info) = line.split(':')
    sets = info.split(';')    
    max_rgb = [0,0,0]
    for set in sets:
        outcome = set.split(', ')
        for s in outcome:
            s = s.strip()
            (count, colour) = s.split(' ')
            idx = 0 if colour == 'red' else 1 if colour == 'green' else 2
            if max_rgb[idx] < int(count):
                max_rgb[idx] = int(count)

    print()
    res += max_rgb[0] * max_rgb[1] * max_rgb[2]

print(res)