from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(frozen=True)
class EnrollStudentInput:
    student_id: UUID
    course_id: UUID


@dataclass(frozen=True)
class EnrollmentOutput:
    id: UUID
    student_id: UUID
    course_id: UUID
    status: str
    enrolled_at: datetime
    withdrawn_at: datetime | None