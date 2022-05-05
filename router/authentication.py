from fastapi import APIRouter,Depends,HTTPException
from database import get_db
from models import Users
from passhash import Hasher
from sqlalchemy.orm import Session
from tokens import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags = ["Authentication"]
)

@router.post('/login')
def login(form: OAuth2PasswordRequestForm = Depends() ,db : Session = Depends(get_db)):
    uname = db.query(Users).filter(Users.email == form.username).first()
    if not uname:
        raise HTTPException(status_code = 404, detail = "Invalid Credentials") 
    res = Hasher.verify_password(form.password, uname.passwd)
    if res == False:
        raise HTTPException(status_code = 404, detail = "Invalid Credentials")    
    access_token = create_access_token(data={"sub": uname.email})
    return access_token