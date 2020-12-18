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

all_seats =[]
min_found_seat_row = 127
max_found_seat_row = 0

for row in range(1,126): #exclude very front and very back rows
  for column in range(8):
    all_seats.append((row, column))

for line in file:
  line = line.strip()
  seat_row = get_row(line[0:7])
  if seat_row < min_found_seat_row:
    min_found_seat_row = seat_row
  if seat_row > max_found_seat_row:
    max_found_seat_row = seat_row
    
  seat_column = get_column(line[-3:])
  all_seats.remove((seat_row, seat_column))

for (row, column) in all_seats[:]:
  if row < min_found_seat_row + 1:
    all_seats.remove((row, column))
  if row > max_found_seat_row - 1:
    all_seats.remove((row, column))

print(min_found_seat_row)
print(max_found_seat_row)

found_seat = all_seats[0]
result = get_seat_id(found_seat[0], found_seat[1])

print(result)