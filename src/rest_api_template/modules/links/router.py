from typing import List
from fastapi import APIRouter
from src.rest_api_template.db.models import Link
from .dtos.link import LinkDTO
from .repository import LinkRepositoryDep


router = APIRouter()


@router.get("/links/")
async def get_links(repo: LinkRepositoryDep) -> List[Link]:
    Links = repo.get_many()
    return [LinkDTO.model_validate(Link) for Link in Links]
