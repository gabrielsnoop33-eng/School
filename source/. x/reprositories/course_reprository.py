from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.course import Course


class CourseRepository(ABC):
    @abstractmethod
    def add(self, course: Course) -> Course:
        ...

    @abstractmethod
    def get_by_id(self, course_id: UUID) -> Course | None:
        ...

    @abstractmethod
    def list_all(self) -> list[Course]:
        ...

    @abstractmethod
    def update(self, course: Course) -> Course:
        ...