from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.teacher import Teacher


class TeacherRepository(ABC):
    @abstractmethod
    def add(self, teacher: Teacher) -> Teacher:
        ...

    @abstractmethod
    def get_by_id(self, teacher_id: UUID) -> Teacher | None:
        ...

    @abstractmethod
    def list_all(self) -> list[Teacher]:
        ...