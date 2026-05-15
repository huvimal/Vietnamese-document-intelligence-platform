from pydantic import BaseModel
from typing import List

class InvoiceItem(BaseModel):
    name: str
    quantity: float
    price: float

class InvoiceSchema(BaseModel):
    vendor: str
    tax_code: str
    total_amount: float
    invoice_date: str
    items: List[InvoiceItem]