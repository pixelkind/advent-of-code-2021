file = open('./input.txt', 'r')
string = file.read()
lines = string.split()
int_lines = list(map(lambda x: int(x), lines))

three_measurement = list()
for index in range(len(int_lines)):
  if index < len(int_lines) - 2:
    three_value = 0
    for inner_index in range(index, index + 3):
      three_value += int_lines[inner_index]
    three_measurement.append(three_value)

print(three_measurement)

result = 0
last_value = 10000

for value in three_measurement:
  if last_value < value:
    result += 1
  last_value = value

print(result)