import ast
from read import read


def findnation(year):
    """
    Returns a list of every nation that gifts in a given year.

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
