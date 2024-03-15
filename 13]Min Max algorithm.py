def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_input(player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter row and column number (1-3): ").split())
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("Please enter row and column numbers between 1 and 3.")
        except ValueError:
            print("Please enter valid row and column numbers.")

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return -10 + depth
    elif check_winner(board, 'O'):
        return 10 - depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player_row, player_col = get_input('X')
        if board[player_row][player_col] != " ":
            print("That cell is already occupied. Please choose another.")
            continue
        board[player_row][player_col] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        comp_row, comp_col = find_best_move(board)
        board[comp_row][comp_col] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
