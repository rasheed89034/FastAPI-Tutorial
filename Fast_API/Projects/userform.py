from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator , EmailStr
import re

app = FastAPI()

class UserReg(BaseModel):
    name : str
    age : int
    address : str
    cgpa : float
    email : EmailStr

    password : str = Field(min_length = 8, max_length = 20)

    @field_validator('password')
    @classmethod

    def check_validation(cls,value:str):
        if not any(char.isupper() for char in value):
            raise ValueError("One letter must be in Capital")
        if not any(char.islower() for char in value):
            raise ValueError("One letter must be in Small")
        if not any(char.isdigit() for char in value):
            raise ValueError("(0-9) one number is must")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]",value):
            raise ValueError("One speical character is must")


@app.post("/User_Registration")
def userData(user:UserReg):
    return{
        "Message" : "Account created Successfully",
        "Name is " : user.name,
        "Age is ":user.age,
        "Address is ":user.address,
        "CGPA is ":user.cgpa,
        "Email is ":user.email,
        "Password ": "Strong and Valid"
    }
