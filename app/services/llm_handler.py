from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
import os
import json
from schemas.invoice import Invoice


load_dotenv()


# Crear el parser basado en Pydantic
invoice_parser = PydanticOutputParser(pydantic_object=Invoice)


def extract_invoice_data_with_items(invoice_text: str) -> dict:
    """
    Usa un modelo LLM para extraer datos detallados de una factura.
    """
    # Configuración del LLM
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

    # Prompt afinado
    prompt = PromptTemplate(
        template=("""
        Eres un experto en análisis de facturas. Extrae información clave de la siguiente factura y devuélvela como un JSON string siguiendo este formato:
        {format_instructions}

        Las claves del JSON son:
        - Número de factura (numero_factura)
        - RUC del proveedor (ruc_proveedor)
        - Orden de compra (orden_compra)
        - Número de guía (numero_guia)
        - Fecha de emisión (fecha_emision)
        - Fecha de vencimiento (fecha_vencimiento)
        - Número de cuota (numero_cuota)
        - Moneda (moneda)
        - Forma de pago (forma_pago)
        - Condición de pago (condicion_pago)
        - Subtotal
        - Impuestos
        - Monto total
        - Ítems: lista con descripción, cantidad, precio unitario, subtotal

        NOTAS IMPORTANTES:
        - No incluyas información del cliente conocida (RUC: 20100163471, NOMBRE: JJC CONTRATISTAS GENERALES S.A, DIRECCIÓN: AV. ALFREDO BENAVIDES...).
        - Asegúrate de capturar el RUC del proveedor correctamente, omitiendo el RUC del cliente.
        - Si algún dato no está disponible, utiliza un string vacío ("") o `null` para valores numéricos.

        Texto de la factura:
        {invoice_text}
        """),
        input_variables=["invoice_text"],
        partial_variables={"format_instructions": invoice_parser.get_format_instructions()},
    )

    # Crear la cadena con LangChain
    chain = prompt | llm 

    try:
        # Ejecutar el LLM con el texto de la factura
        result = chain.invoke({"invoice_text": invoice_text})

        print(result.content)

        # Validar y parsear la salida al modelo Pydantic
        parsed_invoice = invoice_parser.parse(result.content)

        return parsed_invoice.model_dump()
    except Exception as e:
        print(f"Error durante la extracción: {e}")
        return Invoice().model_dump()
