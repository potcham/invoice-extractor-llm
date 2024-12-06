from pydantic import BaseModel, Field
from typing import List, Optional

class Item(BaseModel):
    descripcion: str = Field(..., description="Descripción del producto o servicio.")
    cantidad: Optional[int] = Field(None, description="Cantidad del ítem.")
    precio_unitario: Optional[float] = Field(None, description="Precio unitario del ítem.")
    subtotal: Optional[float] = Field(None, description="Subtotal del ítem.")

class Invoice(BaseModel):
    numero_factura: Optional[str] = Field("", description="Número de la factura.")
    ruc_proveedor: Optional[str] = Field("", description="RUC del proveedor.")
    orden_compra: Optional[str] = Field("", description="Orden de compra asociada.")
    numero_guia: Optional[str] = Field("", description="Número de guía de remisión.")
    fecha_emision: Optional[str] = Field("", description="Fecha de emisión de la factura en formato ISO 8601.")
    fecha_vencimiento: Optional[str] = Field("", description="Fecha de vencimiento de la factura en formato ISO 8601.")
    numero_cuota: Optional[str] = Field("", description="Número de cuota asociada, si aplica.")
    moneda: Optional[str] = Field("", description="Moneda en que está expresada la factura.")
    forma_pago: Optional[str] = Field("", description="Forma de pago indicada en la factura.")
    condicion_pago: Optional[str] = Field("", description="Condiciones de pago.")
    items: List[Item] = Field(default_factory=list, description="Lista de ítems en la factura.")
    subtotal: Optional[float] = Field(None, description="Suma de todos los subtotales.")
    impuestos: Optional[float] = Field(None, description="Monto de los impuestos.")
    monto_total: Optional[float] = Field(None, description="Monto total de la factura.")
