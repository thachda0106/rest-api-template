from src.rest_api_template.core.base.repository import BaseRepository
from src.rest_api_template.db.models import Link
from typing import Annotated
from fastapi import Depends
from src.rest_api_template.db.engine import SessionDep
from sqlmodel import Session

class LinkRepository(BaseRepository[Link]):
    def __init__(self, session: Session):
        super().__init__(Link, session)


def get_repo(session: SessionDep):
    repo = LinkRepository(session)
    yield repo

LinkRepositoryDep = Annotated[LinkRepository, Depends(get_repo)]
