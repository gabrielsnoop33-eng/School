from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.use_cases.course.create_course import CreateCourseUseCase
from app.application.use_cases.course.list_courses import ListCoursesUseCase
from app.application.use_cases.enrollment.enroll_student import EnrollStudentUseCase
from app.application.use_cases.enrollment.list_enrollments import ListEnrollmentsByStudentUseCase
from app.application.use_cases.student.create_student import CreateStudentUseCase
from app.application.use_cases.student.get_student import GetStudentUseCase
from app.application.use_cases.student.list_students import ListStudentsUseCase
from app.infrastructure.database.session import SessionLocal
from app.infrastructure.repositories.sqlalchemy_course_repository import SqlAlchemyCourseRepository
from app.infrastructure.repositories.sqlalchemy_enrollment_repository import SqlAlchemyEnrollmentRepository
from app.infrastructure.repositories.sqlalchemy_student_repository import SqlAlchemyStudentRepository
from app.infrastructure.repositories.sqlalchemy_teacher_repository import SqlAlchemyTeacherRepository


def get_db() -> Generator[Session, None, None]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# --- Repositories ---

def get_student_repository(db: Session = Depends(get_db)) -> SqlAlchemyStudentRepository:
    return SqlAlchemyStudentRepository(db)


def get_teacher_repository(db: Session = Depends(get_db)) -> SqlAlchemyTeacherRepository:
    return SqlAlchemyTeacherRepository(db)


def get_course_repository(db: Session = Depends(get_db)) -> SqlAlchemyCourseRepository:
    return SqlAlchemyCourseRepository(db)


def get_enrollment_repository(db: Session = Depends(get_db)) -> SqlAlchemyEnrollmentRepository:
    return SqlAlchemyEnrollmentRepository(db)


# --- Use cases : Student ---

def get_create_student_use_case(
    repo: SqlAlchemyStudentRepository = Depends(get_student_repository),
) -> CreateStudentUseCase:
    return CreateStudentUseCase(repo)


def get_get_student_use_case(
    repo: SqlAlchemyStudentRepository = Depends(get_student_repository),
) -> GetStudentUseCase:
    return GetStudentUseCase(repo)


def get_list_students_use_case(
    repo: SqlAlchemyStudentRepository = Depends(get_student_repository),
) -> ListStudentsUseCase:
    return ListStudentsUseCase(repo)


# --- Use cases : Course ---

def get_create_course_use_case(
    course_repo: SqlAlchemyCourseRepository = Depends(get_course_repository),
    teacher_repo: SqlAlchemyTeacherRepository = Depends(get_teacher_repository),
) -> CreateCourseUseCase:
    return CreateCourseUseCase(course_repo, teacher_repo)


def get_list_courses_use_case(
    repo: SqlAlchemyCourseRepository = Depends(get_course_repository),
) -> ListCoursesUseCase:
    return ListCoursesUseCase(repo)


# --- Use cases : Enrollment ---

def get_enroll_student_use_case(
    student_repo: SqlAlchemyStudentRepository = Depends(get_student_repository),
    course_repo: SqlAlchemyCourseRepository = Depends(get_course_repository),
    enrollment_repo: SqlAlchemyEnrollmentRepository = Depends(get_enrollment_repository),
) -> EnrollStudentUseCase:
    return EnrollStudentUseCase(student_repo, course_repo, enrollment_repo)


def get_list_enrollments_use_case(
    repo: SqlAlchemyEnrollmentRepository = Depends(get_enrollment_repository),
) -> ListEnrollmentsByStudentUseCase:
    return ListEnrollmentsByStudentUseCase(repo)