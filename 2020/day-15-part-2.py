def run():

  lines = open('day-15.input')

  numbers = []
  for line in lines:
    line = line.strip()
    numbers = [int(num) for num in line.split(',')]


  spoken = {}
  last = None

  curr_turn = 1

  for turn in range(len(numbers)):
    spoken[numbers[turn]] = curr_turn
    last = numbers[turn]
    curr_turn += 1

  while curr_turn <= 30000000:
    say = 0 if last not in spoken else curr_turn - 1 - spoken[last]
    spoken[last] = curr_turn - 1
    last = say
    curr_turn += 1

  print(last)

run()