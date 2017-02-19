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