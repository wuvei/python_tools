from PyPDF2 import PdfFileReader, PdfFileWriter
def split_pdf(infn, outfn):
    pdf_output = PdfFileWriter()
    pdf_input = PdfFileReader(open(infn, 'rb'))
    # get how many pages there are in the pdf
    page_count = pdf_input.getNumPages()
    print(page_count)
    # to write page 77 to 87 into a new file
    for i in range(76, 87):
        pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))
def merge_pdf(infnList, outfn):
    pdf_output = PdfFileWriter()
    for infn in infnList:
        pdf_input = PdfFileReader(open(infn, 'rb'))
        
        page_count = pdf_input.getNumPages()
        print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
    pdf_output.write(open(outfn, 'wb'))
if __name__ == '__main__':
    infn = 'Proceedings-of-the-Third-International-Conference-on-Electronics-and-Software-Science-ICESS2017-Takamatsu-Japan-2017.pdf'
    outfn = 'outfn.pdf'
    split_pdf(infn, outfn)