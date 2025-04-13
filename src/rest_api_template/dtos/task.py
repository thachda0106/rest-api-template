from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime

from enum import Enum

from sqlmodel import Field

class TaskType(str, Enum):
    task = "task"
    summary = "summary"
    milestone = "milestone"


class TaskDTO(BaseModel):
    id: Optional[Union[int, str]] = None
    start: datetime
    end: Optional[datetime] = None
    duration: Optional[int] = None
    text: Optional[str] = None
    progress: Optional[int] = None
    parent: Optional[Union[int, str]] = None
    type: Optional[TaskType] = Field(default=TaskType.task)
    open: Optional[bool] = True
    lazy: Optional[bool] = False
    base_start: Optional[datetime] = None
    base_end: Optional[datetime] = None
    base_duration: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True
