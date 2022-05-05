from fastapi import APIRouter,Depends,HTTPException
from typing import List
from sqlalchemy.orm import Session
from schemas import show_blogs,get_blogs_withid,show_users
from database import get_db
from models import Blogs
from oauth2 import get_current_user

router = APIRouter(
    tags = ['Blogs']
)

@router.get('/blogs/show',response_model = List[show_blogs])
def show_all_blogs(db:Session = Depends(get_db),current_user: show_users = Depends(get_current_user)):
    show_blogs_all = db.query(Blogs).all()
    return show_blogs_all

@router.get('/blogs/{id}',response_model = show_blogs,)
def show_blog_withid(id : int, db: Session = Depends(get_db),current_user: show_users = Depends(get_current_user)):
    blog1 = db.query(Blogs).filter(Blogs.id == id).first()
    if not blog1:
        return HTTPException(status_code = 404 , detail = "No Blog With That Id")
    return blog1

@router.post('/blogs',response_model = show_blogs)
def create_blog(response: show_blogs,db:Session = Depends(get_db),current_user: show_users = Depends(get_current_user)):
    create_blog = Blogs(title = response.title , body = response.body, user_id = 1)
    db.add(create_blog)
    db.commit()
    db.close()
    return create_blog

@router.put('/blogs')
def update_blogs(request: get_blogs_withid, title : str, db: Session = Depends(get_db),current_user: show_users = Depends(get_current_user)):
    blog_id = db.query(Blogs).filter(Blogs.id == request.id).first()
    blog_id.title = title
    db.commit()
    db.close()
    return "Title Updated"

@router.delete('/Blogs')
def delete_blogs(response: get_blogs_withid,db : Session = Depends(get_db),current_user: show_users = Depends(get_current_user)):
    delete = db.query(Blogs).filter(Blogs.id == response.id).first()
    if not delete:
        return HTTPException(status_code = 404 , detail = "No Blog With That Id")
    db.delete(delete)
    db.commit()
    db.close()
    return "Blog Deleted"