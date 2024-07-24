import re
lines = open('input.txt')

res = 0
d = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
for line in lines:
    print(line)
    
        
    digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',line)
    #digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
    print(digits)
    digits = [digits[0],digits[-1]]

    for i in range(len(digits)):
        if digits[i] in d:
            digits[i] = d[digits[i]]
    
    #print(digits)
    #input()
    res += int(f'{digits[0]}{digits[-1]}')

print(res)