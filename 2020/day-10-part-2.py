import math

lines = open('day-10.input')

numbers = [int(line) for line in lines]
numbers.sort()
print(len(numbers))
print(numbers)
numbers = [0] + numbers + [numbers[-1] + 3]

start = 0
end = numbers[-1]

result = None
sols = []

def solve(sol, input, output, numbers):
  if input == output:
    sols.append(sol)
    return True
  
  else:
    sub_numbers = numbers[:]

    if input + 3 in numbers:
      sub_numbers.remove(input + 3)
      solve(sol + [input + 3], input + 3, output, sub_numbers)
    
    elif input + 2 in numbers:
      sub_numbers.remove(input + 2)
      solve(sol + [input + 2], input + 2, output, sub_numbers)

    elif input + 1 in numbers:
      sub_numbers.remove(input + 1)
      solve(sol + [input + 1], input + 1, output, sub_numbers)
    

    elif numbers[0] > input + 3:
      return False

solve([0], 0, numbers[-1], numbers)

comb = 1
keep = set()
for (cur, next) in list(zip(numbers[:-1], numbers[1:])):
  if next - cur == 3:
    keep.add(next)
    keep.add(cur)


      


keep = [0] + list(keep)
keep.sort()
print(len(keep))
print(keep)

result = 1
for (min, max) in zip(keep[:-1], keep[1:]):
  t = len([num for num in numbers if num > min and num < max])
  if t == 0:
    continue
  tmp = int(math.pow(2, t))
  if (max - min) > 3:
    tmp -= 1
  result *= tmp


print(result)



#print(sols)
#print(len(numbers))
#print(len(sols[0]))
