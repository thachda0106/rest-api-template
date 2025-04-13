from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine
from .models import *
from ..configs.env import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]