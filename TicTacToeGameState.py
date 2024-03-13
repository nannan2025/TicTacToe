class TicTacToeGameState:
  def __init__(self, board):
      self.board = board

  def is_terminal(self):
      # Check if the game is over (i.e., if there's a winner or the board is full)
      return self._check_winner() or self._is_board_full()

  def _check_winner(self):
      # Helper function to check if there's a winner
      for row in self.board:
          if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
              return True  # Row win
      for col in range(3):
          if all(self.board[row][col] == 'X' for row in range(3)) or \
                  all(self.board[row][col] == 'O' for row in range(3)):
              return True  # Column win
      if all(self.board[i][i] == 'X' for i in range(3)) or \
              all(self.board[i][i] == 'O' for i in range(3)):
          return True  # Diagonal win
      if all(self.board[i][2 - i] == 'X' for i in range(3)) or \
              all(self.board[i][2 - i] == 'O' for i in range(3)):
          return True  # Anti-diagonal win
      return False

  def _is_board_full(self):
      # Helper function to check if the board is full (i.e., no more moves possible)
      return all(cell != ' ' for row in self.board for cell in row)

  def utility(self):
      # Calculate the utility value of the terminal state
      if self._check_winner():
          return 1 if self._check_winner() == 'X' else -1
      else:
          return 0  # Draw
