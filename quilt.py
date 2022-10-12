"""
Lab 7, Task 3

Using the turtle module, draws a Williams purple and gold quilt pattern.
"""
from turtle import *
from sys import argv

# Colors: Williams Purple and Gold.
PURPLE = '#500082'
GOLD = '#FFBE0A'

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

    # Configure our turtles line width and speed
    pensize(1)
    shape('turtle')
    speed(5)   # 0=fastest, 1=slowest, 6=normal

    # By default turtle starts at (0,0), the center of the screen and faces east.
    # We move it to the bottom left corner of the pattern.
    up()
    goto(-size/2, -size/2)


def drawQuilt(quiltSize, patchSize, patchColor, otherColor):
    """Draws a colored quilt as described in the lab writeup.
    Assume that the turtle is positioned at the bottom left
    end point of quilt facing east before this function is called.
    """

    if quiltSize < patchSize:
        pass
    else:
        drawSquare(quiltSize, patchColor)
        #draws the first square of the quilt
        left(90)
        forward(quiltSize/2)
        right(90)
        #moves turtle to position to draw next next quilt
        drawQuilt(quiltSize/2, patchSize, otherColor, patchColor)
        left(90)
        backward(quiltSize/2)
        #repositions turtle at starting point
        right(90)
        forward(quiltSize/2)
        #moves turtle into position to draw next quilt
        drawQuilt(quiltSize/2, patchSize, otherColor, patchColor)
        backward(quiltSize/2)
        #returns turtle to starting position


# When run as a script, take a picture size and the gap between
# concentric squares as command-line arguments.
if __name__=='__main__':
    """Testing code"""
    if len(argv) != 3:
        print("Provide a quilt size and patch size when running, eg:\n")
        print("  python3 quit.py 512 128\n")
    else:
        quiltSize = int(argv[1])
        patchSize = int(argv[2])

        initializeTurtle(quiltSize)
        drawQuilt(quiltSize, patchSize, PURPLE, GOLD)
        getscreen().getcanvas().postscript(file="drawQuilt-{}-{}.ps".format(quiltSize, patchSize))

        # Comment out the line below if you want
        # the turtle screen to close automatically.
        exitonclick()
