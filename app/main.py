from fastapi import FastAPI, UploadFile, File
import os
from services.pdf_reader import extract_text_with_pymupdf
from services.llm_handler import extract_invoice_data_with_items

app = FastAPI()

@app.post("/extract")
async def extract_invoice(file: UploadFile = File(...)):
    # Guardar archivo temporal
    temp_file = f"/tmp/{file.filename}"
    with open(temp_file, "wb") as f:
        f.write(file.file.read())

    # Extraer texto del PDF
    invoice_text = extract_text_with_pymupdf(temp_file)

    # Usar el modelo LLM para estructurar los datos
    try:
        data = extract_invoice_data_with_items(invoice_text)
    except Exception as e:
        return {"error": str(e)}

    # Limpiar archivo temporal
    os.remove(temp_file)

    return data
