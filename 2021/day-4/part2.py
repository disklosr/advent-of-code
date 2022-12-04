lines = open('input.txt')

draws = [int(i) for i in next(lines).strip().split(',')]
boards = []
current_board = []

next(lines)

for line in lines:
    line = line.strip()
    if line != '':
        current_board.append(' ' + line + ' ')
    else:
        boards.append(current_board)
        current_board = []

def mark_number(board, number):
    for i in range(0,5):
        board[i] = board[i].replace(f' {number} ', f' *{number} ')

def is_winning_board(board):
    for line in board:
        if line.count('*') == len(board):
            return True

    for i in range(0,5):
        marked_count = sum([line.split(' ')[i].count('*') for line in board])
        if marked_count == len(board):
            return True
    return False

def compute_score(board, draw):
    res = 0
    for line in board:
        res += sum([int(i) for i in line.split(' ') if i.isdigit()])
    return res * draw

def dump(board):
    for line in board:
        print(line)
    print('')

for draw in draws:
    for board in boards[:]:
        mark_number(board, draw)
        if is_winning_board(board):
            if len(boards) == 1:
                score = compute_score(board, draw)
                print(score)
                exit()
            else:
                boards.remove(board)


