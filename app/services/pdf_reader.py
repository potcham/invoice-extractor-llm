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
