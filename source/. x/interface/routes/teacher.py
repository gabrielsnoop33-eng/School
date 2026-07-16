from fastapi import APIRouter, Depends, status

from app.domain.entities.teacher import Teacher
from app.infrastructure.repositories.sqlalchemy_teacher_repository import SqlAlchemyTeacherRepository
from app.interfaces.api.dependencies import get_teacher_repository
from app.interfaces.api.schemas.teacher_schema import TeacherCreateRequest, TeacherResponse

router = APIRouter(prefix="/teachers", tags=["teachers"])


@router.post("", response_model=TeacherResponse, status_code=status.HTTP_201_CREATED)
def create_teacher(
    payload: TeacherCreateRequest,
    repo: SqlAlchemyTeacherRepository = Depends(get_teacher_repository),
) -> TeacherResponse:
    teacher = Teacher(
        first_name=payload.first_name,
        last_name=payload.last_name,
        email=payload.email,
        subject=payload.subject,
    )
    saved = repo.add(teacher)
    return TeacherResponse(
        id=saved.id,
        first_name=saved.first_name,
        last_name=saved.last_name,
        full_name=saved.full_name,
        email=saved.email,
        subject=saved.subject,
        is_active=saved.is_active,
    )


@router.get("", response_model=list[TeacherResponse])
def list_teachers(
    repo: SqlAlchemyTeacherRepository = Depends(get_teacher_repository),
) -> list[TeacherResponse]:
    return [
        TeacherResponse(
            id=t.id,
            first_name=t.first_name,
            last_name=t.last_name,
            full_name=t.full_name,
            email=t.email,
            subject=t.subject,
            is_active=t.is_active,
        )
        for t in repo.list_all()
    ]