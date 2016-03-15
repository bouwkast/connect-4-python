class game:
    num_rows = 6
    num_cols = 7
    num_win = 4
    board = None
    player = 1

    def __init__(self, num_rows, num_cols, num_win):
        if num_rows < 2 or num_rows > 100:
            print("Error! The number of rows must be between 2 and 100. \n")
            quit()
        else:
            self.num_rows = num_rows
        if num_cols < 2 or enumerate > 100:
            print("Error! The number of columns must be between 2 and 100. \n")
            quit()
        else:
            self.num_cols = num_cols
        if num_win > num_cols or num_win > num_rows:
            print("Error! The number in a row to win must be less than both the number of rows and columns. \n")
            quit()
        else:
            self.num_win = num_win

    def create_board(self):
        self.board = []
        for row in range(self.num_rows):
            self.board.append([])
            for col in range(self.num_cols):
                self.board[row].append(-1)

    def place_token(self, col):
        if col < 0 or col >= self.num_cols:
            print("Error! You must place a token on the board.")
        else:
            for row in xrange(self.num_rows - 1, 0, -1):
                if self.board[row][col] == -1:
                    self.board[row][col] = self.player
                    return 1
                if row == 0:
                    print("That column is full")
                    return 0
        return 0 # Was not able to place the token



