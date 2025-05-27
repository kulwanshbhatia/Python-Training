#import module
from fastapi import FastAPI,status,HTTPException,APIRouter
from . import schema
from random import randrange

#creating object
router = APIRouter(tags=["User DML App"])

#dummy data
user_data=[]

#add user in array
@router.post('/adduser')
def addUser(user:schema.User):
    data=user.model_dump()  #model dump converts input data in key value pairs
    data['id']=randrange(0,10000) #generate random value
    user_data.append(data)
    return {'message': data}

#reusable function to perform (search,update and delete)
def searchUser(id):
    for index,data in enumerate(user_data):
        if data['id']== id:
            return index
        

# delete the user with id
@router.delete('/deleteuser/{id}')
def loadUser(id:int):
    post=searchUser(id)
    if post == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User with Given ID , NOT Found")
    user_data.pop(post)
    return {'user is deleted ': post}

#update the user (accept ID and data to update)
@router.put('/update user/{id}')
def updateUser(id:int,user:schema.User):
    indexId=searchUser(id)
    if indexId == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User with Given ID , NOT Found")
    data=user.model_dump()
    user['id']= id
    user_data[indexId]=data
    return {'user is updated ': data}