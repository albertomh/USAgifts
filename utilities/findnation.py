import ast
from read import read


def findnation(year, *args):
    """
    Returns a list of every nation that gifts in a given year.
    findnation(year).count('nation') returns number of gifts from a single nation.

    Run findnation(year, "missing") to return list of records missing gifter nation data.

    """

# Initialise lists with processed data and list of nations.
    giftdata = read(year)
    with open('l_nations.txt', encoding='utf8') as infile:
        indata = infile.read()
    nations = ast.literal_eval(indata)

# Populate 'contained' with every instance of a nation found in 'giftdata'.
    contained = []
    for row in range(len(giftdata)):
        nationmatch = [x for x in nations if x in giftdata[row][2]]
        contained.extend(nationmatch)

# Code to evaluate *args and return all records missing gifter nation.
        if args:
            if not nationmatch:
                print(giftdata[row][2], '\n\n')

    contained = list(set(contained))  # Remove set to return every instance.
    return contained
