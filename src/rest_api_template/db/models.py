from typing import List, Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, DateTime


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    start:datetime = Field(sa_column=Column(DateTime(timezone=True)))
    end: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True))
    )
    duration: Optional[int] = None

    text: Optional[str] = None
    progress: Optional[int] = None

    parent: Optional[int] = Field(default=None, foreign_key="task.id")
    # could be "task", "summary", "milestone", or custom
    type: Optional[str] = "task"

    open: Optional[bool] = True
    lazy: Optional[bool] = False

    base_start: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True))
    )
    base_end: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True))
    )
    base_duration: Optional[int] = None

    # Relationships (optional depending on your app logic)
    children: List["Task"] = Relationship(
        back_populates="parent_task",
        sa_relationship_kwargs={"remote_side": "Task.id"}
    )
    parent_task: Optional["Task"] = Relationship(
        back_populates="children"
    )


class Link(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source_id: int = Field(foreign_key="task.id")
    target_id: int = Field(foreign_key="task.id")
    type: str

    source_task: Optional[Task] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Link.source_id]"}
    )
    target_task: Optional[Task] = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Link.target_id]"}
    )
