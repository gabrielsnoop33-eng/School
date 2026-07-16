from fastapi import APIRouter, Depends, status

from app.application.dto.course_dto import CreateCourseInput
from app.application.use_cases.course.create_course import CreateCourseUseCase
from app.application.use_cases.course.list_courses import ListCoursesUseCase
from app.interfaces.api.dependencies import get_create_course_use_case, get_list_courses_use_case
from app.interfaces.api.schemas.course_schema import CourseCreateRequest, CourseResponse

router = APIRouter(prefix="/courses", tags=["courses"])


@router.post("", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(
    payload: CourseCreateRequest,
    use_case: CreateCourseUseCase = Depends(get_create_course_use_case),
) -> CourseResponse:
    result = use_case.execute(
        CreateCourseInput(
            name=payload.name,
            teacher_id=payload.teacher_id,
            max_capacity=payload.max_capacity,
        )
    )
    return CourseResponse(**result.__dict__)


@router.get("", response_model=list[CourseResponse])
def list_courses(
    use_case: ListCoursesUseCase = Depends(get_list_courses_use_case),
) -> list[CourseResponse]:
    return [CourseResponse(**c.__dict__) for c in use_case.execute()]