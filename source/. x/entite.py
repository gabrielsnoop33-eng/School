Entité du domaine : Student.


from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4

from app.domain.exceptions import DomainError


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    email: str
    id: UUID = field(default_factory=uuid4)
    enrolled_course_ids: list[UUID] = field(default_factory=list)
    is_active: bool = True

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        if not self.first_name.strip() or not self.last_name.strip():
            raise DomainError("Le prénom et le nom sont obligatoires.")
        if "@" not in self.email:
            raise DomainError("Email invalide.")
        age = (date.today() - self.birth_date).days // 365
        if age < 3:
            raise DomainError("L'élève doit avoir au moins 3 ans.")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def enroll_in(self, course_id: UUID) -> None:
        """Règle métier : un élève ne peut pas être inscrit deux fois au même cours."""
        if course_id in self.enrolled_course_ids:
            raise DomainError("L'élève est déjà inscrit à ce cours.")
        if not self.is_active:
            raise DomainError("Un élève inactif ne peut pas s'inscrire à un cours.")
        self.enrolled_course_ids.append(course_id)

    def withdraw_from(self, course_id: UUID) -> None:
        if course_id not in self.enrolled_course_ids:
            raise DomainError("L'élève n'est pas inscrit à ce cours.")
        self.enrolled_course_ids.remove(course_id)

    def deactivate(self) -> None:
        self.is_active = False
        """


class DomainError(Exception):
    """Erreur générique de violation d'une règle métier."""


class EntityNotFoundError(DomainError):
    """Levée quand une entité recherchée n'existe pas."""


class AlreadyExistsError(DomainError):
    """Levée quand on tente de créer une entité déjà existante (ex: email dupliqué)."""


class CapacityExceededError(DomainError):
    """Levée quand un cours a atteint sa capacité maximale."""
    from dataclasses import dataclass, field
from uuid import UUID, uuid4

from app.domain.exceptions import DomainError


@dataclass
class Teacher:
    first_name: str
    last_name: str
    email: str
    subject: str
    id: UUID = field(default_factory=uuid4)
    is_active: bool = True

    def __post_init__(self) -> None:
        if not self.first_name.strip() or not self.last_name.strip():
            raise DomainError("Le prénom et le nom du professeur sont obligatoires.")
        if "@" not in self.email:
            raise DomainError("Email invalide.")
        if not self.subject.strip():
            raise DomainError("La matière enseignée est obligatoire.")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
        from dataclasses import dataclass, field
from uuid import UUID, uuid4

from app.domain.exceptions import CapacityExceededError, DomainError


@dataclass
class Course:
    name: str
    teacher_id: UUID
    max_capacity: int
    id: UUID = field(default_factory=uuid4)
    enrolled_student_ids: list[UUID] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise DomainError("Le nom du cours est obligatoire.")
        if self.max_capacity <= 0:
            raise DomainError("La capacité maximale doit être positive.")

    @property
    def available_seats(self) -> int:
        return self.max_capacity - len(self.enrolled_student_ids)

    @property
    def is_full(self) -> bool:
        return self.available_seats <= 0

    def add_student(self, student_id: UUID) -> None:
        """Règle métier centrale : on ne dépasse jamais la capacité max."""
        if student_id in self.enrolled_student_ids:
            raise DomainError("L'élève est déjà inscrit à ce cours.")
        if self.is_full:
            raise CapacityExceededError(
                f"Le cours '{self.name}' a atteint sa capacité maximale "
                f"({self.max_capacity} places)."
            )
        self.enrolled_student_ids.append(student_id)

    def remove_student(self, student_id: UUID) -> None:
        if student_id not in self.enrolled_student_ids:
            raise DomainError("L'élève n'est pas inscrit à ce cours.")
        self.enrolled_student_ids.remove(student_id)
        from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class EnrollmentStatus(str, Enum):
    ACTIVE = "active"
    WITHDRAWN = "withdrawn"
    COMPLETED = "completed"


@dataclass
class Enrollment:
    """
    Entité qui trace la relation entre un élève et un cours dans le temps.
    Séparée de Student/Course pour garder un historique (dates, statut),
    plutôt que de simples listes d'IDs.
    """
    student_id: UUID
    course_id: UUID
    id: UUID = field(default_factory=uuid4)
    status: EnrollmentStatus = EnrollmentStatus.ACTIVE
    enrolled_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    withdrawn_at: datetime | None = None

    def withdraw(self) -> None:
        self.status = EnrollmentStatus.WITHDRAWN
        self.withdrawn_at = datetime.now(timezone.utc)

    def complete(self) -> None:
        self.status = EnrollmentStatus.COMPLETED
