from uuid import UUID

from sqlalchemy.orm import Session

from app.domain.entities.course import Course
from app.domain.repositories.course_repository import CourseRepository
from app.infrastructure.database.models import CourseModel


class SqlAlchemyCourseRepository(CourseRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def _to_entity(self, model: CourseModel) -> Course:
        course = Course(
            name=model.name,
            teacher_id=model.teacher_id,
            max_capacity=model.max_capacity,
            id=model.id,
        )
        course.enrolled_student_ids = [e.student_id for e in model.enrollments if e.status == "active"]
        return course

    def add(self, course: Course) -> Course:
        model = CourseModel(
            id=course.id,
            name=course.name,
            teacher_id=course.teacher_id,
            max_capacity=course.max_capacity,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)

    def get_by_id(self, course_id: UUID) -> Course | None:
        model = self._session.get(CourseModel, course_id)
        return self._to_entity(model) if model else None

    def list_all(self) -> list[Course]:
        return [self._to_entity(m) for m in self._session.query(CourseModel).all()]

    def update(self, course: Course) -> Course:
        model = self._session.get(CourseModel, course.id)
        model.name = course.name
        model.max_capacity = course.max_capacity
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)