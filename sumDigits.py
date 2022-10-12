"""
Lab 7, Warm-up Task 0

Fruitful recursion with numbers.
Sums the digits of a non-negative number
"""


def sumDigits(num):
    """Given a non-negative integer num, return the sum of the
    digits of num.
    >>> sumDigits(1)
    1
    >>> sumDigits(8)
    8
    >>> sumDigits(90)
    9
    >>> sumDigits(178)
    16
    >>> sumDigits(1234567890)
    45
    """
    if num < 10:
        sum = num
    else:
        sum = num % 10 + sumDigits(num // 10)
        # divides number by ten until the final number is less than 10
        # then adds the remainders of all operations to the final number and
        # returns that sum
    return sum



# Standard code to run the doc tests
if __name__ == '__main__':
    import doctest
    doctest.testmod()
