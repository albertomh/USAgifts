import os


def readPDF():
    """ Creates list of .pdf files in a directory """

    l_pdfs = []
    dirpath = r'C:\Users\Alberto\Documents\Projects\US Gifts Analysis\pdfs\\'

    for file in os.listdir(dirpath):
        if file.endswith(".pdf"):
            l_pdfs.append(file)
    print(l_pdfs)

    
# Read each file referred to in 'l_pdfs' and writes ocntents to 'datadump$YEAR.txt'.

    for pdf in l_pdfs:

        with open(dirpath + pdf, 'rb') as pdfFileObj:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

            pdfyear = ''.join(x for x in pdf if x.isdigit())
            with open(''.join(['datadump', pdfyear, '.txt']), 'a') as txtdump:
                for page in range(pdfReader.getNumPages()):
                    txtdump.write(pdfReader.getPage(page).extractText())
