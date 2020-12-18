

lines = open('day-13.input').readlines()
nbf = int(lines[0])
buses = set(lines[1].strip().split(','))
buses.remove('x')
buses = [int(bus) for bus in buses]

print(nbf)
print(buses)

earliest_bus_id = 0

for i in range(nbf, nbf + max(buses)):
  for bus in buses:
    if i % bus == 0:
      earliest_bus_id = bus
      print(earliest_bus_id * (i - nbf))
      exit() 