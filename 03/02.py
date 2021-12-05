file = open('./input.txt', 'r')
lines = file.read().splitlines()

def find_rating(lines, pos, rating):
  index0 = []
  index1 = []
  for line in lines:
    if line[pos] is '0':
      index0.append(line)
    else:
      index1.append(line)
  
  keep = []
  if len(index1) > len(index0) and rating is 'oxygen' or len(index1) == len(index0) and rating is 'oxygen' or len(index1) < len(index0) and rating is 'co2':
    keep = index1
  else:
    keep = index0

  if len(keep) > 1:
    pos += 1
    keep = find_rating(keep, pos, rating)
  
  return keep

oxygen = find_rating(lines, 0, 'oxygen')
print(oxygen[0])

co2 = find_rating(lines, 0, 'co2')
print(co2[0])

result = int(oxygen[0], 2) * int(co2[0], 2)
print(result)