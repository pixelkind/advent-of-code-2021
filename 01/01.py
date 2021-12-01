file = open('./input.txt', 'r')
string = file.read()
lines = string.split()
int_lines = list(map(lambda x: int(x), lines))

result = 0
last_value = 10000
for value in int_lines:
  if last_value < value:
    result += 1
  last_value = value

print(result)