import math

# Define a utility function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Define a utility function to check if the game is over
def is_game_over(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != " ":
            return True

    # Check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != " ":
        return True
    if len(set([board[i][2-i] for i in range(3)])) == 1 and board[0][2] != " ":
        return True

    # Check if board is full
    if all(board[row][col] != " " for row in range(3) for col in range(3)):
        return True

    return False

# Define a utility function to evaluate the board state
def evaluate(board):
    # Check rows
    for row in board:
        if row.count("X") == 3:
            return 10
        elif row.count("O") == 3:
            return -10

    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count("X") == 3:
            return 10
        elif [board[row][col] for row in range(3)].count("O") == 3:
            return -10

    # Check diagonals
    if [board[i][i] for i in range(3)].count("X") == 3 or [board[i][2-i] for i in range(3)].count("X") == 3:
        return 10
    elif [board[i][i] for i in range(3)].count("O") == 3 or [board[i][2-i] for i in range(3)].count("O") == 3:
        return -10

    return 0

# Define the Alpha-Beta Pruning algorithm
def alpha_beta_pruning(board, depth, alpha, beta, is_maximizer):
    if depth == 0 or is_game_over(board):
        return evaluate(board)

    if is_maximizer:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = alpha_beta_pruning(board, depth-1, alpha, beta, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = alpha_beta_pruning(board, depth-1, alpha, beta, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Define the function to find the optimal move using Alpha-Beta Pruning
def find_best_move(board, depth):
    best_eval = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = alpha_beta_pruning(board, depth-1, -math.inf, math.inf, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Define the function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    depth = 4  # Adjust depth based on the game complexity

    while not is_game_over(board):
        # Player's move
        row, col = map(int, input("Enter row and column number (1-3) for your move: ").split())
        row -= 1
        col -= 1
        if board[row][col] != " ":
            print("That cell is already occupied. Please choose another.")
            continue
        board[row][col] = "O"
        print_board(board)

        if is_game_over(board):
            break

        # Computer's move
        print("Computer's move:")
        comp_row, comp_col = find_best_move(board, depth)
        board[comp_row][comp_col] = "X"
        print_board(board)

    print("Game over!")

if __name__ == "__main__":
    play_game()
