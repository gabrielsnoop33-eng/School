from uuid import UUID

from pydantic import BaseModel, Field


class CourseCreateRequest(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    teacher_id: UUID
    max_capacity: int = Field(gt=0)


class CourseResponse(BaseModel):
    id: UUID
    name: str
    teacher_id: UUID
    max_capacity: int
    available_seats: int
    is_full: bool

    model_config = {"from_attributes": True}