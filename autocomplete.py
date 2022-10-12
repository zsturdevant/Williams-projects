"""
Module to implement auto complete
"""

import csv
from freqword import *
from result import *

class AutoComplete:
    """
    A class for generating autocomplete suggestions
    """

    __slots__ = [ "_words" ]

    def __init__(self, corpus):
        """
        Constructor for the AutoComplete class. The input
        corpus corresponds to a filename to be used as a basis
        for constructing the frequency of words dictionary.

        >>> AutoComplete("data/miniGutenberg.csv")._words[0]
        circumstances[107]
        >>> AutoComplete("data/miniGutenberg.csv")._words[-2]
        wooded[8]
        >>> AutoComplete("data/miniGutenberg.csv")._words[-2].getText()
        'wooded'
        >>> AutoComplete("data/miniGutenberg.csv")._words[-2].getCount()
        8
        >>> AutoComplete("data/miniGutenberg.csv")._words[-3].getCount()
        21
        >>> AutoComplete("data/miniGutenberg.csv")._words[-3].getText()
        'scraped'
        """
        wordList = []
        with open(corpus) as file:
            #takes each line in a file and makes a Freqword object which is then
            #added to a list of freqwords and returned.
            for line in file:
                new = line.strip().split(",")
                text = new[0]
                count = new[1]
                frequencyTrack = FreqWord(text, count)
                wordList.append(frequencyTrack)
        self._words = sorted(wordList, key=textKey)

    def _matchWords(self, criteria):
        """
        Part 3 of Lab:
        Perform a search to return a list of word objects that match
        the given criteria -- when the criteria corresponds to a prefix,
        this returns a list where each word contains the given prefix.

        Part 4 of Lab:
        if the criteria corresponds to a pattern (contains *'s), this
        returns a list where each word matches the given pattern.

        >>> AutoComplete("data/miniGutenberg.csv")._matchWords("sc")
        [scold[3], scraped[21]]
        >>> AutoComplete("data/miniGutenberg.csv")._matchWords("um")
        []
        >>> AutoComplete("data/miniGutenberg.csv")._matchWords("cir")
        [circumstances[107]]
        """
        listOfWords = []
        for each in self._words:
            #takes words in wordList and looks for words matching a given criteria
            #then returns a list of the words matching that criteria
            if "*" not in criteria:
                if each.hasPrefix(criteria):
                    listOfWords.append(each)
            else:
                if each.matchesPattern(criteria):
                    listOfWords.append(each)
        return listOfWords


    def suggestCompletions(self, inputString):
        """
        Suggest word completions based on (i) whether the user has input
        a criteria or a wild card expression and (ii) frequency of occurrence
        of the possible completions. The final object that is returned is
        an instance of the Result class with the top 3 completions if at least
        3 possible completions exist (and fewer if there are less than 3 possible
        completions.) Remember that if the inputString is itself a possible completion
        it should be given top priority regardless of its frequency.

        >>> print(AutoComplete("data/gutenberg.csv").suggestCompletions("auto"))
        auto --> autonomy[7] | autocratic[5] | auto[3]
        >>> print(AutoComplete("data/miniGutenberg.csv").suggestCompletions("woo*e*"))
        woo*e* --> wooden[37] | wooded[8]
        >>> print(AutoComplete("data/gutenberg.csv").suggestCompletions("woo*e*"))
        woo*e* --> wooden[37] | woolen[15] | wooded[8]
        >>> print(AutoComplete("data/gutenberg.csv").suggestCompletions("cir"))
        cir --> circumstances[107] | circulation[91] | circle[78]
        """
        #Returns the top three choices from match words sorted by relivence.
        return(Result(inputString, sorted(self._matchWords(inputString),
                            key=countKey, reverse = True)[:3]))

    def __str__(self):
        """
        >>> print(AutoComplete("data/miniGutenberg.csv"))
        circumstances[107]
        scold[3]
        scraped[21]
        wooded[8]
        wooden[37]
        >>> print( AutoComplete("data/miniGutenberg.csv")._words[-2])
        wooded[8]
        """
        #takes list of freqwords returns them in a printable manner.
        strCompletions = []
        for element in self._words:
            strCompletions.append(str(element))
        return "\n".join(strCompletions)






if __name__ == "__main__":
    # Run all the doctests
    import doctest
    doctest.testmod()

    # Suggest completions for any input strings provided on the command
    # line.  Eg:
    #
    #    python3 autocomplete.py moo cow r***s
    #
    import sys
    auto = AutoComplete("data/gutenberg.csv")
    for inputString in sys.argv[1:]:
        print(auto.suggestCompletions(inputString))
