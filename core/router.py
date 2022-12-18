from fastapi import FastAPI
from fa_learn_app.routers import group
from fa_learn_app.routers import student


def set_routers_student(app: FastAPI):
    app.include_router(student.router, prefix="", tags=['students'])

def set_routers_group(app: FastAPI):
    app.include_router(group.router, prefix="", tags=['groups'])