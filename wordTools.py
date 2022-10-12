
"""
various tools that are useful for solving word puzzles
This documentation is visible with
    pydoc3 wordTools
"""

# All functions go below here.
def letters(phrase):
    """Takes as input a string phrase and returns a string
    that contains just the letters from phrase (in order).

    >>> letters('superb: owl!')
    'superbowl'
    >>> letters('')
    ''
    >>> letters('#@$%')
    ''
    """
    #new
    result = ''
    for char in phrase:
        if char.isalpha():
            result += char
    return result
    #old
    result = ''
    for char in phrase:
        if char.isalpha():  # if char is a letter
            result += char  # concatenate to result
    return result

def canon(word):
    """Takes as input a string word and returns a "canonical" version
    of word: just the letters, in lower case, and in alphabetical order
    (as a string). Supports anagram testing.

    >>> canon('fix me') # fix this broken doctest
    'efimx'
    >>> canon('Mamma Mia!')
    'aaaimmmm'
    >>> canon('iAm')
    'aim'
    >>> canon('a lot')
    'alot'
    """
    word1 = letters(word)
    word2 = word1.lower()
    word3 = soreted(word2)
    return ''.join(word3)










    #word = letters(word)      # drop anything that's not a letter (e.g. spaces)
    #lowerWord = word.lower()  # to ensure Carol == carol
    #orderedWord = sorted(lowerWord) # ie.  a *list* of letters, in alpha order
    #result = ''.join(orderedWord) # converts list of letters to a single string
    #return result

def uniques(word):
    """Takes as input string word and return a string consisting of the unique
    characters in word.

    >>> uniques('abracadabra')
    'abrcd'
    >>> uniques('Connecticut')
    'Conectiu'
    >>> uniques('butterfly')
    'buterfly'
    >>> uniques('Montana')
    'Monta'
    """
    result = '' #sets counter to blank
    for char in word:
        if char.isalpha and char not in result: #checks for letters, verifies no duplicates
            result += char #adds new letters to result
    return result

def isIsogram(word):
    """Takes as input a string word and returns True only if the
    characters in word are unique (i.e., there are no repeated characters).
    Note that case should be ignored (i.e., E and e are the same character).

    >>> isIsogram('Monkey')
    True
    >>> isIsogram('Moo!')
    False

    """




    first = word.lower()
    second = uniques(first)
    third = canon(second)
    origional = canon(word)
    return third == origional


def sized(n, wordList):
    """ Takes a number of characters and returns from word list all
    words that are that length.

    >>>sized( 3 ,['The', 'man', 'said', 'plan'] )
    ['The', 'man']

    >>> sized( 2 , ['The', 'man', 'said', 'plan' , 'he' , 'Me'] )
    ['he' , 'Me']
    """

    list = []
    for word in wordList:
        if len(word) == n:
            list += [word]
    return list


def readWords(filename):
    """Takes as input the path to a file filename, opens and reads the words
    (one per line) in that file, and returns a list containing those words.

    >>> len(readWords('words/firstNames.txt'))
    5166
    >>> readWords('words/bodyparts.txt')[14]
    'belly button'
    >>> sized(8, readWords('words/italianCities.txt'))
    ['Cagliari', 'Florence', 'Siracusa']
    """
    results = []
    with open(filename) as wordFile:
        for line in wordFile:
            word = line.strip()   # do not use letters (think: 'belly button')
            results.append(word)  # add on to results list
    return results

def shift(word):
    """ takes and shifts characters in word 3 letters later in the alphabetical
    with the exception of x, y, and z which is makes 23 letters earlier.

    >>>shift('cat')
    'fdw'
    >>>shift('zap')
    'cds'
    """

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in word:
        nword = ''
        letterlist = list(word.lower())
        for char in letterlist:
            if char in alphabet[:23]:
                letter = alphabet.index(char)
                nletter = alphabet[letter+3]
                nword += nletter
            else:
                letter = alphabet.index(char)
                nletter = alphabet[letter-23]
                nword += nletter
    return nword

if __name__ == '__main__':
    # the following code tests the tests in the docstrings ('doctests').
    # as you add tests, re-run this as a script to test your work
    from doctest import testmod  # this import is necessary when testing
    testmod()                    # test this module, according to the doctests
