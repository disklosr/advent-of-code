lines = open('input.txt')

lines = [line.strip() for line in lines]

count = 0
for line in lines:
    wires, segments = line.split('|')
    wires, segments = (wires.split(), segments.split())
    
    for digit in segments:
        if len(digit) in [2, 4, 3, 7]:
            count += 1