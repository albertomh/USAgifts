import ast

dirpath = r'$PATH'


def clean(year):
    """
    Normalise nation names.

    """

# Get data in from year.txt and dictionary of replacement strings.
    with open(dirpath + 'txt\\' + str(year) + '.txt', encoding='utf8') as infile:
        indata = infile.read()
    giftdata = indata
    with open(dirpath + 'utilities\\' + 'd_replacements.txt', encoding='utf8') as d_infile:
        replacements = ast.literal_eval(d_infile.read())

# Replace strings found in d_replacements.txt.
    for k, v in replacements.items():
        giftdata = giftdata.replace(k, v)

# Write data back to year.txt.
    with open(dirpath + 'txt\\' + str(year) + '.txt', 'wb') as outfile:
        outfile.write(giftdata.encode('utf8'))


def read(year):
    """
    Reads data from the textfiles generated using parseXML.py.
    Returns data evaluated into a usable list.

    """

    with open(dirpath + 'txt\\' + str(year) + '.txt', encoding='utf8') as infile:
        indata = infile.read()
    giftdata = ast.literal_eval(indata)

    return giftdata
