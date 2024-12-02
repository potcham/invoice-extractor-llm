from pydantic import BaseModel, Field
from typing import List, Optional

class Item(BaseModel):
    descripcion: str = Field(..., description="Descripción del producto o servicio.")
    cantidad: int = Field(..., description="Cantidad del ítem.")
    precio_unitario: float = Field(..., description="Precio unitario del ítem.")
    subtotal: float = Field(..., description="Subtotal del ítem.")

class Invoice(BaseModel):
    numero_factura: str = Field(..., description="Número de la factura.")
    ruc_proveedor: str = Field(..., description="RUC del proveedor.")
    nombre_proveedor: str = Field(..., description="Nombre del proveedor.")
    fecha_emision: str = Field(..., description="Fecha de emisión de la factura en formato ISO 8601.")
    items: List[Item] = Field(..., description="Lista de ítems en la factura.")
    subtotal: float = Field(..., description="Suma de todos los subtotales.")
    impuestos: Optional[float] = Field(None, description="Monto de los impuestos.")
    monto_total: float = Field(..., description="Monto total de la factura.")
