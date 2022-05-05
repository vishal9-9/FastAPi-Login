from fastapi import APIRouter,Depends
from schemas import create_users,show_users
from passhash import Hasher
from models import Users
from database import get_db
from sqlalchemy.orm import Session
from oauth2 import get_current_user

router = APIRouter(
    tags = ["User"] 
)

@router.post('/users')
def create_user(response: create_users, db: Session = Depends(get_db),current_user: show_users = Depends(get_current_user)):
    hashed_pass = Hasher.get_password_hash(response.passwd)
    user = Users(name = response.name , passwd = hashed_pass, email = response.email)
    db.add(user)
    db.commit()
    db.close()
    return "User Created"

@router.get('/users/{id}',response_model = show_users)
def show_user_withid(id: int,db: Session = Depends(get_db),current_user: show_users = Depends(get_current_user)):
    user = db.query(Users).filter(Users.id == id).first()
    return user
