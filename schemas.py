from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    student = "student"

class Student_create(BaseModel):
    name : str
    email : str
    password : str
    role: UserRole

class Student_out(BaseModel):
    id : str
    name : str
    email : str
    role : UserRole
    created_at :  datetime
    updated_at : Optional[datetime]
    
    class Config:
        from_attributes=True

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email : Optional[str] = None