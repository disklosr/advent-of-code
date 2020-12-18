file = open('day-4.input')

result = None
passports= []
valid_passeports = []

def is_valid_passport(passport):
  for field in ['byr', 'iyr', 'eyr', 'hgt' ,'hcl', 'ecl', 'pid']:
    if field not in passport:
      return False
  return True

passport = {}
for line in file:
  print(len(line)) 
  if line.strip() == '':
    print(passport)
    if is_valid_passport(passport):
      valid_passeports.append(passport)
    passports.append(passports)
    passport = {}
  else:
    kvps = line.strip().split(' ')
    for kvp in kvps:
      passport[kvp[0:3]] = kvp[4:]

#print(valid_passeports)
result = len(valid_passeports)

print(len(passports))
print(result)