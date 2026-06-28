## Nested Class Concept Pydantic
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city : str
    postal_code : int

class User(BaseModel):
    name : str
    age : int
    address : Address

@app.post("/create_user")
def user(user:User):
    return user
    
