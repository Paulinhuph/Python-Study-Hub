from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    nome:  str  = Field(..., min_length=2, max_length=30)
    icone: str  = Field(default="📦")
    cor:   str  = Field(default="#4ade80")


class CategoryUpdate(BaseModel):
    nome:  str | None = Field(default=None, min_length=2, max_length=30)
    icone: str | None = None
    cor:   str | None = None