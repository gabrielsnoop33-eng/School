"""
DTOs (Data Transfer Objects) : structures simples utilisées pour faire
transiter des données entre les use cases et les couches externes,
sans exposer directement les entités du domaine ni les schémas HTTP.
"""
from dataclasses import dataclass
from datetime import date
from uuid import UUID


@dataclass(frozen=True)
class CreateStudentInput:
    first_name: str
    last_name: str
    birth_date: date
    email: str


@dataclass(frozen=True)
class StudentOutput:
    id: UUID
    first_name: str
    last_name: str
    full_name: str
    email: str
    birth_date: date
    is_active: bool
    enrolled_course_ids: list[UUID]