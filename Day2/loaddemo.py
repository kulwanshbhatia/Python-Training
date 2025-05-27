#import module
from fastapi import FastAPI,status,HTTPException,APIRouter,Depends
from . import schema
from . import models
from random import randrange
from sqlalchemy.orm import Session
from .database import engine,get_connection

#creating object
router = APIRouter(tags=["User loading App"])

#dummy data
user_data=[]

#load the data from array
@router.get('/loadusers')
def loadUsers(db:Session=Depends(get_connection)):
    data=db.query(models.UserApp).all()
    return {'data':data}

        
#search the user with id
@router.get('/loaduser/{name}')
def loadUser(name,db:Session=Depends(get_connection)):
    post=db.query(models.UserApp).filter(models.UserApp.uname == name).first()
    if post == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User with Given ID , NOT Found")
    return {'userdata': post}

