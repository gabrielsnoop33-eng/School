import uuid

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class StudentModel(Base):
    __tablename__ = "students"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    birth_date: Mapped[Date] = mapped_column(Date)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    enrollments: Mapped[list["EnrollmentModel"]] = relationship(back_populates="student")


class TeacherModel(Base):
    __tablename__ = "teachers"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    subject: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class CourseModel(Base):
    __tablename__ = "courses"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(150))
    teacher_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teachers.id"))
    max_capacity: Mapped[int] = mapped_column(Integer)

    enrollments: Mapped[list["EnrollmentModel"]] = relationship(back_populates="course")


class EnrollmentModel(Base):
    __tablename__ = "enrollments"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    student_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("students.id"))
    course_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("courses.id"))
    status: Mapped[str] = mapped_column(String(20), default="active")
    enrolled_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    withdrawn_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    student: Mapped["StudentModel"] = relationship(back_populates="enrollments")
    course: Mapped["CourseModel"] = relationship(back_populates="enrollments")