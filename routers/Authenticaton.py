from fastapi import APIRouter,HTTPException,Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from model import User
from hashing import Hash
from routers.token import create_access_token
router=APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(User).filter(User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=404, detail="Incorrect password")
    
    access_token= create_access_token(data={"sub":user.email})
    return {"access_token": access_token,"token_type":"bearer"}
