"""
Lab 7, Extra credit

"""

from turtle import *

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
    speed(0)   # 0=fastest, 1=slowest, 6=normal

    # By default turtle starts at (0,0), the center of the screen and faces east.
    # We move it to the bottom left corner of the pattern.
    up()
    goto(-size/2, -size/2)

def drawFancySquares(patternSize, minSize, colors):
    """Draws a pattern specified in Lab 7 Extra Credit.
    Returns a triple (a 3-tuple) consisting of
      (1) the total number of squares of colors[0] in pattern
      (2) the total number of squares of colors[1] in pattern
      (3) the total number of squares of colors[2] in pattern
    Assume that the turtle is positioned at the bottom left
    end point of pattern facing east before this function is called.
    """
    # Write me!
    pass

# When run as a script, take a picture size and the gap between
# concentric squares as command-line arguments.
if __name__=='__main__':
    """Testing code"""
    from sys import argv
    if len(argv) != 3:
        print("Provide a size and gap when running, eg:\n")
        print("  python3 fancy.py 512 64\n")
    else:
        patternSize = int(argv[1])
        minSize = int(argv[2])

        initializeTurtle(patternSize)
        counts = drawFancySquares(patternSize, minSize, ("red", "blue", "cyan"))
        print('fancy({}, {})->{})'.format(patternSize, minSize, counts))
        getscreen().getcanvas().postscript(file="fancy-{}-{}.ps".format
                            (patternSize, minSize))

        # Comment out the line below if you want
        # the turtle screen to close automatically.
        exitonclick()
