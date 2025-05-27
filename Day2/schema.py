from pydantic import BaseModel
#Schema created
class User(BaseModel):
    uname:str
    email:str
    city:str