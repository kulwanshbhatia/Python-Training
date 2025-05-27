#import module
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from random import randrange

#creating object
app=FastAPI()

#dummy data
user_data=[]

class User(BaseModel):
    uname:str
    email:str
    city:str

def searchUser(id):
    for index,data in enumerate(user_data):
        if data['id']== id:
            return data
        
@app.get('/loaduser/{id}')
def loadUser(id:int):
    post=searchUser(id)
    if post == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User with Given ID , NOT Found")
    return {'userdata': post}

@app.get('/loadusers')
def loadUsers():
    return {'data':user_data}

@app.post('/adduser')
def addUser(user:User):
    data=user.model_dump()  #model dump converts input data in key value pairs
    data['id']=randrange(0,10000)
    user_data.append(data)
    return {'message': data}