# Script includes functions with logic errors
"""
This program tests whether or not a word is "vowelacious".  We call
a word vowelacious if it contains 3 or more consecutive vowels.
"""


# Change these three strings to be examples where isVowelaciousBuggy1
# properly identifies a vowelacious word, properly identifies a
# non-vowelacious word, and misclassifies a vowelacious word as
# not vowelacious:
buggy1Vowelacious = "ooo"    # string is vowelacious; function returns True
buggy1NotVowelacious = "aok" # string is not vowelacious; function returns False
buggy1Bad = "oook"            # string is vowelacious; function returns False


# Change these three strings to be examples where isVowelaciousBuggy2
# properly identifies a vowelacious word, properly identifies a
# non-vowelacious word, and misclassifies a vowelacious word as
# not vowelacious:
buggy2Vowelacious = "oook"    # string is vowelacious; function returns True
buggy2NotVowelacious = "aka" # string is not vowelacious; function returns False
buggy2Bad = "oaa"            # string is vowelacious; function returns False


def isVowelaciousBuggy1(word):
    """Takes a word as input and is supposed to return True if
    the word is vowelacious (contain 3 or more consecutive vowels).
    This version has a logic error.
    TODO: DESCRIBE THE LOGIC ERROR!

    The logic error occures when the 3 vowels do not occur at the end of the
    word, because of how the if statement is written the list of vowels is never
    checked for length prior to the full word being analized. therefore if the
    sequences does not occur at the end of the word it will be ereased before
    being checked.
    """
    #print('isVowelaciousBuggy1({})'.format(word)) # debugging print
    vowelSeq = '' # initializing variable to accumulate vowel seq

    for char in word:
        if char.lower() in 'aeiou':
            vowelSeq += char # add char
        else:
            vowelSeq = '' # reset if a consonant occurs
        #print('vowelSeq =', vowelSeq) # debugging print

    return len(vowelSeq) >= 3

def isVowelaciousBuggy2(word):
    """Takes a word as input and is supposed to return True if
    the word is vowelacious (contain 3 or more consecutive vowels).
    This version has a logic error.
    TODO: DESCRIBE THE LOGIC ERROR!

    The logic error occures when the three vowels are at the end of the word,
    because the length of vowelSeq is not checked unless char is not in aeiou
    an ending of three vowels would not be checked for length.and thus cannot
    return True.
    """

    #print('isVowelaciousBuggy2({})'.format(word)) # debugging print
    vowelSeq = '' # initializing variable to accumulate vowel seq
    found = False # initialize return value

    for char in word:
        if char.lower() in 'aeiou':
            vowelSeq += char # add char
        elif len(vowelSeq) >= 3:
            #print("Setting found to true") # debugging print
            found = True
        else:
            vowelSeq = '' # reset if a consonant occurs
        #print('vowelSeq =', vowelSeq) # debugging print

    return found

def isVowelacious(word):
    """Takes a word as input and is supposed to return True if
    the word is vowelacious (contain 3 or more consecutive vowels).
    This is the correct version.
    >>> isVowelacious('ooo')
    True
    >>> isVowelacious('aka')
    False
    >>> isVowelacious('cooook')
    True


    """
    vowelSeq = '' # initializing variable to accumulate vowel seq

    for char in word:
        if char.lower() in 'aeiou':
            vowelSeq += char # add char
            if len(vowelSeq) >= 3:
                return len(vowelSeq) >= 3
        else:
            vowelSeq = '' # reset if a consonant occurs

    return len(vowelSeq) >= 3

if __name__ == "__main__":
    # call the functions on some test cases directly
    #print(isVowelaciousBuggy1("hello"))
    #print(isVowelaciousBuggy2("world"))
    #print(isVowelacious(""))
