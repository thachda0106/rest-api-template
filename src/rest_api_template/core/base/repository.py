# core/base_repository.py
from typing import Generic, TypeVar, Type, Optional, List
from sqlmodel import SQLModel, Session, select
from sqlalchemy.orm import load_only

ModelType = TypeVar("ModelType", bound=SQLModel)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: Session):
        self.model = model
        self.session = session

    def get_by_id(self, id: str, **filters) -> Optional[ModelType]:
        stmt = select(self.model).where(self.model.id == id)

        # Apply additional filters, if any
        for field, value in filters.items():
            stmt = stmt.where(getattr(self.model, field) == value)

        return self.session.exec(stmt).first()

    def get_many(self, where: dict = {}, select: list[str] = []) -> List[ModelType]:
        stmt = select(self.model)

        # WHERE filters
        for field, value in where.items():
            stmt = stmt.where(getattr(self.model, field) == value)

        # SELECT specific fields
        if select:
            valid_fields = set(self.model.__annotations__.keys())
            for field in select:
                if field not in valid_fields:
                    raise ValueError(f"Invalid field: {field}")
            stmt = stmt.options(load_only(*(getattr(self.model, field) for field in select)))

        return self.session.exec(stmt).all()


    def create(self, obj: ModelType) -> ModelType:
        try:
            self.session.add(obj)
            self.session.refresh(obj)
            return obj
        except Exception as e:
            raise e

    def delete(self, id: str) -> bool:
        obj = self.get_by_id(id)
        if not obj:
            return False
        try:
            self.session.delete(obj)
            return True
        except  Exception as e:
            self.session.rollback()
            raise e

    def update(self, id: str, data: dict) -> Optional[ModelType]:
        obj = self.get_by_id(id)
        try:
            for key, value in data.items():
                if key in data:
                    setattr(obj, key, value)
            self.session.add(obj)
            self.session.refresh(obj)
            return obj
        except Exception as e:
            raise
