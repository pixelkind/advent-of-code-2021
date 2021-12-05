file = open('./input.txt', 'r')
lines = file.read().split('\n\n')

random_numbers = map(lambda x: int(x), lines[0].split(','))

def check_row(row):
  checked_elements = filter(lambda x: x[1], row)
  return len(checked_elements) == len(row)

def check_column(board, index):
  checked_elements = filter(lambda x: x[index][1], board)
  return len(checked_elements) == len(board)

# Create 2d lists out of the board strings
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

# Playing the bingo numbers
found_row = False
found_col = False
winning_boards = []
winning_board = -1
winning_number = -1
for number in random_numbers:
  for index, board in enumerate(boards):
    if index in winning_boards:
      continue
    for line in board:
      for x, element in enumerate(line):
        if element[0] == number:
          element[1] = True
          found_row = check_row(line)
          found_col = check_column(board, x)
          if found_row or found_col:
            winning_boards.append(index)
            print(winning_boards)
            winning_board = index
            winning_number = number
            if len(winning_boards) == len(boards):
              break
    if len(winning_boards) == len(boards):
      break
  if len(winning_boards) == len(boards):
    break

print(winning_board)
unmarked = 0
for line in boards[winning_board]:
  for element in line:
    if not element[1]:
      unmarked += element[0]

print(unmarked * winning_number)