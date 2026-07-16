from fastapi import FastAPI

from app.infrastructure.database.session import init_db
from app.interfaces.api.error_handlers import register_error_handlers
from app.interfaces.api.v1.courses import router as courses_router
from app.interfaces.api.v1.enrollments import router as enrollments_router
from app.interfaces.api.v1.students import router as students_router
from app.interfaces.api.v1.teachers import router as teachers_router

app = FastAPI(
    title="School System API",
    description="Système de gestion scolaire construit avec les principes de la Clean Architecture.",
    version="1.0.0",
)

register_error_handlers(app)

app.include_router(students_router, prefix="/api/v1")
app.include_router(teachers_router, prefix="/api/v1")
app.include_router(courses_router, prefix="/api/v1")
app.include_router(enrollments_router, prefix="/api/v1")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/", tags=["health"])
def health_check() -> dict:
    return {"status": "ok", "service": "school-system"}