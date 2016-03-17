from objects.game import Game
import sys


def main():
    connect = Game()

    if len(sys.argv) == 4:
        try:
            connect = Game(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        except ValueError:
            print("ValueError - please enter integers as a parameters. Exiting.")
            quit()

    player = 0
    connect.print_board()
    while True:
        user_input = None
        result = 0
        while user_input is None:
            try:
                user_input = raw_input("Please enter a column to place a token: ")
                if user_input.lower() == "save":
                    connect.save_game()
                elif user_input.lower() == "load":
                    connect = connect.load_game()
                result = connect.put_token(int(user_input), player)
            except ValueError:
                print("Error! Please enter an integer to place a token")

        if result == 1:
            print("Token successfully placed in column " + user_input)
            player += 1
            player %= 2
            connect.player = player
            connect.print_board()
        else:
            print("Sorry, can't place a token in column " + user_input)
            connect.print_board()
        is_winner = connect.check_winner()
        if is_winner != -1:
            print("Here")
            print("Congratulations! Player " + str(is_winner) + " has won!")
            connect.print_board()
            break;
        is_full = connect.is_board_full()
        if is_full != 0:
            print("Tie game, the board is full.")
            connect.print_board()
            break


if __name__ == '__main__':
    main()
