from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from routers.token import verify_token
from model import User

oauth2_Scheme=OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token :str = Depends(oauth2_Scheme),db:Session=Depends(get_db)):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,\
        detail='could not validate credentails',
        headers={"www-Authenticate": "Bearer"}
    )
    token_data=verify_token(token,credentials_exception)
    user=db.query(User).filter(User.email==token_data.email).first()
    if user is None:
        raise credentials_exception
    return user