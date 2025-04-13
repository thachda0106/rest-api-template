from fastapi import APIRouter

router = APIRouter()


@router.get("/links/")
async def read_links():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/links/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/links/{username}")
async def read_user(username: str):
    return {"username": username}
