from fastapi import Depends
import tokens
from fastapi import HTTPException,Depends,status
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Unable to verify",
        headers = {"WWW-Authenticate": "Bearer"}
    )