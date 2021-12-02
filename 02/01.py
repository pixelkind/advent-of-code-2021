file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

# forward, down, up

horizontal = 0
depth = 0

for line in lines:
  command = line.split(' ')
  if 'forward' in line:
    horizontal += int(command[1])
  elif 'down' in line:
    depth += int(command[1])
  elif 'up' in line:
    depth -= int(command[1])

print(horizontal * depth)