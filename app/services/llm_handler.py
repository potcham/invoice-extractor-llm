# from langchain.llms import OpenAI
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
        Eres un experto en análisis de facturas. Extrae información clave de la siguiente factura y devuélvela como JSON en este formato:
        {format_instructions}

        Texto de la factura:
        {invoice_text}
        """),
        input_variables=["invoice_text"],
        partial_variables={"format_instructions": invoice_parser.get_format_instructions()},
    )

    # Crear la cadena con LangChain
    chain = prompt | llm # LLMChain(llm=llm, prompt=prompt)
    # structured_data = chain.invoke({"invoice_text": text})

    # Ejecutar el LLM con el texto de la factura
    result = chain.invoke({"invoice_text": invoice_text})

    print(result.content)

    # Validar y parsear la salida al modelo Pydantic
    parsed_invoice = invoice_parser.parse(result.content)

    return parsed_invoice

    # # Convertir el resultado a un diccionario
    # # print(structured_data)
    # print(structured_data.content)
    # # print(structured_data["text"])

    # output = json.loads(structured_data.content)
    # print("output_format: ", output)

    # return eval(structured_data)
