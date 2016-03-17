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

    count = -1
    player = lambda p: (p + 1) % 2  # lambda function to change the player's turn
    connect.print_board()
    saved = False
    loaded = False
    while True:
        user_input = None
        result = 0
        while user_input is None:
            try:
                user_input = raw_input("Please enter a column to place a token: ")
                if user_input.lower() == "save":
                    connect.save_game()
                    saved = True
                    loaded = False
                    break
                elif user_input.lower() == "load":
                    connect = connect.load_game()
                    saved = False
                    loaded = True
                    break
                result = connect.put_token(int(user_input), player(count))
            except ValueError:
                print("Error! Please enter an integer to place a token")
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt - exiting the game")
                quit()

        if result == 1:
            print("Token successfully placed in column " + user_input)
            count += 1
            player(count)
            connect.player = player(count)
            connect.print_board()
            saved = False
            loaded = False
        elif result != 1 and not saved:
            if not loaded:
                print("Sorry, can't place a token in column " + user_input)
            connect.print_board()
        is_winner = connect.check_winner()
        if is_winner != -1:
            print("Congratulations! Player " + str(is_winner) + " has won!")
            connect.print_board()
            break
        is_full = connect.is_board_full()
        if is_full != 0:
            print("Tie game, the board is full.")
            connect.print_board()
            break


if __name__ == '__main__':
    main()
