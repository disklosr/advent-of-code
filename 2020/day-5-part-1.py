import math
file = open('day-5.input')

result = 0

# F, ==> lower half ==> [min, math.floor((max - min) / 2)]
# B,R ==> upper half

def get_row(expression):
  min = 0
  max = 127
  
  for i in range(7):
    selector = expression[i]
    if selector == 'F':
      max = math.floor((max+min)/ 2)
    elif selector == 'B':
      min = math.ceil((max + min) / 2)

  return max

def get_column(expression):
  min = 0
  max = 7
  
  for i in range(3):
    selector = expression[i]
    if selector == 'L':
      max = math.floor((max+min)/ 2)
    elif selector == 'R':
      min = math.ceil((max + min) / 2)

  return max

def get_seat_id(seat_row, seat_column):
  return 8 * seat_row + seat_column

for line in file:
  line = line.strip()
  seat_row = get_row(line[0:7])
  seat_column = get_column(line[-3:])
  if result < get_seat_id(seat_row, seat_column):
    result = get_seat_id(seat_row, seat_column)


print(result)