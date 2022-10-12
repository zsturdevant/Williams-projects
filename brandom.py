# DO NOT MODIFY
# brandom.py
"""
Functions to create random numbers and random permutations of lists.
"""

import random

def randomInt(start, end):
    """
    Returns an integer i such that start <= i <= end.

    >>> 0 <= randomInt(0,1) <= 1
    True
    >>> 0 <= randomInt(0,1) <= 1
    True
    >>> randomInt(0,0)
    0
    """
    return random.randint(start, end)

def shuffled(seq):
    """
    Return a new list containing the shuffled elements of seq.

    >>> shuffled([]) == []
    True
    >>> set(shuffled([1,2,3])) == set([1,2,3])
    True
    """
    mixed = seq.copy()
    random.shuffle(mixed)
    return mixed


def randomize(seed = None):
    """
    Call this with no arguments to randomize the random
    number generator seed.  Your program will always 
    see the same random numbers unless you call this
    at the start of your script.  Eg:

    if __name__ == "__main__":
        randomize()
        # rest of your code ...

    """
    random.seed(seed)

# Make it always be the same random numbers
randomize(0)

if __name__ == "__main__":
    from doctest import testmod
    testmod()
