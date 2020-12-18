lines = open('day-10.input')

numbers = [int(line) for line in lines]
numbers.sort()
numbers = [0] + numbers + [numbers[-1] + 3]

start = 0
end = numbers[-1]

result = None
sols = []

def solve(sol, input, output, numbers):
  print((input, output))
  if input == output:
    sols.append(sol)
    return True
  
  else:
    sub_numbers = numbers[:]

    if input + 1 in numbers:
      sub_numbers.remove(input + 1)
      return solve(sol + [input + 1], input + 1, output, sub_numbers)
    
    elif input + 2 in numbers:
      sub_numbers.remove(input + 2)
      return solve(sol + [input + 2], input + 2, output, sub_numbers)
    

    if input + 3 in numbers:
      sub_numbers.remove(input + 3)
      return solve(sol + [input + 3], input + 3, output, sub_numbers)
    
    else:
      return False

solve([0], 0, numbers[-1], numbers)
print(sols)

print(len(numbers))
print(len(sols[0]))

diff1 = 0
diff3 = 0

for i in range(0, len(sols[0]) - 1):
  diff = sols[0][i+1] - sols[0][i]
  if diff == 1:
    diff1 += 1
  elif diff == 3:
    diff3 += 1


print(diff1 * diff3)
