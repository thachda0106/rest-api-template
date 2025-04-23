from enum import Enum
from pydantic import BaseModel
from typing import Optional

class LinkType(str, Enum):
    e2s = "e2s"
    s2s = "s2s"
    e2e = "e2e"
    s2e = "s2e"

class LinkDTO(BaseModel):
    id: Optional[int]
    source_id: int
    target_id: int
    type: LinkType

    class Config:
        orm_mode = True
        from_attributes = True
