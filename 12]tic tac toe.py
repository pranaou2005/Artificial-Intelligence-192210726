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
            row = int(input(f"Player {player}, enter row number (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column number (1-3): ")) - 1
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Please enter row and column numbers between 1 and 3.")
        except ValueError:
            print("Please enter valid row and column numbers.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        row, col = get_input(player)

        if board[row][col] != " ":
            print("That cell is already occupied. Please choose another.")
            continue

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    play_game()
