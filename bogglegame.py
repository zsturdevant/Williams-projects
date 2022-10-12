"""Implements the logic of the game of boggle."""

from graphics import GraphWin
from boggleboard import BoggleBoard
from boggleletter import BoggleLetter
from brandom import randomize

class BoggleGame(BoggleBoard):

    __slots__ = [ "_validWords", "_board", "_foundWords", "_selectedLetters", "_currentWord",
                    "_currentLetter"]

    def __init__(self, win):
        """
        Create a new Boggle Game and load in our lexicon.
        """
        # set up the set of valid words we can match
        self._validWords = self.__readLexicon()

        super().__init__(win)

        self._foundWords = []

        self._selectedLetters = []

        self._currentLetter = BoggleLetter(win)

        # init other attributes here.

    def __readLexicon(self, lexiconName='bogwords.txt'):
        """
        A helper method to read the lexicon and return it as a set.
        """
        validWords = set()
        with open(lexiconName) as f:
          for line in f:
            validWords.add(line.strip().upper())

        return validWords

    def __resetState(self):
        """
        A helper method that resets _selectedLetters, colors and clears
        lower text area.
        """
        self._selectedLetters =[]
        self.resetColors()
        self.clearLowerText()

    def doOneClick(self, point):
        """
        Implements the logic for processing one click.
        Returns True if play should continue, and False if the game is over.
        """
        # These steps are one way to think about the design, although
        # you are free to do things differently if you prefer.

        # step 1: check for exit button and return False if clicked
        if self.inExit(point):
            return False

        # step 2: check for reset button and reset
        elif self.inReset(point):
            self.resetColors()
            self.reset()
            self._selectedLetters =[]
            self._foundWords = []
            self._currentLetter = BoggleLetter(win)


        # step 3: check if click is on a cell in the grid
        elif self.inGrid(point):
            # gets BoggleLetter at point
            letter = self.getBoggleLetterAtPoint(point)

            # if this is the first letter in a word being constructed,
            # add letter and display it on lower text of board
            if len(self._selectedLetters) == 0:
                self._currentLetter = letter
                self._selectedLetters = [letter.getLetter()]
                self.setStringToLowerText(letter.getLetter())
                letter.setColor("blue")


            # else if adding a letter to a non-empty word, make sure it's adjacent
            # and update state
            elif self.getBoggleLetterAtPoint(point).getColor() == "black" and self._currentLetter.isAdjacent(letter):
                    self.addStringToLowerText(letter.getLetter())
                    self._currentLetter.setColor("green")
                    self._currentLetter = letter
                    self._selectedLetters.append(letter.getLetter())
                    letter.setColor("blue")

        # else if clicked on same letter as last time, end word and check for validity
            elif (letter.getRow(), letter.getCol()) == (self._currentLetter.getRow(),self._currentLetter.getCol()):
                word = "".join(self._selectedLetters).upper()

                # adds word to trackers if a new real word is found and resets
                # other aspects of the board.
                if word in self._validWords and word not in self._foundWords:
                    self._foundWords.append(word)
                    self.addStringToTextArea(word + "\n")
                    self.__resetState()

                #if new word is not found resets state and lower text area.
                else:
                    self.__resetState()

        # else if clicked anywhere else in the grid, reset the state to an empty word.
            else:
                self.__resetState()

        # else if on the board but not in a defined space, reset state.
        else:
            self.__resetState()

        # # return True to indicate we want to keep playing
        return True


if __name__ == '__main__':

    # When you are ready to run on different boards,
    # insert a call to randomize() here.  BUT you will
    # find it much easier to test your code without
    # randomizing things!
    randomize()
    win = GraphWin("Boggle", 400, 400)
    game = BoggleGame(win)
    keepGoing = True
    while keepGoing:
        point = win.getMouse()
        keepGoing = game.doOneClick(point)
