"""
A module for representing information about words in a corpus.
"""

class FreqWord:
    """
    A class representing a word and its count.
    """

    # _text is a string, _count is an int
    __slots__ = ["_text", "_count"]

    def __init__(self, text, count):
        """
        Constructor for the FreqWord class.

        """
        self._text = text
        self._count = int(count)

    def getText(self):
        """
        Accessor method to get text of the word

        >>> FreqWord('contemplate', 100).getText()
        'contemplate'
        >>> FreqWord('', 0).getText()
        ''
        >>> FreqWord('applesauce', 12).getText()
        'applesauce'
        """
        return self._text

    def getCount(self):
        """
        Accessor method to get frequency of the word

        >>> FreqWord('contemplate', 100).getCount()
        100
        >>> FreqWord('', 0).getCount()
        0
        >>> FreqWord('applesauce', 12).getCount()
        12
        """
        return self._count

    def __str__(self):
        """
        A method that converts an instance of the Result
        class into an easily readable string.

        >>> print(FreqWord("moo", 5))
        moo[5]
        >>> FreqWord('applesauce', 12)
        applesauce[12]
        """
        return "{}[{}]".format(self._text, self._count)


    def hasPrefix(self, prefix):
        """
        Returns whether the text starts with the given prefix or not.

        >>> FreqWord('contemplate', 100).hasPrefix('con')
        True
        >>> FreqWord('contemplate', 100).hasPrefix('tempt')
        False
        >>> FreqWord('BeesKneeS', 100).hasPrefix('BEE')
        True
        >>> FreqWord('contemplate', 100).hasPrefix('templ')
        False
        """
        return self._text[:len(prefix)].lower() == prefix.lower()


    def __repr__(self):
        """
        This is a special method that allows printing lists of WordFreq
        objects.
        """
        # Just invokes the __str__ method to create a nice string.
        return self.__str__()



    def matchesPattern(self, pattern):
         """
         Returns whether the text matches the given pattern or not.

         >>> FreqWord('contemplate', 100).matchesPattern('c***emp*at*')
         True
         >>> FreqWord('contemplate', 100).matchesPattern('contemp**')
         False
         >>> FreqWord('test', 100).matchesPattern('text')
         False
         >>> FreqWord('test', 100).matchesPattern('ne*t')
         False
         >>> FreqWord('temple', 100).matchesPattern('t****e')
         True
         """
         #itterates over a pattern checking that each non * character matches the
         #character of the corresponding letter in a word, then returns wether or
         #not the word matches the pattern.
         count = 0
         if len(pattern) == len(self.getText()):
            for each in pattern:
                if each != '*':
                    if each == self.getText()[count]:
                        count += 1
                    else:
                        return False
                else:
                    count += 1
            return True
         return False



# The following two functions are defined outside of the class, so that
# we can use them as the key functions when sorting.

def textKey(freqWord):
    """
    A function that can be used as a sorting key function.
    It extracts the text from FreqWords.

    >>> words = [ FreqWord("b",5), FreqWord("c",10), FreqWord("a", 8) ]
    >>> sorted(words, key = textKey)
    [a[8], b[5], c[10]]
    >>> sorted(words, key = textKey, reverse = True)
    [c[10], b[5], a[8]]
    """

    return freqWord.getText()

def countKey(freqWord):
    """
    A function that can be used as a sorting key function.
    It extracts the count from FreqWords.

    >>> words = [ FreqWord("b",5), FreqWord("c",10), FreqWord("a", 8) ]
    >>> sorted(words, key = countKey)
    [b[5], a[8], c[10]]
    >>> sorted(words, key = countKey, reverse = True)
    [c[10], a[8], b[5]]
    """
    return freqWord.getCount()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
