import os
import re
from PyPDF2 import PdfMerger

def sorter(s):
    m = re.compile('[0-9]')
    return m.findall(s)[0]

def combine_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf_file in pdf_list:
        merger.append(pdf_file)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    # Read the list of PDF files from the generated txt file
    with open("pdf_list.txt", "r") as file:
        pdf_list = [line.strip() for line in file]
    # Specify the output path for the combined PDF
    output_path = "AllFormulaSheets.pdf"
    pdf_list.sort(key=sorter)
    # Combine PDFs
    combine_pdfs(pdf_list, output_path)
