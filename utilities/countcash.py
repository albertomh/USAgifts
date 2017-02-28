import re
from read import read
from findnation import findnation

dirpath = r'$PATH'


def countcash(year):
    """
    Returns a dictionary containing total cash value of gifts in a year
    as well as the top nation and their total contribution.

    """

    giftdata = read(year)
    contained = findnation(year)
    d_cash = {}
    d_gold = {}

# Populate dictionaries with the gifting nations in a given year.
    for nation in contained:
        d_cash[nation] = 0
        d_gold[nation] = 0

# Regular expressions to find cash, gold, books and alcohol.
    re_cash = re.compile('\$(\d*)')
    re_gold = re.compile('gold', re.IGNORECASE)
    re_book = re.compile('book', re.IGNORECASE)
    re_booze = re.compile('alcohol|wine|whiskey|cognac|champagne|spirits', re.IGNORECASE)
    totalbook = 0
    totalbooze = 0

    for row in range(len(giftdata)):
        recash = re_cash.findall(giftdata[row][1])
        recash = list(filter(None, recash))
        recash = list(map(int, recash))
        regold = re_gold.findall(giftdata[row][1])
        rebook = re_book.findall(giftdata[row][1])
        rebooze = re_booze.findall(giftdata[row][1])

        nationmatch = [x for x in contained if x in giftdata[row][2]]

        if [nationmatch]:
            d_cash[nationmatch[0]] += sum(recash)
        if regold:
            d_gold[nationmatch[0]] += len(regold)
        if rebook:
            totalbook += len(rebook)
        if rebooze:
            totalbooze += len(rebooze)

    d_cash = {k: v for k, v in d_cash.items() if v is not 0}
    d_gold = {k: v for k, v in d_gold.items() if v is not 0}

    totalcash = sum(d_cash.values())
    maxcash = max(d_cash, key=d_cash.get)
    totalgold = sum(d_gold.values())
    maxgold = max(d_gold, key=d_gold.get)

    output = {'total': totalcash, 'cashnation': maxcash, 'topcash': d_cash[maxcash],
              'totalgold': totalgold, 'goldnation': maxgold, 'topgold': d_gold[maxgold],
              'books': totalbook, 'booze': totalbooze}

    return output


def bynation(year, nation):
    """
    NEEDS DOCUMENTING!
    bynation(1999, "China") returns China: $8,380.00

    """

    giftdata = read(year)
    results = []

# NEEDS DOCUMENTING!
    for row in range(len(giftdata)):
        if nation in giftdata[row][2]:
            results.append(giftdata[row][1])

# NEEDS DOCUMENTING!
    re_cash = re.compile('\$(\d*)')
    totalcash = []
    for gift in range(len(results)):
        recash = re_cash.findall(results[gift])
        recash = list(filter(None, recash))
        recash = list(map(int, recash))
        totalcash.extend(recash)

    d_results = (nation, sum(totalcash))

    return d_results  # nation + ': ${:,.2f}'.format(sum(totalcash)))
