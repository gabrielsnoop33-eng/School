from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.application.dto.student_dto import CreateStudentInput
from app.application.use_cases.student.create_student import CreateStudentUseCase
from app.application.use_cases.student.get_student import GetStudentUseCase
from app.application.use_cases.student.list_students import ListStudentsUseCase
from app.interfaces.api.dependencies import (
    get_create_student_use_case,
    get_get_student_use_case,
    get_list_students_use_case,
)
from app.interfaces.api.schemas.student_schema import StudentCreateRequest, StudentResponse

router = APIRouter(prefix="/students", tags=["students"])


@router.post("", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(
    payload: StudentCreateRequest,
    use_case: CreateStudentUseCase = Depends(get_create_student_use_case),
) -> StudentResponse:
    result = use_case.execute(
        CreateStudentInput(
            first_name=payload.first_name,
            last_name=payload.last_name,
            birth_date=payload.birth_date,
            email=payload.email,
        )
    )
    return StudentResponse(**result.__dict__)


@router.get("/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: UUID,
    use_case: GetStudentUseCase = Depends(get_get_student_use_case),
) -> StudentResponse:
    result = use_case.execute(student_id)
    return StudentResponse(**result.__dict__)


@router.get("", response_model=list[StudentResponse])
def list_students(
    use_case: ListStudentsUseCase = Depends(get_list_students_use_case),
) -> list[StudentResponse]:
    return [StudentResponse(**s.__dict__) for s in use_case.execute()]