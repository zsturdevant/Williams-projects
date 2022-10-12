"""
Lab 7, Task 1

Accumulating recursion with lists of strings.
Inspired by https://stackoverflow.com/questions/3021/what-is-recursion-and-when-should-i-use-it
"""

def firstSentence(object, subject):
    """Given the strings object and subject, return a string representing the
    first sentence of the story about those characters."""
    return  "The mother of the " + object + " told " + \
            "a story about a " + subject + "..."

def lastSentence(object):
    """Given the string object, return a string representing the second (last)
    sentence of the story about that character."""
    return "and then the " + object + " fell asleep."

def bedtimeStory(characters):
    """
    Main (recursive) function for producing a bedtime story based on a list of
    strings (story characters). Returns a list of strings where each element is
    a sentence in the bedtime story.

    >>> bedtimeStory(['ant', 'fly'])
    ['The mother of the ant told a story about a fly...', 'and then the ant fell asleep.']

    >>> bedtimeStory(['ant', 'fly', 'chicken', 'pig', 'monkey'])
    ['The mother of the ant told a story about a fly...', 'The mother of the fly told a story about a chicken...', 'The mother of the chicken told a story about a pig...', 'The mother of the pig told a story about a monkey...', 'and then the pig fell asleep.', 'and then the chicken fell asleep.', 'and then the fly fell asleep.', 'and then the ant fell asleep.']
    """
    story = []
    if len(characters) <= 1:
        return[]
    else:
        char1 = characters[0]
        char2 = characters[1]
        story.append(firstSentence(char1, char2))
        story.extend(bedtimeStory(characters[1:]))
        story.append(lastSentence(char1))
        # takes first two characters and makes inserts them into first sentence
        # which is added to story then repeats this process with a new list of characters
        # starting with character 2 until there is only 1 character left then
        # ends the story with last sentence

    return story



def formatPrint(storyList):
    """Given a list of strings as story list, prints out the full story to the
    terminal in a nicely indented fashion."""
    n = len(storyList)

    # Print the first half of the list, with increasing indentation.
    for i in range(n // 2):
        print("   " * i + storyList[i])

    # Print the second half of the list, with decreasing indentation.
    for i in range(n // 2, n):
        print(("   " * (n - i - 1)) + storyList[i])

# Run the doctests, and also generate a list of characters from you provide
# when you run your program from the terminal.  Eg:
#
#    python3 bedtime.py parrot flamingo heron cow
#
if __name__ == "__main__":
    """Testing code"""
    from doctest import testmod
    testmod()

    from sys import argv
    chars = argv[1:]
    formatPrint(bedtimeStory(chars))
