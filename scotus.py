# Support function for analyzing the decisions of the Supreme Court.
# Much of this work follows that of Fowler (see paper directory).

# STUDENTS: add code at places marked "pass",
#           and Remove pass-es before submitting.
"""
This module provides a number of methods that support the analysis of
Supreme Court of the United States (SCOTUS) decisions.

It provides three important functions:
   readDecisions - read yearly dockets of cases and their citation counts
   hIndex - given a list of citation counts, compute the 'h-index'
   plotImpacts - plot the h-index for each year's docket of cases
   readCourts - assembles a dictionary that maps the name of a justice to a
                tuple of case citations
    byImpact - a 'key function' for use for sorting tuples by citation count
    rankJustices - constructs a list of (justice, hIndex) pairs sorted in
                    decreasing order of hIndex
"""
import csv
import matplotlib.pyplot as plt

def readDecisions(filename):
    """
    This function takes the name of a CSV file (string) containing Supreme Court
    data and creates a dictionary that maps a year (int) to that year's docket
    (a tuple of case citation counts).

    >>> len(readDecisions('data/judicial.csv'))
    235
    >>> db = readDecisions('data/judicial.csv')
    >>> (min(db), max(db))  # range of dates for decisions
    (1754, 2002)
    >>> max(readDecisions('data/judicial.csv'))
    2002
    >>> readDecisions('data/judicial.csv')[1793]
    (0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 31, 0, 0, 0, 0, 0)
    >>> [ year in db for year in [ 1753, 1754, 1755 ] ]
    [False, True, False]
    >>> db[1783]
    (0, 1, 0)
    >>> db[1784]
    (1, 0, 1, 0, 0, 0, 0, 0, 1, 0)
    >>> 1754 in db
    True
    >>> len(db[2002])
    17

    """
    # a dictionary that maps a year (key) to a tuple of citation counts (indeg)
    db = dict()

    with open(filename) as caseFile:
        for row in csv.reader(caseFile):
            # ignore the top header line in caseFile
            if row[0][0].isalpha() is False:

                year = int(row[3])
                docket = int(row[8])

            # update your dictionary (db)
                if year in db:
                    db[year] += (docket,)
                else:
                    db[year] = (docket,)

    # return the accumulated data
    return db

def hIndex(citations):
    """Computes and returns the h-index (int) of citations (tuple of citation counts).

    >>> hIndex( (0, 2, 15, 9, 7, 48, 4, 82, 14, 6) )
    6
    >>> hIndex( (2, 2, 2, 2) )
    2
    >>> hIndex( (5, 4, 3, 2, 1) )
    3
    >>> hIndex( (0, 0) )
    0
    >>> hIndex((0,1,2,3,19))
    2
    >>> hIndex((0,))
    0
    >>> hIndex((100, 120, 4, 1800, 0, 0))
    4
    """
    cite = sorted(list(citations), reverse=True)
    count = 0
    for number in cite:
        if number > count:
            count += 1
        else:
            return count

    # Takes the citations and sorts them from least to greatest then returns
    # the number  x where is the number of papers that have all been cited over
    # x times

def plotImpacts(dockets, plotFilename):
    """Generate a line plot of the h-index associated with each year in
    the database, dockets (dictionary).  Plot saved as file with name found in
    plotFilename (string).
    """
    # 1. extract all the years into a list, sorted into increasing order.
    years = sorted(dockets.keys())

    # 2. compute a list of hIndex values for each year's case citations
    impacts = []
    for year in years:
        impacts.append(hIndex(dockets[year]))


    # 3. generate the plot (see lab handout)
    plt.title('Impact of Surpreme Court Decisions')
    plt.xlabel('Year')
    plt.ylabel('H - Index score')
    plt.plot(years, impacts, 'b-')
    plt.savefig(plotFilename)

def readCourts(justiceFilename,dockets):
    """Given a justiceFilename (string) a path to csv file of Chief Justices and
    their terms (name, start-year, end-year) and a database of case citation
    counts called dockets (dict), assemble and return a dictionary that maps the name
    of a justice to a tuple of case citations.

    >>> len(readCourts('data/chiefJustices.csv', readDecisions('data/judicial.csv')))
    16
    >>> db = readDecisions('data/judicial.csv')
    >>> cjdb = readCourts('data/chiefJustices.csv', db)
    >>> cjdb['John Rutledge'] == db[1795]
    True
    >>> cjdb['Oliver Ellsworth'] == db[1796]+db[1797]+db[1798]+db[1799]+db[1800]
    True
    """
    cjd = dict()
    with open(justiceFilename) as f:
        for row in csv.reader(f):
            if row[-1][0].isalpha() is False:
                count = int(row[1])
                #sets count to the first year of the justices term.

                while count <= int(row[2]):
                    if row[0] not in cjd:
                        cjd[row[0]] = dockets.get(int(row[1]))
                        count += 1
                        # adds the name of the justice to the dictionary as a key
                        # and adds the first years case citations as the value
                        # then increases the year by 1

                    elif dockets.get(count) == None:
                        count +=1
                        #skips years with no decisions

                    else:
                        cjd[row[0]] += dockets.get(count)
                        count += 1
                        # adds any additional years citations that the chief
                        # justice oversaw and then goes to the next years citations
                        # until it reaches the year after that justice was replaced
                        # then moves to the next chief justice
    return cjd

def byImpact(pair):
    """A 'key function' for use in sorted.

    >>> byImpact( ('John Jay', 5 ) )
    5
    """
    name, impact = pair
    return impact

def rankJustices(cjdb):
    """Construct a list of (justice, hIndex) pairs sorted in decreasing order
    of hIndex given cjdb (dict).

    >>> db = readDecisions('data/judicial.csv')
    >>> cjdb = readCourts('data/chiefJustices.csv', db)
    >>> rankJustices(cjdb)[-2]
    ('John Jay', 5)
    """
    rank = []
    for key in cjdb:
        rank.append((key, hIndex(cjdb[key])))
        # takes the name of a justice and adds a tuple of their name
        # and hIndex score to a list

    return sorted(rank, key = byImpact, reverse = True)
        #sorts and returns rank from greatest to least hIndex.

def test():
    """Exercise document tests."""
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()  # check to make sure methods are correct

    # 1. read in decisions
    db = readDecisions('data/judicial.csv')

    # 2. plot their impacts
    plotImpacts(db, 'scotusImpact.pdf')

    # 3. Read in the court impacts
    courtDB = readCourts('data/chiefJustices.csv',db)

    # 4. Build rankings
    ranking = rankJustices(courtDB)

    # 5. Print the rankings out
    for court, impact in ranking:
        print("{}: {}".format(court,impact))
