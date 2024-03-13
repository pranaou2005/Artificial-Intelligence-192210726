def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def print_solution(board):
    for row in board:
        line = ['.'] * len(board)
        line[row] = 'Q'
        print(' '.join(line))
    print('\n')

def solve_queens(n, board, row):
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_queens(n, board, row + 1)
            board[row] = 0

def n_queens(n):
    board = [0] * n
    solve_queens(n, board, 0)

n_queens(8)
