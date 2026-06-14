from pydantic import BaseModel, Field
from typing import Literal


class ChatMessage(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)


class HistoryMessage(BaseModel):
    role:    Literal["user", "assistant"]
    content: str