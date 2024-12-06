import pymupdf  # PyMuPDF

def extract_text_with_pymupdf(file_path: str) -> str:
    """
    Extrae texto de un PDF usando PyMuPDF.
    """
    with pymupdf.open(file_path) as pdf:
        text = ""
        for page in pdf:
            text += page.get_text()
    return text


import pdfplumber

def extract_text_with_pdfplumber(pdf_path: str) -> str:
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()  # Extrae el texto respetando los espaciados
        return text
