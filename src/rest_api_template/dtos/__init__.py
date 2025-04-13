from enum import Enum
from typing import Optional
from pydantic import BaseModel

class Type(str, Enum):
    e2s = "e2s"
    s2s = "s2s"
    e2e = "e2e"
    s2e = "s2e"

class LinkDTO(BaseModel):
    id: Optional[int]
    source_id: int
    target_id: int
    type: Type

    class Config:
        orm_mode = True
