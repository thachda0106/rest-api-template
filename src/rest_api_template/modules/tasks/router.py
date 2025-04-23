from typing import List
from fastapi import APIRouter, HTTPException
from sqlmodel import select
from .dtos.task import TaskDTO
from src.rest_api_template.db.models import Task
from .repository import TaskRepositoryDep
from src.rest_api_template.db.engine import SessionDep
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/tasks/", status_code=200)
async def get_tasks(repo: TaskRepositoryDep) -> List[Task]:
    return repo.get_many()

@router.post("/tasks/", status_code=200)
async def create_task(payload: TaskDTO, repo: TaskRepositoryDep, session: SessionDep) -> int:
    try:
        with session.begin():
            task = Task(**payload.model_dump(exclude_unset=True))
            repo.create(task)
            return task.id
    except Exception as e:
        logger.exception("Failed to create task!")
        raise HTTPException(status_code=500, detail="Internal server error!")


@router.put("/tasks/{id}", status_code=200)
async def update_task(id: int, repo: TaskRepositoryDep):
    task = repo.get_by_id(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{id}", status_code=200)
def delete_task(id: int, repo: TaskRepositoryDep, session: SessionDep):
    try:
        with session.begin():
            task = repo.get_by_id(id)
            if not task:
                raise HTTPException(status_code=404, detail="Task not found")
            repo.delete(task.id)
            return {}
    except Exception as e:
        logger.exception("Failed to delete task!")
        raise HTTPException(status_code=500, detail="Internal server error!")
