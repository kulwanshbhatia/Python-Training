#import module
from fastapi import FastAPI,status,HTTPException,APIRouter,Depends
from . import schema
from . import models
from random import randrange
from sqlalchemy.orm import Session
from .database import engine,get_connection

#creating object
router = APIRouter(tags=["User DML App"])

#dummy data
user_data=[]

#add user in array
@router.post('/adduser')
def addUser(user:schema.User,db:Session=Depends(get_connection)):
    #data=user.model_dump()  #model dump converts input data in key value pairs
    postdata= models.UserApp(**user.model_dump())
    db.add(postdata)
    db.commit()


   # data['id']=randrange(0,10000) #generate random value
    #user_data.append(data)
    return {'message': postdata}

#reusable function to perform (search,update and delete)
def searchUser(id):
    for index,data in enumerate(user_data):
        if data['id']== id:
            return index
        

# delete the user with id
@router.delete('/deleteuser/{name}')
def loadUser(name,db:Session=Depends(get_connection)):
    post=db.query(models.UserApp).filter(models.UserApp.uname == name).first()
    if post == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User with Given ID , NOT Found")
    #post.delete(synchronize_session=False)
    db.delete(post)
    db.commit()
    return {'user is deleted ': post}

#update the user (accept ID and data to update)
@router.put('/update user/{name}')
def updateUser(name,db:Session=Depends(get_connection)):
    post=db.query(models.UserApp).filter(models.UserApp.uname == name).first()
    if post == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User with Given ID , NOT Found")
    #db.update(synchronize_session=False)
    db._update_impl(post)
    db.commit()
    return {'user is updated ': post}