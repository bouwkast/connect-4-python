import pickle
import sys
from board import Board


class Game:
    num_rows = 3
    num_cols = 3
    num_win = 3
    board = None
    player = -1

    def __init__(self, num_rows=3, num_cols=3, num_win=3):
        if num_rows < 2 or num_rows > 100:
            print("Error! The number of rows must be between 2 and 100. \n")
            quit()
        else:
            self.num_rows = num_rows
        if num_cols < 2 or num_cols > 100:
            print("Error! The number of columns must be between 2 and 100. \n")
            quit()
        else:
            self.num_cols = num_cols
        if num_win > num_cols or num_win > num_rows:
            print("Error! The number in a row to win must be less than both the number of rows and columns. \n")
            quit()
        else:
            self.num_win = num_win

        self.board = Board(self.num_rows, self.num_cols)

    def put_token(self, col, player):
        try:
            column = int(col)
            return self.board.place_token(column, player)
        except ValueError:
            print("Error! Couldn't determine column entered, please make sure to use an integer within the bounds.")
            return -1

    def print_board(self):
        for row in xrange(0, self.num_rows):
            for col in xrange(0, self.num_cols):
                sys.stdout.write(str(self.board.cell_at(row, col)))
                sys.stdout.write("\t")
            print
        print

    def horizontal_check(self):
        for row in xrange(0, self.num_rows):
            num_tokens = 1
            for col in xrange(0, self.num_cols):
                player = self.board.cell_at(row, col)
                if player != -1 and col < self.num_cols - 1:
                    if self.board.cell_at(row, col + 1) == player:
                        num_tokens += 1
                    else:
                        num_tokens = 1
                else:
                    num_tokens = 1
                if num_tokens == self.num_win:
                    winner = int(self.board.cell_at(row, col))
                    return winner
        return -1  # no winner

    def vertical_check(self):
        for col in xrange(0, self.num_cols - 1):
            num_tokens = 1
            for row in xrange(0, self.num_rows - 1):
                player = self.board.cell_at(row, col)
                if player != -1:
                    if self.board.cell_at(row + 1, col) == player:
                        num_tokens += 1
                    else:
                        num_tokens = 1
                else:
                    num_tokens = 1

                if num_tokens == self.num_win:
                    winner = int(self.board.cell_at(row, col))
                    return winner
        return -1  # no winner

    def down_right_check(self):
        for row in xrange(0, self.num_rows - 1):
            for col in xrange(0, self.num_cols - 1):
                num_tokens = 1
                y = col
                for x in xrange(row, self.num_rows - 1):
                    player = self.board.cell_at(x, y)
                    if player != -1 and x < self.num_rows - 1 and y < self.num_cols - 1:
                        if self.board.cell_at(x + 1, y + 1) == player:
                            num_tokens += 1
                        else:
                            num_tokens = 1
                    else:
                        num_tokens = 1
                    if num_tokens == self.num_win:
                        winner = int(self.board.cell_at(x, y))
                        return winner
                    y += 1
                    if y > self.num_cols - 2:
                        break
        return -1

    def down_left_check(self):
        for row in xrange(0, self.num_rows - 1):
            for col in xrange(0, self.num_cols - 1):
                num_tokens = 1
                y = col + 1
                for x in xrange(row, self.num_rows - 1):
                    if y < 0:
                        break
                    player = self.board.cell_at(x, y)
                    if player != -1 and y > 0:
                        if self.board.cell_at(x + 1, y - 1) == player:
                            num_tokens += 1
                        else:
                            num_tokens = 1
                    else:
                        num_tokens = 1
                    if num_tokens == self.num_win:
                        winner = int(self.board.cell_at(x, y))
                        return winner
                    y -= 1

        return -1

    def check_winner(self):
        winner = self.horizontal_check()
        if winner != -1:
            return winner
        winner = self.vertical_check()
        if winner != -1:
            return winner
        winner = self.down_left_check()
        if winner != -1:
            return winner
        winner = self.down_right_check()
        if winner != -1:
            return winner
        return -1

    def is_board_full(self):
        for row in xrange(0, self.num_rows):
            for col in xrange(0, self.num_cols):
                if self.board.cell_at(row, col) == -1:
                    return 0
        return 1

    def save_game(self):
        file_name = "connect_4_python_user_save"
        file_object = open(file_name, 'wb')
        try:
            pickle.dump(self, file_object)
            print("Saved the game")
        except pickle.PicklingError:
            print("Error saving the game - game was not saved")
        except IOError as ioe:
            print("IOError {0}".format(ioe.args))

    def load_game(self):
        file_name = "connect_4_python_user_save"

        try:
            file_object = open(file_name, 'r')
            print("Loaded the game")
            return pickle.load(file_object)
        except IOError as ioe:
            print("IOError {0}".format(ioe.args))
        except pickle.UnpicklingError:
            print("Couldn't load the game, something must be wrong with the save file")

#
# connect = Game(3, 3, 2)
# connect.print_board()
# connect.put_token(0, 1)
# connect.print_board()
# connect.put_token(1, 0)
# connect.print_board()
# connect.put_token(0, 1)
# connect.print_board()
# connect.put_token(0, 1)
# connect.print_board()
# print(connect.check_winner())
