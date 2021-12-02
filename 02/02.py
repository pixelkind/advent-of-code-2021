file = open('./input.txt', 'r')
string = file.read()
lines = string.split('\n')

# forward, down, up

horizontal = 0
depth = 0
aim = 0

for line in lines:
  command = line.split(' ')
  x = int(command[1])
  if 'forward' in line:
    horizontal += x
    depth += aim * x
  elif 'down' in line:
    aim += x
  elif 'up' in line:
    aim -= x

print(horizontal, depth)
print(horizontal * depth)