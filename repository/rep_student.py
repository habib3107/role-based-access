from sqlalchemy.orm import Session
from model import User
from schemas import Student_create
from fastapi import HTTPException
from hashing import Hash

def create_student(request: Student_create, db: Session):
    existing = db.query(User).filter(User.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail='Email already existing')

    last_user = db.query(User).order_by(User.id.desc()).first()
    if last_user:
        last_id_user = int(last_user.id.replace("AA", ""))
        new_id = f"AA{last_id_user + 1}"
    else:
        new_id = "AA1"

    hashed_password = Hash.bcrypt(request.password)

    new_user = User(
        id=new_id,
        name=request.name,
        email=request.email,
        password=hashed_password,
        role=request.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_student(db:Session):
    users= db.query(User).all()
    return users

def get_one_student(student_id : str ,db:Session):
    user=db.query(User).filter(User.id==student_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="student not found")
    return user