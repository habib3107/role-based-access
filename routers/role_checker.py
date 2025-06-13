from fastapi import Depends,HTTPException,status
from model import User
from schemas import UserRole
from routers.Oauth_security import get_current_user

def allow_roles(*allowed_roles : UserRole):
    def role_dependency(current_user : User =Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Access denied . Required roles :{allowed_roles}")
        return current_user
    return role_dependency