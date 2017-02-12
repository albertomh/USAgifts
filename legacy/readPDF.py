import os


def readPDF():
    """ Creates list of .pdf files in a directory """

    l_pdfs = []
    dirpath = r'C:\Users\Alberto\Documents\Projects\US Gifts Analysis\pdfs\\'

    for file in os.listdir(dirpath):
        if file.endswith(".pdf"):
            l_pdfs.append(file)
    print(l_pdfs)
