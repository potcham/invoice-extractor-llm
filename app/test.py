from fastapi.testclient import TestClient
from main import app  # Asegúrate de usar el nombre de tu archivo principal

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Invoice Parser API"}

def test_parse_invoice():
    sample_invoice_text = {
        "invoice_text": """
        Factura N° ELCE-0000913
        RUC: CMM860120KI1
        Proveedor: CASA DE MONEDA DE MÉXICO
        Fecha de emisión: 2017-12-04T12:23:37
        Subtotal: 99.31
        Impuestos: 15.89
        Monto Total: 115.20
        """
    }
    response = client.post("/parse_invoice", json=sample_invoice_text)
    assert response.status_code == 200
    data = response.json()
    assert data["numero_factura"] == "ELCE-0000913"
    assert data["monto_total"] == 115.20
