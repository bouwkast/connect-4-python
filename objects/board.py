

class board:
    height = 6 # Standard height for a connect 4 board
    width = 7 # Standard width for a connect 4 board
    grid = None # Will be the 2-D board to hold all respective values
    def __init__(self):
        self.grid = []
        for row in range (self.height):
            self.grid.append([])
            for col in range (self.width):
                self.grid[row].append(-1)

    def __init__(self, num_rows, num_cols):
        self.grid = []
        if num_rows < 2 or num_rows > 100:
            print("Error! The number of rows must be between 2 and 100. \n")
            quit()
        else:
            self.height = num_rows
        if num_cols < 2 or enumerate > 100:
            print("Error! The number of columns must be between 2 and 100. \n")
            quit()
        else:
            self.width = num_cols
        for row in range (self.height):
            self.grid.append([])
            for col in range (self.width):
                self.grid[row].append(-1)

