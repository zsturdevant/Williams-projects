"""
Lab 7, Task 2

Using the turtle module, draws a nested squares in Williams purple and white.
"""

from turtle import *
from sys import argv

# Colors: Williams Purple and White.
PURPLE = '#500082'
WHITE = '#FFFFFF'

def drawSquare(size, color):
    """Draws a single square of side length size (int) and given color (string)
    assuming turtle is initially at one of its endpoints"""
    down()
    pen(fillcolor = color)
    begin_fill()
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()
    up()

def initializeTurtle(size):
    """Setups up the window given size (int) and initializes the turtle to be at
    the bottom left corner of the pattern facing east (the default direction)."""

    # Create a turtle window
    padding = 50
    setup(width = size + padding, height = size + padding)
    reset()
    shape('turtle')
    # Configure our turtles line width and speed
    pensize(1)
    speed(0)   # 0=fastest, 1=slowest, 6=normal

    # By default turtle starts at (0,0), the center of the screen and faces east.
    # We move it to the bottom left corner of the pattern.
    up()
    goto(-size/2, -size/2)


def drawNestedSquares(size, gap, color, otherColor):
    """Draws the nested squares as described in the lab writeup.
    Assume that the turtle is positioned at the bottom left
    of the biggest square we must draw and facing east.
    """

    if size <= 0:
        pass

    else:
        drawSquare(size, color)
        forward(gap)
        left(90)
        forward(gap)
        right(90)
        drawNestedSquares(size-gap*2, gap, otherColor, color)
        left(90)
        backward(gap)
        right(90)
        backward(gap)


# When run as a script, take a picture size and the gap between
# concentric squares as command-line arguments.
if __name__=='__main__':
    """Testing code"""

    # argv is a list of the command-line arguments passed to python3,
    #  so argv[0] is squares.py, and argv[1] and argv[2] should be the
    #  size and gap.
    if len(argv) != 3:
        print("Provide a size and gap when running, eg:\n")
        print("  python3 squares.py 400 20\n")
    else:
        size = int(argv[1])
        gap = int(argv[2])

        # Create turtle world and position turtle in the lower left.
        initializeTurtle(size)

        # Your function
        drawNestedSquares(size, gap, PURPLE, WHITE)

        # Save the drawing to a file.
        getscreen().getcanvas().postscript(file="drawSquares-{}-{}.ps".format(size, gap))

        # Comment out the line below if you want
        # the turtle screen to close automatically.
        exitonclick()
