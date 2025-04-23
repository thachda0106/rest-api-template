from src.rest_api_template.core.base.repository import BaseRepository
from src.rest_api_template.db.models import Task
from typing import Annotated
from fastapi import Depends
from src.rest_api_template.db.engine import SessionDep
from sqlmodel import Session

class TaskRepository(BaseRepository[Task]):
    def __init__(self, session: Session):
        super().__init__(Task, session)


def get_repo(session: SessionDep):
    repo = TaskRepository(session)
    yield repo

TaskRepositoryDep = Annotated[TaskRepository, Depends(get_repo)]
