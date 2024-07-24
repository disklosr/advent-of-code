rgb = [12,13,14]

all_games = set()
impossible_games = set()
for line in open('input.txt'):
    (game_id, info) = line.split(':')
    game_id = int(game_id.split(' ')[1])
    all_games.add(game_id)
    sets = info.split(';')
    for set in sets:
        current_rgb = [0,0,0]
        outcome = set.split(', ')
        for s in outcome:
            s = s.strip()
            (count, colour) = s.split(' ')
            idx = 0 if colour == 'red' else 1 if colour == 'green' else 2
            if rgb[idx] < int(count):
                print('impossible: ',game_id, idx, count)
                impossible_games.add(game_id)
                break

print(sum(all_games - impossible_games))

            
