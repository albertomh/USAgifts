import os
import time
import xml.etree.ElementTree as ET

dirpath = r'$PATH'


def extract(year):
    """
    Extract data from a given XML file, referenced to by year.
    The /xml directory contains gift registers in $YEAR.xml files.

    """

# Initiate variables.
    start_time = time.perf_counter()
    tree = ET.parse(dirpath + 'xml\\' + str(year) + '.xml')
    l_data = []

# Iterate through XML and extract content.
    for child in tree.iter():
        if child.tag == str('ROW'):
            l_temp = [item.strip() for item in child.itertext()]

# Discard incomplete records, write content to l_data.
            l_temp = list(filter(None, l_temp))
            if len(l_temp) == 4:
                l_data.append(l_temp)

# Write data out to a .txt file.
    with open(dirpath + 'txt\\' + str(year) + '.txt', 'wb') as outfile:
        outfile.write(b'[')
        for row in l_data:
            outfile.write('{}, '.format(row).encode('utf8'))
        outfile.write(b']')

# Print out stats
    time_taken = time.perf_counter() - start_time
    print(str(year) + ': '
          + str(len(l_data))
          + ' gifts recorded. | That took:'
          + '{0:.1f}'.format(time_taken)
          + 'seconds.\n')