import PyPDF2
from utils.DataTypeTeller import dataTypeTeller
from utils.PyLogger import PyLogger as logs


def extract_information(pdfFile):
    pdfReader = PyPDF2.PdfReader(pdfFile)
    text = ""
    for page in pdfReader.pages:
        text += page.extract_text() + "\n"
    return text


def extraction(pdf):

    # check if the pdf_path indicates a path or is it a File itself
    if (dataTypeTeller(pdf) == 'String'):
        with open(pdf, 'rb') as file:  
            extracted_text = extract_information(file)
            
        return extracted_text
