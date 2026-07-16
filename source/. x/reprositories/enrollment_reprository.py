from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.enrollment import Enrollment


class EnrollmentRepository(ABC):
    @abstractmethod
    def add(self, enrollment: Enrollment) -> Enrollment:
        ...

    @abstractmethod
    def list_by_student(self, student_id: UUID) -> list[Enrollment]:
        ...

    @abstractmethod
    def list_by_course(self, course_id: UUID) -> list[Enrollment]:
        ...

    @abstractmethod
    def get_active(self, student_id: UUID, course_id: UUID) -> Enrollment | None:
        ...

    @abstractmethod
    def update(self, enrollment: Enrollment) -> Enrollment:
        ...