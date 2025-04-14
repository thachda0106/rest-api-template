from typing import List
from fastapi import APIRouter
from sqlmodel import select
from ..db.engine import SessionDep
from ..db.models import Link
from ..dtos.link import LinkDTO

router = APIRouter()


@router.get("/links/")
async def get_links(session: SessionDep) -> List[Link]:
    Links = session.exec(select(Link)).all()
    return [LinkDTO.model_validate(Link) for Link in Links]