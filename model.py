from sqlalchemy import Column ,String,DateTime,func
from database import Base
from schemas import UserRole
from sqlalchemy import Enum as SqlEnum

class User(Base):
    __tablename__="Student"
    id = Column(String(50),primary_key=True,index=True)
    name=Column(String(100),nullable=False)
    email=Column(String(100),nullable=False,unique=True,index=True)
    password=Column(String(100),nullable=False)
    role = Column(SqlEnum(UserRole), nullable=False)  # 👈 Use Enum in DB
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),onupdate=func.now())

    