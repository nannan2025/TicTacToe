from TicTacToeGameState import TicTacToeGameState

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def main():
    # Initialize an empty Tic-Tac-Toe board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_state = TicTacToeGameState(board)
    player = 'X'

    while not game_state.is_terminal():
        print("Current Board:")
        print_board(game_state.board)

        # Get user input for the next move
        row = int(input("Enter the row number (0, 1, 2): "))
        col = int(input("Enter the column number (0, 1, 2): "))

        # Check if the move is valid
        if game_state.board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue

        # Update the board with the player's move
        game_state.board[row][col] = player

        # Switch players
        player = 'O' if player == 'X' else 'X'

    print("Final Board:")
    print_board(game_state.board)

    # Print game result
    if game_state.utility() == 1:
        print("Player 0 wins!")
    elif game_state.utility() == -1:
        print("Player X wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
