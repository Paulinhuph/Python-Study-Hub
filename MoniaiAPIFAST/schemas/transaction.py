from pydantic import BaseModel, Field
from typing import Literal
from pydantic import UUID4  
from datetime import date

class TransactionCreate(BaseModel):
    descricao: str = Field(..., min_length=3, max_length=50)
    valor: float = Field(..., gt=0, description="Valor deve ser maior que zero")
    tipo: Literal["receita", "despesa"]
    categoria_id: UUID4
    data: date = Field(default_factory=date.today)
    

    