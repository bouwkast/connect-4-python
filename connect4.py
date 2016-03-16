from objects.game import Game
import sys


def main():
    connect = Game()

    if len(sys.argv) == 4:
        connect = Game(sys.argv[1], sys.argv[2], sys.argv[3])

    player = 0
    winner = False
    connect.print_board()
    while not winner:
        column = None
        result = 0
        while column is None:
            try:
                column = raw_input("Please enter a column to place a token: ")
                result = connect.put_token(int(column), player)
            except ValueError:
                print("Error! Please enter an integer to place a token")

        if result == 1:
            print("Token successfully placed in column " + column)
            player += 1
            player %= 2
            connect.print_board()
        else:
            print("Sorry, can't place a token in column " + column)
            connect.print_board()
        is_winner = connect.check_winner()
        if is_winner != -1:
            print("Here")
            print("Congratulations! Player " + str(is_winner) + " has won!")
            winner = True
            connect.print_board()
            break;
        is_full = connect.is_board_full()
        if is_full != 0:
            print("Tie game, the board is full.")
            connect.print_board()
            break;


if __name__ == '__main__':
    main()
