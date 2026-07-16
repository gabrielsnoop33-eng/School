from uuid import UUID

from app.application.dto.student_dto import StudentOutput
from app.domain.exceptions import EntityNotFoundError
from app.domain.repositories.student_repository import StudentRepository


class GetStudentUseCase:
    def __init__(self, student_repository: StudentRepository) -> None:
        self._students = student_repository

    def execute(self, student_id: UUID) -> StudentOutput:
        student = self._students.get_by_id(student_id)
        if student is None:
            raise EntityNotFoundError(f"Élève {student_id} introuvable.")

        return StudentOutput(
            id=student.id,
            first_name=student.first_name,
            last_name=student.last_name,
            full_name=student.full_name,
            email=student.email,
            birth_date=student.birth_date,
            is_active=student.is_active,
            enrolled_course_ids=student.enrolled_course_ids,
        )