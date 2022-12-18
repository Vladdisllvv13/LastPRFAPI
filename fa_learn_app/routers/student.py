from typing import List
import uuid
from fastapi import APIRouter, Depends
from fa_learn_app.dependencies_student import get_student_repo
from fa_learn_app.models.student import StudentIn, StudentOut, StudentStorage
from fa_learn_app.repositories.student import BaseProductRepository


router = APIRouter()

@router.get("/students", response_model = List[StudentOut])
async def get_students(
        student_repo :BaseProductRepository = Depends(get_student_repo),
        limit :int = 100,
        skip :int = 0
    ):
    return student_repo.get_all(limit=limit, skip=skip)

@router.get("/student", response_model = StudentOut)
async def get_student(
        id :uuid.UUID,
        student_repo :BaseProductRepository = Depends(get_student_repo),
    ):
    return student_repo.get_by_id((id))

@router.post("/student", response_model = StudentOut) ##HERE
async def create_student(
        student_in :StudentIn,
        student_repo :BaseProductRepository = Depends(get_student_repo),
    ):
    return student_repo.create(student_in)

@router.put("/student", response_model = StudentOut | str)
async def update_students(
        id: uuid.UUID,
        student_in: StudentIn,
        student_repo: BaseProductRepository = Depends(get_student_repo),
        ):
    return student_repo.update_student(id, student_in)

@router.delete("/student", response_model=str)
async def delete_student(
        id: uuid.UUID,
        student_repo: BaseProductRepository = Depends(get_student_repo),
        ):
    return student_repo.delete(id)
