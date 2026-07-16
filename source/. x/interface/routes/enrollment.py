from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.application.dto.enrollment_dto import EnrollStudentInput
from app.application.use_cases.enrollment.enroll_student import EnrollStudentUseCase
from app.application.use_cases.enrollment.list_enrollments import ListEnrollmentsByStudentUseCase
from app.interfaces.api.dependencies import get_enroll_student_use_case, get_list_enrollments_use_case
from app.interfaces.api.schemas.enrollment_schema import EnrollmentCreateRequest, EnrollmentResponse

router = APIRouter(prefix="/enrollments", tags=["enrollments"])


@router.post("", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll_student(
    payload: EnrollmentCreateRequest,
    use_case: EnrollStudentUseCase = Depends(get_enroll_student_use_case),
) -> EnrollmentResponse:
    result = use_case.execute(
        EnrollStudentInput(student_id=payload.student_id, course_id=payload.course_id)
    )
    return EnrollmentResponse(**result.__dict__)


@router.get("/student/{student_id}", response_model=list[EnrollmentResponse])
def list_enrollments_by_student(
    student_id: UUID,
    use_case: ListEnrollmentsByStudentUseCase = Depends(get_list_enrollments_use_case),
) -> list[EnrollmentResponse]:
    return [EnrollmentResponse(**e.__dict__) for e in use_case.execute(student_id)]