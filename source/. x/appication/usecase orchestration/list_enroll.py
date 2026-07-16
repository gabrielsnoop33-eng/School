from uuid import UUID

from app.application.dto.enrollment_dto import EnrollmentOutput
from app.domain.repositories.enrollment_repository import EnrollmentRepository


class ListEnrollmentsByStudentUseCase:
    def __init__(self, enrollment_repository: EnrollmentRepository) -> None:
        self._enrollments = enrollment_repository

    def execute(self, student_id: UUID) -> list[EnrollmentOutput]:
        return [
            EnrollmentOutput(
                id=e.id,
                student_id=e.student_id,
                course_id=e.course_id,
                status=e.status.value,
                enrolled_at=e.enrolled_at,
                withdrawn_at=e.withdrawn_at,
            )
            for e in self._enrollments.list_by_student(student_id)
        ]