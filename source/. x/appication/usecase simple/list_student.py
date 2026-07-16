from app.application.dto.student_dto import StudentOutput
from app.domain.repositories.student_repository import StudentRepository


class ListStudentsUseCase:
    def __init__(self, student_repository: StudentRepository) -> None:
        self._students = student_repository

    def execute(self) -> list[StudentOutput]:
        return [
            StudentOutput(
                id=s.id,
                first_name=s.first_name,
                last_name=s.last_name,
                full_name=s.full_name,
                email=s.email,
                birth_date=s.birth_date,
                is_active=s.is_active,
                enrolled_course_ids=s.enrolled_course_ids,
            )
            for s in self._students.list_all()
        ]