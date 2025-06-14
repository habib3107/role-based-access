from fastapi import APIRouter,Depends,Form
from schemas import Student_out,Student_create
from sqlalchemy.orm import Session
from database import get_db
from repository import rep_student
from typing import List
from routers.Oauth_security import get_current_user
from schemas import UserRole
from model import User
from routers.role_checker import allow_roles


router=APIRouter(
    prefix='/student',
    tags=['STUDENT']
)

@router.post('/',response_model=Student_out)
def create_student(
    name : str =Form(...),
    email : str = Form(...),
    password : str = Form(...),
    role: UserRole = Form(...),
    db: Session=Depends(get_db),
    current_get:User = Depends(allow_roles(UserRole.admin))
):
    student_data=Student_create(name=name,email=email,password=password,role=role)

    return rep_student.create_student(student_data,db)

@router.get('/',response_model=List[Student_out])
def get_student(
    db : Session=Depends(get_db),
    current_get:User = Depends(allow_roles(UserRole.admin,UserRole.student))
):
    return rep_student.get_student(db)

@router.get('/{student_id}',response_model=Student_out)
def get_one(
    student_id : str,
    db :Session=Depends(get_db),
    current_get:User = Depends(allow_roles(UserRole.admin,UserRole.student))
):
    return rep_student.get_one_student(student_id,db)