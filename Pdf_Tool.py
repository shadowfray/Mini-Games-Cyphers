#Shadowfray
'''
A program that uses the tools from PyPDF2 to make a number of subprograms.
These include a page extractor, that makes a new pdf of a range of pages,
a pdf splitter and a pdf merger.
'''

import PyPDF2

def main():
    print(' PDF tools - PYPDF2 '.center(30,'='))
    print('')
    while True:
        print('Please select a method:')
        print('[1] Extract pages from a PDF')
        print('[2] Split a PDF')
        print('[3] Merge two PDFs')
        print('[4] Exit')
        print('')

        try:
            choice = int(input('> '))
        except:
            print('Invalid Command')

        #exit command 
        if choice == 4:
            print('Good bye')
            break
            
        filepath = input('Please input a filepath to the PDF: ')

        #PDF page extractor
        if choice == 1:
            newname = input('Please input a name for the new PDF: ')
            print('Please input an integer for the page you would like to start the extract on.')
            try:
                first = int(input('> '))
            except:
                print('ERROR: Not integer')
                continue
            print('Please input an integer for the page you would like to end the extract on.')
            try:
                last = int(input('> '))
            except:
                print('ERROR: Not integer')
                continue
            page_extractor(filepath, newname, first, last)
            print(f'Extracted new file, {newname}.pdf, pages {first} to {last}')

        #PDF splitter
        if choice == 2:
            newname1 = input('Please input a name for the first new PDF: ')
            newname2 = input('Please input a name for the second new PDF: ')
            print('Please input an integer for the page you would like to split on.')
            try:
                page = int(input('> '))
            except:
                print('ERROR: Not integer')
                continue

            pdf_split(filepath, page, newname1, newname2)
            print(f'Extracted new files.')

        #PDF merger
        if choice == 3:
            path2 = input('Please input a path for the second PDF: ')
            newname = input('Please input a name for the new PDF: ')

            pdf_merge(filepath, path2, newname)
            print('Merged and created new file')
    
def page_extractor(filepath, name='Extracted',start=0,stop=1):
    #Takes a PDF, copies pages from [start] to [stop] into a new pdf with name [name].pdf
    pdfFileObj = open(filepath,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    lengthPdf = pdfReader.getNumPages()
    pdfWriter = PyPDF2.PdfFileWriter()

    if start > stop:
        print('Error: Start bigger than stop.')
        return None
    if stop > lengthPdf:
        print('Stop point is larger than pdf. Defaulting to end of PDF.')
        stop = lengthPdf
        return None
    if start > lengthPdf:
        print('Start point is larger than pdf. Extracting last page.')
        start = lengthPdf - 1
        return None

    for pg in range(start,stop):
        pageObj = pdfReader.getPage(pg)
        pdfWriter.addPage(pageObj)

    OutputFile = open(name + '.pdf', 'wb')
    pdfWriter.write(OutputFile)
    OutputFile.close()
    pdfFileObj.close()

def pdf_split(filepath, pagesplit, name1='Split_1', name2='Split_2'):
    #takes a pdf, splits it after the pagesplit
    pdfFileObj = open(filepath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    lengthPdf = pdfReader.getNumPages()

    newPdf_1 = PyPDF2.PdfFileWriter()
    newPdf_2 = PyPDF2.PdfFileWriter()

    if pagesplit > lengthPdf:
        print('Error: Indicated page to split on does not exist')
        return None

    for page in range(pagesplit):
        adding_page = pdfReader.getPage(page)
        newPdf_1.addPage(adding_page)

    for page in range(pagesplit,lengthPdf):
        adding_page = pdfReader.getPage(page)
        newPdf_2.addPage(adding_page)

    outputFile_1 = open(f'{name1}.pdf','wb')
    outputFile_2 = open(f'{name2}.pdf','wb')
    newPdf_1.write(outputFile_1)
    newPdf_2.write(outputFile_2)
    outputFile_1.close()
    outputFile_2.close()
    pdfFileObj.close()
    

def pdf_merger(filepath1, filepath2,name='Merged'):
    #takes pdf2 and appends it to the end of pdf1
    pdfFile_1 = open(filepath1, 'rb')
    pdfFile_2 = open(filepath1, 'rb')
    pdfReader_1 = PyPDF2.PdfFileReader(pdfFile_1)
    pdfReader_2 = PyPDF2.PdfFileReader(pdfFile_2)
    newPdf = PyPDF2.PdfFileWriter()

    for page in range(pdfReader_1):
        adding_page = pdfReader_1.getPage(page)
        newPdf.addPage(adding_page)

    for page in range(pdfReader_2):
        adding_page = pdfReader_2.getPage(page)
        newPdf.addPage(adding_page)

    outputFile = open(f'{name}.pdf','wb')
    newPdf.write(outputFile)
    outputFile.close()
    pdfFile_1.close()
    pdfFile_2.close()

main()
