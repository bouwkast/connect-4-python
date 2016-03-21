#!/usr/bin/env python

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

    player = lambda p: (p + 1) % 2  # lambda function to change the player's turn
    print("Creating a board of size " + str(connect.num_rows) + "x" + str(connect.num_cols) + " with " + str(
        connect.num_win) + " in a row to win.")
    print(
        "To save the game, simply type save. Only one save is permitted and there is no option to determine its name.")
    print("To load the game, simply type load.\n\n")

    connect.print_board()
    saved = False
    loaded = False
    while True:
        user_input = None
        result = 0
        while user_input is None:  # Want to make sure that we have some input to go off of
            try:
                user_input = raw_input("Please enter a column to place a token: ")
                if user_input.lower() == "save":
                    connect.save_game()
                    saved = True  # if they save the game we don't want to try and place a token
                    loaded = False
                    break
                elif user_input.lower() == "load":
                    connect = connect.load_game()
                    saved = False
                    loaded = True  # if they loaded the game we don't want to try and place a token, but need to print
                    break
                result = connect.put_token(int(user_input), connect.player)  # try to put the token on the board
            except ValueError:
                print("Error! Please enter an integer to place a token")
            except KeyboardInterrupt:  # occurs if something like ^C happens
                print("\nExiting the game")
                quit()

        if result == 1:  # if the token was successfully placed on the board
            print("Token successfully placed in column " + user_input)
            connect.player = player(connect.player)  # update the player change in the game
            connect.print_board()
            saved = False
            loaded = False
        elif result != 1 and not saved:
            if not loaded:
                print("Sorry, can't place a token in column " + user_input)
            connect.print_board()
        is_winner = connect.check_winner()  # want to see if one of the players have won
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
