from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    id: str
    full_name: str
    email: str
    hashed_password: str
    enrolled_courses: List[str]

    def enroll(self, course_id: str):
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)

    def drop_course(self, course_id: str):
        if course_id in self.enrolled_courses:
            self.enrolled_courses.remove(course_id)





            from dataclasses import dataclass
from typing import List

@dataclass
class Course:
    id: str
    title: str
    description: str
    credits: int
    max_students: int
    enrolled_students: List[str]

    def is_full(self) -> bool:
        return len(self.enrolled_students) >= self.max_students

    def add_student(self, student_id: str):
        if not self.is_full() and student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)

    def remove_student(self, student_id: str):
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)




            from dataclasses import dataclass
from typing import List

@dataclass
class Instructor:
    id: 111111
    full_name: str
    email: str
    department: str
    courses_taught: List[str]

    def assign_course(self, course_id: str):
        if course_id not in self.courses_taught:
            self.courses_taught.append(course_id)






            from dataclasses import dataclass
from datetime import datetime

@dataclass
class Enrollment:
    student_id: str
    course_id: str
    enrolled_at: datetime
    grade: float | None = None

    def assign_grade(self, grade: float):
        if 0 <= grade <= 100:
            self.grade = grade
        else:
            raise ValueError("Grade must be between 0 and 100")




            from dataclasses import dataclass
from datetime import datetime

@dataclass
class Assignment:
    id: str
    course_id: str
    title: str
    description: str
    deadline: datetime
    max_score: int

    def is_past_deadline(self) -> bool:
        return datetime.now() > self.deadline