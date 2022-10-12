"""
Implements the functionality of a single letter squanre on the Boggle board.
"""

from graphics import *

class BoggleLetter:
    """A Boggle letter has several attributes that define it:
       *  _row, _col coordinates indicate its position in the grid (ints)
       *  _textObj denotes the Text object from the graphics module,
          which has attributes such as size, style, color, etc
          and supports methods such as getText(), setText() etc.
    """

    # add more attributes if needed!
    __slots__ = ['_col', '_row', '_textObj' ]

    def __init__(self, win, col=-1, row=-1, letter="", color="black"):
        """
        Construct a new Boggle Letter at the given position on the board,
        and with the optional letter and color.
        """

        # needed for standalone testing (can safely ignore)
        xInset = 50; yInset = 50; size = 50

        # set row and column attributes
        self._col = col
        self._row = row

        # initialize textObj attribute
        self._textObj = Text(Point(xInset + size * col + size / 2,
                                   yInset + size * row + size / 2), letter)
        self._textObj.setTextColor(color)
        self._textObj.draw(win)

    def getRow(self):
        """Returns _col coordinate (int) attribute."""
        return self._row

    def getCol(self):
        """Returns _col coordinate (int) attribute."""
        return self._col

    def setLetter(self, char):
        """
        Sets the text on the BoggleLetter to char (str) by setting the text
        of the Text object (textObj).
        >>> win = GraphWin("Boggle", 400, 400)
        >>> let1 = BoggleLetter(win, 1, 1, "A")
        >>> let1.setLetter("B")
        >>> print(let1.getLetter())
        B
        >>> win.close()
        """
        self._textObj.setText(char)

    def getLetter(self):
        """
        Returns letter (text of type str) associated with textObj attribute.
        >>> win = GraphWin("Boggle", 400, 400)
        >>> let1 = BoggleLetter(win, 1, 1, "A")
        >>> print(let1.getLetter())
        A
        >>> win.close()
        """
        return self._textObj.getText()

    def setColor(self, color):
        """
        Sets the color of the letters' Text object.
        """
        return self._textObj.setTextColor(color)

    def getColor(self):
        """
        Gets the color of the letter's Text object.
        """
        return self._textObj.getTextColor()

    # test for adjacency
    def isAdjacent(self, other):
        """
        Given a BoggleLetter other, check if other is adjacent to self.
        Returns True if they are adjacent, and otherwise returns False.
        Two letters are considered adjacent if they are not the same, and
        if their row and col coordinates differ by at most 1.

        >>> win = GraphWin("Boggle", 400, 400)
        >>> let1 = BoggleLetter(win, 1, 1, "A")
        >>> let2 = BoggleLetter(win, 1, 2, "B")
        >>> let3 = BoggleLetter(win, 3, 1, "C")
        >>> let1.isAdjacent(let2)
        True
        >>> let2.isAdjacent(let1)
        True
        >>> let3.isAdjacent(let3)
        False
        >>> let3.isAdjacent(let1)
        False
        >>> let2.isAdjacent(let3)
        False
        >>> win.close()
        """
        # checks if X + or - 1 = newX or Y + or - 1 = newY is True but returns False
        # if  X = newX and Y = newY
        (x,y) = self.getRow(), self.getCol()
        (z,t) = other.getRow(), other.getCol()
        if abs(x-z) <= 1 and abs(y-t)<=1 and (abs(x-z) + abs(y-t))!=0:
            return True
        else:
            return False

    def __str__(self):
        """
        Converts a BoggleLetter to a human-readable string.
        Please do not change this method.
        """
        return "BoggleLetter({}, {}, '{}', '{}')".format(self._col, self._row, \
                                                self.getLetter(), self.getColor())

    def __repr__(self):
        """
        A handy special method that enables Python to print lists
        of BoggleLetter objects nicely.
        Please do not change this method.
        """
        return str(self)


if __name__ == "__main__":
    from doctest import testmod
    testmod()

    # # The following code is a larger test.  Uncomment the code
    # # and run it, visually inspecting the results once you
    # # are confident that the class is close to complete.
    #
    from board import Board
    win = GraphWin("Boggle", 400, 400)
    board = Board(win, rows=4, cols=4)

    let1 = BoggleLetter(win, 1, 1, "A")
    let2 = BoggleLetter(win, 1, 2)
    let2.setLetter('B')
    let2.setColor("blue")
    let3 = BoggleLetter(win, 3, 1, "C", color="green")
    let3.setColor("green")

    #pause for mouse click before exiting
    point = win.getMouse()
    win.close()
