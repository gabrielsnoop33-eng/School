from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateCourseInput:
    name: str
    teacher_id: UUID
    max_capacity: int


@dataclass(frozen=True)
class CourseOutput:
    id: UUID
    name: str
    teacher_id: UUID
    max_capacity: int
    available_seats: int
    is_full: bool