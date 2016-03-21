# connect-4-python
An implementation of the game Connect 4 in python

To play the game simply run it from the command line with either of commands:
"./connect4.py"

or

"python connect4.py"

--without quotes

The game takes 3 additional parameters in the command line, all are integers separated by whitespace.

The first refers to the number of rows you want - between 2 to 100.
The second refers to the number of columns you want - between 2 to 100.
The third refers to the number in a row to win - must be less than or equal to the smaller of the number of rows and columns.

To play simply type in the column index starting at 0 and going to (number of columns - 1) and then press Enter.

If you want to save the game, simply type "save", without quotes, and the game will save. There is no option to specify the location or name of the save file - so there is only one.

To load the saved game simply type "load", without quotes.

To quit out of the game Ctrl + C works.
