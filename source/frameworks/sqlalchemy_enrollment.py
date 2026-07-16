from uuid import UUID

from sqlalchemy.orm import Session

from app.domain.entities.enrollment import Enrollment, EnrollmentStatus
from app.domain.repositories.enrollment_repository import EnrollmentRepository
from app.infrastructure.database.models import EnrollmentModel


class SqlAlchemyEnrollmentRepository(EnrollmentRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def _to_entity(self, model: EnrollmentModel) -> Enrollment:
        return Enrollment(
            student_id=model.student_id,
            course_id=model.course_id,
            id=model.id,
            status=EnrollmentStatus(model.status),
            enrolled_at=model.enrolled_at,
            withdrawn_at=model.withdrawn_at,
        )

    def add(self, enrollment: Enrollment) -> Enrollment:
        model = EnrollmentModel(
            id=enrollment.id,
            student_id=enrollment.student_id,
            course_id=enrollment.course_id,
            status=enrollment.status.value,
            enrolled_at=enrollment.enrolled_at,
            withdrawn_at=enrollment.withdrawn_at,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)

    def list_by_student(self, student_id: UUID) -> list[Enrollment]:
        models = self._session.query(EnrollmentModel).filter_by(student_id=student_id).all()
        return [self._to_entity(m) for m in models]

    def list_by_course(self, course_id: UUID) -> list[Enrollment]:
        models = self._session.query(EnrollmentModel).filter_by(course_id=course_id).all()
        return [self._to_entity(m) for m in models]

    def get_active(self, student_id: UUID, course_id: UUID) -> Enrollment | None:
        model = (
            self._session.query(EnrollmentModel)
            .filter_by(student_id=student_id, course_id=course_id, status="active")
            .first()
        )
        return self._to_entity(model) if model else None

    def update(self, enrollment: Enrollment) -> Enrollment:
        model = self._session.get(EnrollmentModel, enrollment.id)
        model.status = enrollment.status.value
        model.withdrawn_at = enrollment.withdrawn_at
        self._session.commit()
        self._session.refresh(model)
        return self._to_entity(model)