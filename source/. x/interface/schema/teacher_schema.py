from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class TeacherCreateRequest(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    subject: str = Field(min_length=1, max_length=100)


class TeacherResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    full_name: str
    email: str
    subject: str
    is_active: bool

    model_config = {"from_attributes": True}