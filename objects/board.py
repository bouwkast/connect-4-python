

class Board:
    num_rows = 6  # Standard height for a connect 4 board
    num_cols = 7  # Standard width for a connect 4 board
    grid = None  # Will be the 2-D board to hold all respective values

    def __init__(self, num_rows, num_cols):
        self.grid = []
        if num_rows < 2 or num_rows > 100:
            print("Error! The number of rows must be between 2 and 100. \n")
            quit()
        else:
            self.num_rows = num_rows
        if num_cols < 2 or num_cols > 100:
            print("Error! The number of columns must be between 2 and 100asdfasdf. \n")
            quit()
        else:
            self.num_cols = num_cols
        for row in xrange(0, self.num_rows):
            self.grid.append([])
            for col in xrange(0, self.num_cols):
                self.grid[row].append(-1)

    def cell_at(self, row, col):
        if row < 0 or row >= self.num_rows:
            print("Error! Can't return that cell because the row " + row + " is out of bounds")
            quit()
        if col < 0 or col >= self.num_cols:
            print("Error! Can't return that cell because the column " + col + " is out of bounds")
            quit()
        return self.grid[row][col]

    def place_token(self, col, player):
        if col < 0 or col >= self.num_cols:
            print("Error! You must place a token on the board.")
        else:
            for row in xrange(self.num_rows - 1, -1, -1):
                if self.grid[row][col] == -1:
                    self.grid[row][col] = player
                    return 1
                if row == 0:
                    print("That column is full")
                    return 0
        return 0  # Was not able to place the token

