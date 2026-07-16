from app.application.dto.course_dto import CourseOutput, CreateCourseInput
from app.domain.entities.course import Course
from app.domain.exceptions import EntityNotFoundError
from app.domain.repositories.course_repository import CourseRepository
from app.domain.repositories.teacher_repository import TeacherRepository


class CreateCourseUseCase:
    def __init__(
        self,
        course_repository: CourseRepository,
        teacher_repository: TeacherRepository,
    ) -> None:
        self._courses = course_repository
        self._teachers = teacher_repository

    def execute(self, data: CreateCourseInput) -> CourseOutput:
        if self._teachers.get_by_id(data.teacher_id) is None:
            raise EntityNotFoundError(f"Professeur {data.teacher_id} introuvable.")

        course = Course(
            name=data.name,
            teacher_id=data.teacher_id,
            max_capacity=data.max_capacity,
        )
        saved = self._courses.add(course)

        return CourseOutput(
            id=saved.id,
            name=saved.name,
            teacher_id=saved.teacher_id,
            max_capacity=saved.max_capacity,
            available_seats=saved.available_seats,
            is_full=saved.is_full,
        )