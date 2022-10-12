# Write documentation for this file

'''
This module contains functions which are used in determining the winner of
an election through a variety of methods.
'''


# Part 1.1
def readBallot(filename):
    ''' Takes and opens file, organizes ballots into a list of lists where
    each list is a ranked ballot.

    >>> readBallot("data/simple.csv")
    [['Aamir', 'Chris', 'Beth'], ['Beth', 'Aamir', 'Chris'], ['Chris', 'Beth', 'Aamir'], ['Aamir', 'Beth', 'Chris']]

    >>> readBallot("data/characters.csv")[0][3]
    'Elizabeth Bennet'

    >>> readBallot("data/characters.csv")[0][3][9]
    ' '
    >>> readBallot('data/example.csv')[3][1]
    'Cid'
    '''
    with open(filename) as ballotList:
        ballots = []
        for line in ballotList:
            votes = line.strip().split(',') #makes list of lists and removes noise
            ballots.append(votes) #adds new list to ballot list
        return ballots

# Part 1.2
def firstChoiceVotes(ballots):
    ''' Takes a list of ballots and returns all first choice candidates.

    >>> firstChoiceVotes(readBallot('data/simple.csv'))
    ['Aamir', 'Beth', 'Chris', 'Aamir']
    >>> firstChoiceVotes([['Abe', 'Betsy'], ['Eve'], ['Fred', 'Gina'], []])
    ['Abe', 'Eve', 'Fred']
    >>> firstChoiceVotes(readBallot('data/simple.csv'))[0]
    'Aamir'
    >>> firstChoiceVotes(readBallot('data/characters.csv'))[0:3]
    ['Harry Potter', 'Harry Potter', 'Scarlett OHara']
    '''
    choice = [list[0] for list in ballots if len(list)>0]
    return choice #returns a list of first choices


# Part 1.3
def mostVotes(votes):
    '''Takes list as input, counts number of first place votes and returns
    a list of those who have the highest number of votes.

    >>> mostVotes(firstChoiceVotes(readBallot('data/example.csv')))
    ['Ava']
    >>> mostVotes(['Aamir', 'Beth', 'Chris', 'Aamir'])
    ['Aamir']
    >>> mostVotes(['Abe', 'Abe', 'Betsy', 'Betsy', 'Carmen', 'Dave', 'Eva', 'Frida', 'Frida'])
    ['Abe', 'Betsy', 'Frida']
    >>> mostVotes([])
    []
    '''
    highest = []
    voteCount = 0
    first = votes
    for name in first:
        number = first.count(name)
        if number > voteCount:
            highest = [name]
            voteCount = number
            #counts the number of votes for each name and save the name and
            #number of votes recieved by the highest.
        elif number == voteCount and name not in highest:
            highest.append(name)
            #if tied for the highest number added name to list of highest.
    return highest

# Part 1.5
def candidates(ballots):
    ''' This function takes a list of ballots and returns a list of all names
    included in all Ballots.

    >>> candidates(readBallot('data/simple.csv'))
    ['Aamir', 'Chris', 'Beth']
    >>> candidates([['Abe', 'Carmen'], ['Betsy'], ['Betsy', 'Gina'], []])
    ['Abe', 'Carmen', 'Betsy', 'Gina']
    >>> candidates(readBallot('data/characters.csv'))
    ['Harry Potter', 'Scarlett OHara', 'Samwise Gamgee', 'Elizabeth Bennet']
    >>> candidates([['Jeff', 'Jeff'], ['Jeffery'], ['Jim', 'Jeffery'], ['Joe']])
    ['Jeff', 'Jeffery', 'Jim', 'Joe']
    '''

    results = []
    for Blist in ballots:
        for name in Blist:
            if name not in results:
                results.append(name)
        #makes a list of possible candates in all ballots
    return results


# Part 2.1
def leastVotes(votes, candidates):
    ''' Takes a set of ballots or list of votes and returns the candidate
    or candidates with the lowest number of votes and returs them.

    >>> leastVotes(['Aamir', 'Beth', 'Chris', 'Aamir'], ['Aamir', 'Beth', 'Chris'])
    ['Beth', 'Chris']
    >>> leastVotes(['Abe', 'Abe', 'Betsy', 'Betsy', 'Carmen', 'Dave', 'Eva', 'Frida', 'Frida'], ['Abe', 'Betsy', 'Carmen', 'Dave', 'Eva', 'Frida'])
    ['Carmen', 'Dave', 'Eva']
    >>> leastVotes(['Abe', 'Betsy', 'Betsy'], ['Abe', 'Betsy', 'Carmen'])
    ['Carmen']
    >>> leastVotes(firstChoiceVotes(readBallot('data/simple.csv')),candidates(readBallot('data/simple.csv')))
    ['Chris', 'Beth']
    >>> leastVotes(firstChoiceVotes(readBallot('data/characters.csv')),candidates(readBallot('data/characters.csv')))
    ['Harry Potter', 'Elizabeth Bennet']
    '''
    voteCount = len(votes)
    least = []
    for name in candidates:#takes name of cantadate
        count = votes.count(name)#counts number of appearances
        if count < voteCount:
            voteCount = count
            least = [name] #assigns name of person with lowest votes to least
        elif count == voteCount:
            least.append(name) #adds any ties to least
    return least


# Part 2.2
def majority(votes):
    ''' Takes a list of votes and returns a string representing the winner if
    they have > 50% of the vote, otherwise returns an empty string.

    >>> majority(['Aamir', 'Beth', 'Chris', 'Aamir'])
    ''
    >>> majority(['Abe', 'Abe', 'Abe', 'Betsy', 'Carmen', 'Dave', 'Abe', 'Abe', 'Frida'])
    'Abe'
    >>> majority(['Jim'])
    'Jim'
    >>> majority([])
    ''
    '''
    if len(votes) > 0 and votes.count(mostVotes(votes)[0]) > len(votes) // 2:
        return mostVotes(votes)[0]
        #ensures the list is not empty, then counts the number of votes recieved
        #by the person with the most if they have a majority.
    else:
        return ''
# Part 2.3
def eliminateCandidates(candidates, ballots):
    ''' Takes a list of ballots, makes a new identical list, then it removes
    each name in cantadates from the new ballot and returns the new list of
    ballots.

    >>> eliminateCandidates(['Chris'], readBallot('data/simple.csv'))
    [['Aamir', 'Beth'], ['Beth', 'Aamir'], ['Beth', 'Aamir'], ['Aamir', 'Beth']]
    >>> eliminateCandidates(['Samwise Gamgee', 'Elizabeth Bennet'],readBallot('data/characters.csv')[0:3])
    [['Harry Potter', 'Scarlett OHara'], ['Harry Potter', 'Scarlett OHara'], ['Scarlett OHara', 'Harry Potter']]
    >>> eliminateCandidates([], [['Jim', 'Jeff'], ['Jeff', 'Jim']])
    [['Jim', 'Jeff'], ['Jeff', 'Jim']]
    >>> eliminateCandidates(['Jim', 'Jeff'], [['Jim', 'Jeff'], ['Jeff', 'Jim']])
    [[], []]
    '''
    newBallots = [name for name in ballots]
    for ballots in newBallots:#looks in ballots in new ballots
        for name in candidates:
            if name in ballots:
                ballots.remove(name)#removes names from newBallots
    return newBallots

if __name__ == '__main__':
    # this allows us to run the doctests included in the functions above
    # when the file is run as a script
    from doctest import *
    testmod()
