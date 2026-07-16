from app.application.dto.student_dto import CreateStudentInput, StudentOutput
from app.domain.entities.student import Student
from app.domain.exceptions import AlreadyExistsError
from app.domain.repositories.student_repository import StudentRepository


class CreateStudentUseCase:
    def __init__(self, student_repository: StudentRepository) -> None:
        self._students = student_repository

    def execute(self, data: CreateStudentInput) -> StudentOutput:
        if self._students.get_by_email(data.email) is not None:
            raise AlreadyExistsError(f"Un élève avec l'email {data.email} existe déjà.")

        student = Student(
            first_name=data.first_name,
            last_name=data.last_name,
            birth_date=data.birth_date,
            email=data.email,
        )
        saved = self._students.add(student)

        return StudentOutput(
            id=saved.id,
            first_name=saved.first_name,
            last_name=saved.last_name,
            full_name=saved.full_name,
            email=saved.email,
            birth_date=saved.birth_date,
            is_active=saved.is_active,
            enrolled_course_ids=saved.enrolled_course_ids,
        )