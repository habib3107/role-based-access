from jose import jwt,JWTError
from datetime import datetime,timedelta
from schemas import TokenData

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data :dict,expires_delta : timedelta=timedelta(minutes=5)):
    to_encode=data.copy()
    expire= datetime.utcnow()+expires_delta
    to_encode.update({"exp":expire})
    encrypt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encrypt

def verify_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email : str = payload.get("sub")
        if email is None :
            raise credentials_exception
        token_data=TokenData(email=email)
        return token_data
    except JWTError:
        raise credentials_exception