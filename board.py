# DO NOT MODIFY
# board.py
'''board.py: The Board class provides a basic game board interface, including
useful methods for creating and manipulating a grid of squares, methods for
converting screen coordinates to grid coordinates and vice versa, and methods
for setting and appending text to various locations outside of the grid.  It
also draws an exit and reset button and provides methods for checking for mouse
clicks inside of those regions.'''

from graphics import *

class Board:
    # _win: graphical window on which we will draw our board
    # _xInset: avoids drawing in corner of window
    # _yInset: avoids drawing in corner of window
    # _rows: number of rows in grid of squares
    # _cols: number of columns in grid of squares
    # _size: edge size of each square

    __slots__ = [ '_xInset', '_yInset', '_rows', '_cols', '_size', \
                '_win', '_exitButton', '_resetButton', \
                '_textArea', '_lowerWord', '_upperWord']

    def __init__(self, win, xInset=50, yInset=50, rows=3, cols=3, size=50):
        # update class attributes
        self._xInset = xInset
        self._yInset = yInset
        self._rows = rows
        self._cols = cols
        self._size = size
        self._win = win
        self.drawBoard()

    # getter methods for attributes
    def getWin(self):
        return self._win

    def getXInset(self):
        return self._xInset

    def getYInset(self):
        return self._yInset

    def getRows(self):
        return self._rows

    def getCols(self):
        return self._cols

    def getSize(self):
        return self._size

    def __initTextAreas(self):
        # initialize text areas
        self._textArea = Text(Point(self._xInset * self._rows + self._size * 2,
                                    self._yInset + 50), "")
        self._textArea.setSize(14)
        self._lowerWord = Text(Point(160, 275), "")
        self._lowerWord.setSize(18)
        self._upperWord = Text(Point(160, 25), "")
        self._upperWord.setSize(18)
        self._upperWord.setTextColor("red")

    def __drawTextAreas(self):
        """Draw the text area to the right/lower/upper side of main grid"""

        #initialize before drawing
        self.__initTextAreas()

        # draw main text area (right of grid)
        self._textArea.draw(self._win)

        #draw the text area below grid
        self._lowerWord.draw(self._win)

        #draw the text area above grid
        self._upperWord.draw(self._win)

    def __makeGrid(self):
        """Creates a row x col grid, filled with squares"""
        for x in range(self._cols):
            for y in range(self._rows):
                # create first point
                p1 = Point(self._xInset + self._size * x, self._yInset + self._size * y)
                # create second point
                p2 = Point(self._xInset + self._size * (x + 1), self._yInset + self._size * (y + 1))
                # create rectangle
                r = Rectangle(p1, p2)
                r.setFill("white")
                # add rectangle to graphical window
                r.draw(self._win)

                # print coord (for debugging)
                #Text(Point(self._xInset + 15 + self._size * x, \
                #           self._yInset + 15+ self._size * y), \
                #           "{},{}".format(x,y)).draw(win)

    def __makeResetButton(self):
        """Add a reset button to board"""
        self._resetButton = Rectangle(Point(50, 300), Point(130, 350))
        self._resetButton.setFill("white")
        self._resetButton.draw(self._win)
        Text(Point(90, 325), "RESET").draw(self._win)

    def __makeExitButton(self):
        """Add exit button to board"""
        self._exitButton = Rectangle(Point(170, 300), Point(250, 350))
        self._exitButton.draw(self._win)
        self._exitButton.setFill("white")
        Text(Point(210, 325), "EXIT").draw(self._win)


    def drawBoard(self):
        # this creates a row x col grid, filled with squares, including buttons
        self._win.setBackground("white smoke")
        self.__makeGrid()
        self.__makeResetButton()
        self.__makeExitButton()
        self.__drawTextAreas()

    # convert grid position to window coordinate
    def _getLocation(self, position):
        '''
        Converts a grid position (tuple) to a Point object.
        Points are essentially x, y screen coordinates.
        '''
        x = position[0] * self._size + self._xInset
        y = position[1] * self._size + self._yInset
        return Point(x, y)

    # convert window coordinate (tuple) to grid position (tuple)
    def getPosition(self, location):
        '''
        Converts a window location (tuple) to a grid position (tuple).
        Window locations are x, y coordinates.
        Note: Grid positions are always returned as col, row.
        '''
        if location[1] < self._yInset:
            row = -1
        else:
            row = int((location[1] - self._yInset) / self._size)

        if location[0] < self._xInset:
            col = -1
        else:
            col = int((location[0] - self._xInset) / self._size)
        return (col, row)

    # check for click inside specific rectangular region
    def _inRect(self, point, rect):
        '''
        Returns True if a Point (point) exists inside a specific
        Rectangle (rect) on screen.
        '''
        pX = point.getX()
        pY = point.getY()
        rLeft = rect.getP1().getX()
        rTop = rect.getP1().getY()
        rRight = rect.getP2().getX()
        rBottom = rect.getP2().getY()
        return pX > rLeft and pX < rRight and pY > rTop and pY < rBottom

    # check for click in grid
    def inGrid(self, point):
        '''
        Returns True if a Point (point) exists inside the grid of squares.
        '''
        ptX = point.getX()
        ptY = point.getY()
        maxY = self._size * (self._rows + 1)
        maxX = self._size * (self._cols + 1)
        return ptX <= maxX and ptY <= maxY and ptX >= self._xInset and ptY >= self._yInset

    # clicked in exit button?
    def inExit(self, point):
        '''
        Returns true if point is inside exit button (rectangle)
        '''
        return self._inRect(point, self._exitButton)

    # clicked in reset button?
    def inReset(self, point):
        '''
        Returns true if point is inside exit button (rectangle)
        '''
        return self._inRect(point, self._resetButton)

    # add text to text area on right
    def addStringToTextArea(self, text):
        '''
        Add text to text area to right of grid.
        Does not overwrite existing text.
        '''
        str = self._textArea.getText()
        self._textArea.setText( str + text )

    # set text to text area on right
    def setStringToTextArea(self, text):
        '''
        Sets text to text area to right of grid.
        Overwrites existing text.
        '''
        self._textArea.setText(text)

    # clear text from text area on right
    def clearTextArea(self):
        '''
        Clear text in text area to right of grid.
        '''
        self._textArea.setText("")

    # add text to text area below grid
    def addStringToLowerText(self, text):
        '''
        Add text to text area below grid.
        Does not overwrite existing text.
        '''
        str = self._lowerWord.getText()
        self._lowerWord.setText( str + text )

    # add text to text area below grid
    def setStringToLowerText(self, text):
        '''
        Set text to text area below grid.
        Overwrites existing text.
        '''
        self._lowerWord.setText( text )

    # clear word below grid
    def clearLowerText(self):
        '''
        Clear text area below grid.
        '''
        self._lowerWord.setText("")

    # add text to text area above grid
    def addStringToUpperText(self, text):
        '''
        Add text to text area above grid.
        Does not overwrites existing text.'''
        self._upperWord.setText(text)

    # set text to text area above grid
    def setStringToUpperText(self, text):
        '''
        Set text to text area above grid.
        Overwrites existing text.
        '''
        self._upperWord.setText(text)

    # clear text above grid
    def clearUpperText(self):
        '''
        Clear text area above grid.
        '''
        self._upperWord.setText("")

if __name__ == "__main__":
    win = GraphWin("Tic Tac Toe", 400, 400)

    # create new board with default values
    board = Board(win)

    # draw Board
    board.drawBoard()

    # set string above grid
    board.setStringToUpperText("Upper text area")

    # set and update string below grid
    board.setStringToLowerText("Lower text area: ")
    board.addStringToLowerText("hi!")

    # set string to text area to right of grid
    board.setStringToTextArea("Text area")

    keepGoing = True
    # loop and return info about mouse clicks until exit is clicked
    while keepGoing:
        # wait for a mouse click
        point = win.getMouse()

        # calculate x and y value from point
        x,y = point.getX(), point.getY()

        # close window and exit if exit button is clicked
        if board.inExit(point):
            print("Exiting...")
            keepGoing = False

        # did we click reset?
        elif board.inReset(point):
            print("Reset button clicked")

        # are we in the grid? if so, print coor and grid position
        elif board.inGrid(point):
            print("Clicked coord {} or grid {}".format((x,y), board.getPosition((x,y))))

        #else just print info about mouse click
        else:
            print("Clicked coord {} which is not in grid".format((x,y)))
