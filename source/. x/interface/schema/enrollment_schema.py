from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class EnrollmentCreateRequest(BaseModel):
    student_id: UUID
    course_id: UUID


class EnrollmentResponse(BaseModel):
    id: UUID
    student_id: UUID
    course_id: UUID
    status: str
    enrolled_at: datetime
    withdrawn_at: datetime | None

    model_config = {"from_attributes": True}