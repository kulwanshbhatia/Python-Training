#import module
from fastapi import FastAPI,status,HTTPException,APIRouter
from . import schema

#creating object
router = APIRouter(tags=["User loading App"])

#dummy data
user_data=[]

#load the data from array
@router.get('/loadusers')
def loadUsers():
    return {'data':user_data}



#reusable function to perform (search,update and delete)
def searchUser(id):
    for index,data in enumerate(user_data):
        if data['id']== id:
            return index
        
#search the user with id
@router.get('/loaduser/{id}')
def loadUser(id:int):
    post=searchUser(id)
    if post == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User with Given ID , NOT Found")
    return {'userdata': post}

