# Script includes syntax errors
"""
This program converts an inputted word into a format common in a Swedish
word game (Rovarkspraket).
The rules are:
  1. For each consonant, the consonant is doubled and the supplied letter
     is inserted between (e.g. "n" becomes "non" when "o" is supplied)
  2. Pre-existing vowels remain untouched
"""

#print("Is anything running when I run this program?")
def convert(letter, word):
    """
    Converts the inputed word into a Rovarkspraket format, using
    the supplied letter as a separator.
    >>> convert('ouo', '')
    ''
    >>> convert('o', 'stubborn')
    'sostotubobboborornon'
    """
    answer = '' #Fixed (made a variable called answer)
    for char in word: #Fixed (added :)
        if char in 'aeiou':
            answer += char
        else:
            answer += char + letter + char
    return answer

def test(letter, word): #fixed (made the variable names more discriptive)
    """Call convert on a letter and a word and print return value"""
    wordR = convert(letter, word) #Fixed (closed parenthesis)
    print("convert('{}', '{}') returns '{}'".format(letter, word, wordR))#fixed


if __name__ == "__main__":#Fixed
    #print("Is this code block being run?"
    testCases = [('ouo', ''), ('o', 'stubborn')]
    for letter, word in testCases:
        # find out what is in letter and word
        #print(letter, word)
        test(print(letter, word))
