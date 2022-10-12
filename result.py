"""
Module to implement a result object that will be returned by auto complete
"""

from freqword import *

class Result:
    """
    A class for outputting readable autocomplete suggestions
    """

    __slots__ = ["_input", "_completions"]

    def __init__(self, inputWord, completionList):
        """
        Constructor for the Result class
        """
        self._input = inputWord
        self._completions = completionList

    def __str__(self):
        """
        A method that converts an instance of the Result
        class into an easily readable string.

        >>> print(Result("the", [FreqWord("the",4), FreqWord("theirs",3), FreqWord("then",2)]))
        the --> the[4] | theirs[3] | then[2]
        >>> print(Result("", [FreqWord("the",4)]))
         --> the[4]
         >>> print(Result("the", [FreqWord("the",4), FreqWord("them",4)]))
         the --> the[4] | them[4]
        """
        #itterates over a list of freqwords and formats them for printing.
        strCompletions = []
        for element in self._completions:
            strCompletions.append(str(element))
        return "{} --> {}".format(self._input, " | ".join(strCompletions))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
