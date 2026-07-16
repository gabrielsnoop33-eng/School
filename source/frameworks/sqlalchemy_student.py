from uuid import UUID

from sqlalchemy.orm import Session

from app.domain.entities.student import Student
from app.domain.repositories.student_repository import StudentRepository
from app.infrastructure.database.models import StudentModel


class SqlAlchemyStudentRepository(StudentRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def _to_entity(self, model: StudentModel) -> Student:
        student = Student(
            first_name=model.first_name,
            last_name=model.last_name,
            birth_date=model.birth_date,
            email=model.email,
            id=model.id,
            is_active=model.is_active,
        )
        student.enrolled_course_ids = [e.course_id for e in model.enrollments if e.status == "active"]
        return student

    def add(self, student: Student) -> Student:
        model = StudentModel(
            id=student.id,
            first_name=student.first_name,
            last_name=student.last_name,
            email=student.email,
            birth_date=student.birth_date,
            is_active=student.is_active,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)

    def get_by_id(self, student_id: UUID) -> Student | None:
        model = self._session.get(StudentModel, student_id)
        return self._to_entity(model) if model else None

    def get_by_email(self, email: str) -> Student | None:
        model = self._session.query(StudentModel).filter_by(email=email).first()
        return self._to_entity(model) if model else None

    def list_all(self) -> list[Student]:
        return [self._to_entity(m) for m in self._session.query(StudentModel).all()]

    def update(self, student: Student) -> Student:
        model = self._session.get(StudentModel, student.id)
        model.first_name = student.first_name
        model.last_name = student.last_name
        model.email = student.email
        model.is_active = student.is_active
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)

    def delete(self, student_id: UUID) -> None:
        model = self._session.get(StudentModel, student_id)
        if model:
            self._session.delete(model)
            self._session.commit()