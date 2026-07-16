from app.application.dto.course_dto import CourseOutput
from app.domain.repositories.course_repository import CourseRepository


class ListCoursesUseCase:
    def __init__(self, course_repository: CourseRepository) -> None:
        self._courses = course_repository

    def execute(self) -> list[CourseOutput]:
        return [
            CourseOutput(
                id=c.id,
                name=c.name,
                teacher_id=c.teacher_id,
                max_capacity=c.max_capacity,
                available_seats=c.available_seats,
                is_full=c.is_full,
            )
            for c in self._courses.list_all()
        ]