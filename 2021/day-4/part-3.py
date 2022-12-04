with open('input.txt') as f: lines = f.read()


draws, *boards = lines.split('\n\n')
boards = [board.split() for board in boards]

def is_winning_board(board):
    for i in range(0,5):
        if (board[i*5:i*5+5] == ['*'] * 5) or (board[i::5] == ['*'] * 5):
            return True
    return False


new_boards = []
for draw in draws.split(','):
    for board in boards:
        board = ['*' if item == draw else item for item in board]
        if is_winning_board(board):
            if len(boards) == 1:
                print(sum([int(i) for i in board if i.isdigit()]) * int(draw))
                exit()
        else:
            new_boards.append(board)

    boards, new_boards = (new_boards, [])
