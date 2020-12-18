import re
file = open('day-2.input')



def count_char(input, char_to_count):
  count = 0
  for char in input:
    if char == char_to_count:
      count += 1
  return count

valid_passwords_count = 0

for line in file:
  fragments = re.split(': |-| ', line)
  low = int(fragments[0])
  high = int(fragments[1])
  letter = fragments[2]
  password = fragments[3]

  count = count_char(password, letter)
  if count <= high and count >= low:
    valid_passwords_count += 1

print(valid_passwords_count)
