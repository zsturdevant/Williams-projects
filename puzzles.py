"""Start by solving spelling-bee puzzle B1.

   Next, you may solve either the NPR puzzle P1 or P2.  You must solve at
   least one of these! If you want extra practice, try solving both.

   Extra Credit: If you would like a challenge, check out problems B2 and P3.
   These are not required! A small amount of extra credit will be given if you
   solve one or both of them.
"""

from wordTools import *

def b1():
    """How many lowercase 7-letter isograms are in words/dict.txt?

    This function returns an int representing the number of 7-letter isograms
    that are the answer.
    """
    dict = readWords("words/dict.txt")
    count = 0
    list7 = sized(7, dict)
    for word in list7:
        if isIsogram(word):
            count += 1
    return count


def p1():
    """Name part of the human body in six letters. Add an 'r' and rearrange
    the result to name another part of the body in seven letters.

    This function returns a string representing the concatenation of the
    two body parts (eg, 'part1 part2' or 'part2 part1').
    """
    parts = readWords("words/bodyParts.txt") #pull list of body parts from body parts

    list6 = sized(6, parts)
    for word in list6: #takes words in list6 adds an r and makes letters canonical
        word6 = word + "r"
        can6 = canon(word6)
        list7 = sized(7, parts) #makes list of 7 letter words, makes canonical
        for word7 in list7:
            can7 = canon(word7)
            if can7 == can6: #if canonical words are the same returns the origoinal words.
                return word + " " + word7




def p2():
    """Think of a major city in France whose name is an anagram of a major city
    in Italy.

    This function returns a string representing the concatenation of
    the cities (eg, 'frenchCity italianCity' or 'italianCity frenchCity').
    """
    pass

def b2():
    """Extra credit: Suppose you have a seven letter hive, 'mixcent'. How many
    4-letter lowercase words in words/dict.txt (1) include 'm' and (2) are
    spelled only using (possibly repeated) letters from the hive string?

    This function returns an int representing the number of words.
    """
    words = readWords("words/dict.txt")
    count = 0
    words4 = sized( 4, words )
    for word in words4:
        listm4 = []
        if "m" in word:
            listm4 += word
            for words in listm4:
                if letters(words) in "mixcent":
                    count += 1
    return count


def p3():
    """Extra credit: Think of a disease in five letters. Shift each letter three
    spaces later in the alphabet---for example, 'a' would become 'd', 'b' would
    become 'e', etc. The result will be a prominent name from the Bible.

    This function returns a string that is a concatenation of the illness and
    the name (eg, 'illness name' or 'name illness').
    """
    diseases = readWords("words/diseases.txt")
    biblenames = readWords("words/bibleNames.txt")
    diseases5 = sized(5, diseases)
    results =[]
    for word in biblenames:
            word = word.lower()
            results.append(word)
    for word in diseases5:
        theSickness = word
        name = shift(word)
        if name in results:
            return theSickness + " " + name


if __name__ == '__main__':
    # call puzzle functions
    print("b1(): " + str(b1()))
    print("p1(): " + str(p1()))
    print("p2(): " + str(p2()))
    print("b2(): " + str(b2()))
    print("p3(): " + str(p3()))
