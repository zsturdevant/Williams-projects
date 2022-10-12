# Implements different voting rules

# import functions from voting module
from voting import *

# Part 1.4
def plurality(ballots):
    '''Takes as input ballot data as a list of lists of strings, and
    returns a list of strings of names of candidates who get the most votes.
    >>> plurality(readBallot('data/simple.csv'))
    ['Aamir']
    >>> plurality(readBallot('data/example.csv'))
    ['Ava']
    >>> plurality(readBallot('data/characters.csv'))
    ['Scarlett OHara', 'Samwise Gamgee']
    '''
    return mostVotes(firstChoiceVotes(ballots)) #takes ballots and returns a
    # list of the cantadates with the most first choice votes.




# Part 1.6
def bordaScore(name, ballots):
    ''' Takes a name and a ballot as a list of lists of strings, assigns points
    based on the position in each ballot then returns the total score for the
    name given.

    >>> bordaScore('Ava',readBallot('data/example.csv'))
    37
    >>> bordaScore('Bob',readBallot('data/example.csv'))
    42
    >>> bordaScore('Cid',readBallot('data/example.csv'))
    47
    '''
    nameCounter = 0
    for Blist in ballots:
        count = Blist.index(name) #takes rank in each ballot
        points = len(Blist) - count #returns points based on position in ballot
        nameCounter += points
    return nameCounter #returns total number of points

def borda(ballots):
    '''Takes as input ballot data as list of lists of strings, and
    returns a list of strings of the names of candidates with the
    maximum borda score.

    >>> borda(readBallot('data/simple.csv'))
    ['Aamir']
    >>> borda(readBallot('data/example.csv'))
    ['Cid']
    >>> borda(readBallot('data/characters.csv'))
    ['Harry Potter']
    '''
    people = candidates(ballots)
    highest = 0
    winner = []
    for name in people: #takes list of candidates
        votes = bordaScore(name, ballots) #finds borda score
        if votes > highest:
            winner = [name] #makes new highest vote total and saves name of.
            highest = votes #winner for later return.
        elif votes == highest:
            winner.append(name)
            #adds names of any who are tied for highest score to winning list.
    return winner


# Part 2.4
def rankedChoice(ballots):
    '''Takes as input ballot data as list of lists of strings, and
    returns the winner of the election based on ranked-choice
    voting as a list of strings of names.

    >>> rankedChoice(readBallot('data/simple.csv'))
    ['Aamir']
    >>> rankedChoice(readBallot('data/example.csv'))
    ['Bob']
    >>> rankedChoice(readBallot('data/characters.csv'))
    ['Scarlett OHara']
    >>> rankedChoice([['Abe', 'Betsy', 'Carmen'], ['Betsy', 'Abe', 'Carmen'], ['Carmen', 'Abe', 'Betsy']])
    ['Abe', 'Betsy', 'Carmen']
    >>> rankedChoice([['Sierra', 'Tao', 'Una'], ['Sierra', 'Tao', 'Una'], ['Tao', 'Sierra', 'Una'], ['Tao', 'Sierra', 'Una']])
    ['Sierra', 'Tao']
    '''
    nBallots = [ballot for ballot in ballots]
    while True:
        if majority(firstChoiceVotes(nBallots)) != '':
            return [majority(firstChoiceVotes(nBallots))]
            #checks for and returns majority winner.
        elif leastVotes(firstChoiceVotes(nBallots), candidates(nBallots)) == candidates(nBallots):
            return candidates(nBallots)
            #determines if all remaining candidates are tied in vote.
        else:
            eliminateCandidates(leastVotes(firstChoiceVotes(nBallots), candidates(nBallots)), nBallots)
            #eliminates the candidates with the lowest number of votes.



# Part 2.5
def condorcet(ballots):
    '''EXTRA CREDIT: Takes as input ballot data as list of
    lists of strings, and returns the winner of the election
    as a string (or empty string if there is no winner).
    >>> condorcet([['Jeff', 'Sarah', 'Jim'], ['Jeff', 'Sarah', 'Jim'], ['Sarah', 'Jim', 'Jeff']])
    'Jeff'

    '''
    if majority(firstChoiceVotes(ballots)) != '':
        return majority(firstChoiceVotes(ballots))
    else:
        nBallot = [ballot for ballot in ballots]
        winner = candidates(ballots)
        listOfCandidates = candidates(ballots)

        for name in listOfCandidates:
            for nameTwo in listOfCandidates:
                compareList = [name, nameTwo]
                aBallot = nBallot[:]
                elimList = [name for name in winner if name not in compareList]
                eliminateCandidates(elimList, aBallot)
                if leastVotes(aBallot, candidates(aBallot))[0] in winner:
                    winner.remove(leastVotes(aBallot, candidates(aBallot)))
        if len(winner) == 1:
            return winner[0]
        else:
            return ''






if __name__ == '__main__':
    from doctest import *
    testmod()

    # Read in our ice cream ballots and run our election algorithms for Part 1.
    #print('Ice-cream flavor class election results:')
    #print('Plurality winner:', ", ".join(plurality(readBallot('data/icecream.csv'))))
    #print('Borda winner:', ", ".join(borda(readBallot('data/icecream.csv'))))

    # # Read in our ice cream ballots and run our election algorithms for Part 2.
    # #print('Ranked-choice winner:', ", ".join(rankedChoice(readBallot('data/icecream.csv'))))
    # # Uncomment the following line if you complete the extra credit
    # print('Condorcet winner:', condorcet(readBallot('data/icecream.csv')))
