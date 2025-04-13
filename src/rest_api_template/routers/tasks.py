from typing import List
from fastapi import APIRouter, HTTPException
from sqlmodel import select
from ..dtos.task import TaskDTO
from ..db.engine import SessionDep
from ..db.models import Task

router = APIRouter()


@router.get("/tasks/", status_code=200)
async def get_tasks(session: SessionDep) -> List[Task]:
    tasks = session.exec(select(Task)).all()
    return [TaskDTO.model_validate(task) for task in tasks]


@router.post("/tasks/", status_code=200)
async def create_task(payload: TaskDTO, session: SessionDep) -> int:
    task = Task(**payload.model_dump(exclude_unset=True))
    session.add(task)
    session.commit()
    session.refresh(task)
    return task.id


@router.put("/tasks/{id}", status_code=200)
async def read_user(id: int, session: SessionDep):
    task = session.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{id}", status_code=200)
def delete_hero(id: int, session: SessionDep):
    task = session.get(Task, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {}
