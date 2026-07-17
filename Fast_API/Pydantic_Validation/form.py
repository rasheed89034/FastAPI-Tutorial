from fastapi import FastAPI,Form
from pydantic import BaseModel,ValidationError,Field,field_validator,EmailStr
import re

app = FastAPI()

dataBase = {}

class Data(BaseModel):
    name : str
    email : EmailStr
    password : str = Field(min_length=8,max_length=20)

    @field_validator("password")
    @classmethod

    def passwordValidation(cls,value:str):
        if not any(char.isupper() for char in value):
            raise ValueError("A Letter Must be in Capital Case")
        if not any(char.islower() for char in value):
            raise ValueError("A Letter Must be in Small Case")
        if not any(char.isdigit() for char in value):
            raise ValueError("0-9 one digit is required")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]",value):
            raise ValueError("At-least one special Character")
        
        return value

@app.post("/dataForm")
def form_data(
    name : str = Form(...),
    email : str = Form(...),
    password : str = Form(...)
):
    try:
        user = Data(
            name = name,
            email = email,
            password = password
        )
        if user.email in dataBase:
            return user.email,"Already Exist"

        dataBase[user.email] = {
            "name" : name,
            "email" : email,
            "password" : password
        }

        return{
            "Message" : "Data Successfully Save",
            "Name" : user.name,
            "Email" : user.email,
            "Password" : "Valid & Strong"
        }
    except ValidationError as e:
        return{
            "Error": "Validation Failed", 
            "Details": e.errors()
        }

@app.get("/searchUser")
def searchUser(
    email : str,
    password : str
):
    if email in dataBase:
        stored_password = dataBase[email]['password']

        if password == stored_password:
            user_name = dataBase[email]['name']
            return{
                "Status" : "User Found",
                "Name" : user_name
            }
        else:
            return{
                "Status" : "User Not Found"
            }
    else:
        return{
            "Message" : "Invalid Email"
        }


