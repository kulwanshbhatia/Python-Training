#import module
from fastapi import FastAPI
from pydantic import BaseModel

#creating object
app=FastAPI()

#dummy data
user_data=[]

class User(BaseModel):
    uname:str
    email:str
    city:str

@app.get('/loadusers')
def loadUsers():
    return {'data':user_data}

@app.post('/adduser')
def addUser(user:User):
    data=user.model_dump()  #model dump converts input data in key value pairs
    print(data)