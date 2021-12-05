file = open('./input.txt', 'r')
lines = file.read().split('\n\n')

random_numbers = map(lambda x: int(x), lines[0].split(','))

def check_row(row):
  checked_elements = filter(lambda x: x[1], row)
  return len(checked_elements) == len(row)

def check_column(board, index):
  checked_elements = filter(lambda x: x[index][1], board)
  return len(checked_elements) == len(board)

boards = []
for index in range(1, len(lines)):
  board = []
  board_list = lines[index].splitlines()
  for board_string in board_list:
    board_line = []
    for board_index in range(0, 5):
      board_line.append([int(board_string[board_index * 3: board_index * 3 + 2]), False])
    board.append(board_line)
  boards.append(board)

found_row = False
found_col = False
winning_board = -1
winning_number = -1
for number in random_numbers:
  for index, board in enumerate(boards):
    for line in board:
      for x, element in enumerate(line):
        if element[0] == number:
          element[1] = True
          found_row = check_row(line)
          found_col = check_column(board, x)
          if found_row or found_col:
            winning_board = index
            winning_number = number
            break
    if found_row or found_col:
      break
  if found_row or found_col:
    break

unmarked = 0
for line in boards[winning_board]:
  for element in line:
    if not element[1]:
      unmarked += element[0]

print(unmarked * winning_number)