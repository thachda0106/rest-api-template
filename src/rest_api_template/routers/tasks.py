from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks/")
async def read_tasks():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/tasks/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/tasks/{username}")
async def read_user(username: str):
    return {"username": username}
