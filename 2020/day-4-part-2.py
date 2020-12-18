import re
file = open('day-4.input')

result = None
passports= []
valid_passeports = []

def is_valid_byr(value):
  return len(value) == 4 and value.isdigit() and int(value) >= 1920 and int(value) <= 2002

def is_valid_iyr(value):
  return len(value) == 4 and value.isdigit() and int(value) >= 2010 and int(value) <= 2020

def is_valid_eyr(value):
  return len(value) == 4 and value.isdigit() and int(value) >= 2020 and int(value) <= 2030

def is_valid_hgt(value):
  unit = value[-2:]
  amount = value[:-2]
  if unit == 'cm' and amount.isdigit() and int(amount) >= 150 and int(amount) <= 193:
    return True
  elif unit == 'in' and amount.isdigit() and int(amount) >= 59 and int(amount) <= 76:
    return True
  else:
    return False

def is_valid_hcl(value):
  return re.match('^#[0-9a-f]{6}$', value)

def is_valid_ecl(value):
  return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_valid_pid(value):
  return re.match('^[0-9]{9}$', value)
  

validators = {
  'byr': is_valid_byr, 
  'iyr': is_valid_iyr, 
  'eyr': is_valid_eyr, 
  'hgt': is_valid_hgt, 
  'hcl': is_valid_hcl, 
  'ecl': is_valid_ecl, 
  'pid': is_valid_pid
}

def is_valid_passport(passport):
  for field in validators:
    if field not in passport:
      return False
    elif not validators[field](passport[field]):
      return False
  return True

passport = {}
for line in file:
  if line.strip() == '':
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

print(result)