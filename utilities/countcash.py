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

    for nation in contained:
        d_cash[nation] = 0

    re_cash = re.compile('\$(\d*)')

    for row in range(len(giftdata)):
        recash = re_cash.findall(giftdata[row][1])
        recash = list(filter(None, recash))
        recash = list(map(int, recash))

        nationmatch = [x for x in contained if x in giftdata[row][2]]

        if [nationmatch]:
            d_cash[nationmatch[0]] += sum(recash)

    d_cash = {k: v for k, v in d_cash.items() if v is not 0}

    totalcash = sum(d_cash.values())
    maxcash = max(d_cash, key=d_cash.get)

    output = {'total': totalcash, 'cashnation': maxcash, 'topcash': d_cash[maxcash]}

    return output
