file = open('./input.txt', 'r')
lines = file.read().splitlines()

cols = []
for line in lines:
  for index, bin in enumerate(line):
    if len(cols) < index + 1:
      cols.append(list())
    cols[index].append(int(bin))

gamma = list()
epsilon = list()

for col in cols:
  bin0 = col.count(0)
  bin1 = col.count(1)
  if bin0 > bin1:
    gamma.append(0)
    epsilon.append(1)
  else:
    gamma.append(1)
    epsilon.append(0)

gamma_decimal = int(''.join(str(e) for e in gamma), 2)
epsilon_decimal = int(''.join(str(e) for e in epsilon), 2)
result = gamma_decimal * epsilon_decimal
print(result)