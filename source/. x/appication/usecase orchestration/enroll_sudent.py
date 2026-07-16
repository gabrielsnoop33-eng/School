
from app.application.dto.enrollment_dto import EnrollmentOutput, EnrollStudentInput
from app.domain.entities.enrollment import Enrollment
from app.domain.exceptions import EntityNotFoundError
from app.domain.repositories.course_repository import CourseRepository
from app.domain.repositories.enrollment_repository import EnrollmentRepository
from app.domain.repositories.student_repository import StudentRepository


class EnrollStudentUseCase:
    def __init__(
        self,
        student_repository: StudentRepository,
        course_repository: CourseRepository,
        enrollment_repository: EnrollmentRepository,
    ) -> None:
        self._students = student_repository
        self._courses = course_repository
        self._enrollments = enrollment_repository

    def execute(self, data: EnrollStudentInput) -> EnrollmentOutput:
        student = self._students.get_by_id(data.student_id)
        if student is None:
            raise EntityNotFoundError(f"Élève {data.student_id} introuvable.")

        course = self._courses.get_by_id(data.course_id)
        if course is None:
            raise EntityNotFoundError(f"Cours {data.course_id} introuvable.")

        # Règles métier déléguées aux entités elles-mêmes (pas dupliquées ici)
        course.add_student(student.id)
        student.enroll_in(course.id)

        self._courses.update(course)
        self._students.update(student)

        enrollment = Enrollment(student_id=student.id, course_id=course.id)
        saved = self._enrollments.add(enrollment)

        return EnrollmentOutput(
            id=saved.id,
            student_id=saved.student_id,
            course_id=saved.course_id,
            status=saved.status.value,
            enrolled_at=saved.enrolled_at,
            withdrawn_at=saved.withdrawn_at,
        )