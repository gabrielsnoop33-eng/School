"""
Schémas Pydantic : format d'entrée/sortie HTTP UNIQUEMENT.

Ces schémas ne sont utilisés que dans la couche interfaces/api.
Ils ne circulent jamais dans les use cases (qui utilisent les DTOs)
ni dans le domaine (qui utilise les entités). Cette séparation permet
de faire évoluer l'API REST sans toucher à la logique métier.
"""
from datetime import date
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class StudentCreateRequest(BaseModel):
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    birth_date: date
    email: EmailStr


class StudentResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    full_name: str
    email: str
    birth_date: date
    is_active: bool
    enrolled_course_ids: list[UUID]

    model_config = {"from_attributes": True}