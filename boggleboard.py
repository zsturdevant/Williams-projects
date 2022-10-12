"""
Extends the Board class with specific features required for Boggle
"""

from graphics import *
from brandom import *
from boggleletter import BoggleLetter
from board import Board

class BoggleBoard(Board):
    """Boggle Board class implements the functionality of a Boggle board.
    It inherits from the Board class and extends it by creating a grid
    of BoggleLetters, shaken appropriately to randomize play."""

    __slots__ = ['_grid', "_cubes"]

    def __init__(self, win):
        super().__init__(win, rows=4, cols=4)

        self._cubes =  [[ "A", "A", "C", "I", "O", "T" ],
                        [ "T", "Y", "A", "B", "I", "L" ],
                        [ "J", "M", "O", "Qu", "A", "B"],
                        [ "A", "C", "D", "E", "M", "P" ],
                        [ "A", "C", "E", "L", "S", "R" ],
                        [ "A", "D", "E", "N", "V", "Z" ],
                        [ "A", "H", "M", "O", "R", "S" ],
                        [ "B", "F", "I", "O", "R", "X" ],
                        [ "D", "E", "N", "O", "S", "W" ],
                        [ "D", "K", "N", "O", "T", "U" ],
                        [ "E", "E", "F", "H", "I", "Y" ],
                        [ "E", "G", "I", "N", "T", "V" ],
                        [ "E", "G", "K", "L", "U", "Y" ],
                        [ "E", "H", "I", "N", "P", "S" ],
                        [ "E", "L", "P", "S", "T", "U" ],
                        [ "G", "I", "L", "R", "U", "W" ]]
        self._grid = []
        for col in range(self._cols):
            gridCol = []
            for row in range(self._rows):
                letter = BoggleLetter(win, col, row, '')
                gridCol.append(letter)
            self._grid.append(gridCol)
        self.shakeCubes()

    def getBoggleLetterAtPoint(self, point):
        """
        Return the BoggleLetter that contains the given point in the window,
        or None if the click is outside all letters.

        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = BoggleBoard(win)
        >>> pointIn_0_0 = Point(board.getXInset() + board.getSize() / 2, \
                                board.getYInset() + board.getSize() / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_0_0) == board._grid[0][0]
        True
        >>> pointIn_1_2 = Point(board.getXInset() + board.getSize() * 3 / 2, \
                                board.getYInset() + board.getSize() * 5 / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_1_2) == board._grid[1][2]
        True
        >>> win.close()
        """
        #returns the BoggleLetter at a clicked point.
        if self.inGrid(point):
            (x,y) = self.getPosition((point.getX(), point.getY()))
            return self._grid[x][y]

    def resetColors(self):
        """
        Unclicks all boggle letters on the board without changing any
        other attributes.
        """
        for each in self._grid:
            for letter in each:
                letter.setColor('black')

    def reset(self):
        """
        Clears the boggle board by clearing letters,
        clears all text areas (right, lower, upper) on board
        and resets the letters on board by calling shakeCubes.
        """
        #resets al text areas and cubes.
        self.setStringToLowerText('')
        self.setStringToTextArea('')
        self.setStringToUpperText('')
        self.shakeCubes()



    def shakeCubes(self):
        """
        Shakes the boggle board and sets letters
        as described by the handout.
        """
        #randomizes the order that the letters appear on the board while ensuring none repeat.
        cubes = shuffled(self._cubes)
        for col in range(self._cols):
            for row in range(self._rows):
                self._grid[col][row].setLetter(cubes[0][randomInt(0,5)])
                cubes = cubes[1:]



    def __str__(self):
        """
        Returns a string representation of this BoggleBoard
        """
        board = ''
        for r in range(self._rows):
            for c in range(self._cols):
                boggleLetter = self._grid[c][r]
                color = boggleLetter.getColor()
                letter = boggleLetter.getLetter()
                board += '[{}:{}] '.format(letter,color)
            board += '\n'
        return board


if __name__ == "__main__":
    from doctest import testmod
    testmod()

    # # Uncomment this code when you are ready to test it!
    #
    # # When you are ready to run on different boards,
    # # insert a call to randomize() here.  BUT you will
    # # find it much easier to test your code without
    # # randomizing things!
    randomize()
    win = GraphWin("Boggle", 400, 400)
    board = BoggleBoard(win)


    keepGoing = True
    while keepGoing:
        pt = win.getMouse()
        if board.inExit(pt):
            keepGoing = False
        elif board.inGrid(pt):
            (col, row) = board.getPosition((pt.getX(), pt.getY()))
            print("{} at {}".format(board._grid[col][row], (col, row)))
            board._grid[col][row].setColor('blue')
        elif board.inReset(pt):
            board.resetColors()
            board.reset()
