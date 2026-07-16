from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.student import Student


class StudentRepository(ABC):
    @abstractmethod
    def add(self, student: Student) -> Student:
        ...

    @abstractmethod
    def get_by_id(self, student_id: UUID) -> Student | None:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> Student | None:
        ...

    @abstractmethod
    def list_all(self) -> list[Student]:
        ...

    @abstractmethod
    def update(self, student: Student) -> Student:
        ...

    @abstractmethod
    def delete(self, student_id: UUID) -> None:
        ...