from itertools import product
lines = open('input.txt')

#  aaaa
# b    c
# b    c
#  dddd
# e    f
# e    f
#  gggg

zero = 'abcefg'
one = 'cf'
two = 'acdeg'
three = 'acdfg'
four = 'bcdf'
five = 'abdfg'
six = 'abdefg'
seven = 'acf'
eight = 'abcdefg'
nine = 'abcdfg'

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


numbers = set([zero, one, two, three, four, five, six, seven, eight, nine])
nbs = [zero, one, two, three, four, five, six, seven, eight, nine]


lines = [line.strip() for line in lines]
result = 0


def decoded(possibilities):
    for i in possibilities.values():
        if len(i) != 1:
            return False


def improve(possibilities, signal, candidates):
    if possibilities[signal] == []:
        possibilities[signal] += candidates
    else:
        return


count = 0
found_perm = None
for line in lines:
    wires, segments = line.split('|')
    wires, segments = (wires.split(), segments.split())

    possibilities = {
        'a': [],
        'b': [],
        'c': [],
        'd': [],
        'e': [],
        'f': [],
        'g': [],
    }

    while decoded(possibilities) == False:
        available = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        for comb in sorted(wires, key=len):
            #print(comb)
            if len(comb) == 2:  # digit 1
                for signal in comb:
                    improve(possibilities, signal, set(['c', 'f']) & available)
                available -= set(['c', 'f'])
            elif len(comb) == 3:  # digit 7
                for signal in comb:
                    improve(possibilities, signal, set(['a', 'c', 'f']) & available)
                available -= set(['a', 'c', 'f'])
            elif len(comb) == 4:  # digit 4
                for signal in comb:
                    improve(possibilities, signal, set(['b', 'c', 'd', 'f']) & available)
                available -= set(['b', 'c', 'd', 'f'])

            else:
                for signal in comb:
                    improve(possibilities, signal, available)
        available = {}

        permutations = []

        for v in letters :
            if permutations == []:
                permutations = possibilities[v]
            else:
                p = product(permutations, possibilities[v])
                permutations = [''.join(e) for e in p]
        #print(possibilities)
        #print(permutations)

        for p in permutations:
            if len(p) != len(set(p)):
                continue
            for seg in segments:
                tseg = ''.join(map(lambda x: p[letters.index(x)], seg))
                tseg = ''.join(sorted(tseg))
                #print((p, seg, tseg))
                if tseg not in numbers:
                    break
            else:
                found_perm = p
                nbr = ''
                for seg in segments:
                    tseg = ''.join(map(lambda x: p[letters.index(x)], seg))
                    tseg = ''.join(sorted(tseg))
                    nbr += str(nbs.index(tseg))

                result += int(nbr)
                break
        if found_perm != None:
            found_perm = None
            break
            #input()

print(result)
