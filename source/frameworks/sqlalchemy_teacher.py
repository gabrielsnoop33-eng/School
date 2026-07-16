from uuid import UUID

from sqlalchemy.orm import Session

from app.domain.entities.teacher import Teacher
from app.domain.repositories.teacher_repository import TeacherRepository
from app.infrastructure.database.models import TeacherModel


class SqlAlchemyTeacherRepository(TeacherRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def _to_entity(self, model: TeacherModel) -> Teacher:
        return Teacher(
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            subject=model.subject,
            id=model.id,
            is_active=model.is_active,
        )

    def add(self, teacher: Teacher) -> Teacher:
        model = TeacherModel(
            id=teacher.id,
            first_name=teacher.first_name,
            last_name=teacher.last_name,
            email=teacher.email,
            subject=teacher.subject,
            is_active=teacher.is_active,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)

    def get_by_id(self, teacher_id: UUID) -> Teacher | None:
        model = self._session.get(TeacherModel, teacher_id)
        return self._to_entity(model) if model else None

    def list_all(self) -> list[Teacher]:
        return [self._to_entity(m) for m in self._session.query(TeacherModel).all()]