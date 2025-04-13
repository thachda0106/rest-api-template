from typing import List, Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    duration: int
    progress: int
    parent_id: Optional[int] = Field(default=None, foreign_key="task.id")
    type: str
    lazy: bool
    open: bool
    index: int = Field(default=0, exclude=True)

    children: List["Task"] = Relationship(
        back_populates="parent", sa_relationship_kwargs={"remote_side": "Task.id"}
    )
    parent: Optional["Task"] = Relationship(
        back_populates="children"
    )

    outgoing_links: List["Link"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Task.id == Link.source_id"
        }
    )

    incoming_links: List["Link"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Task.id == Link.target_id"
        }
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
