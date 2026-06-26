from fastapi import FastAPI,Form
import re
from pydantic import BaseModel, Field, field_validator, EmailStr,ValidationError

app = FastAPI()

userCompleteData = {}

class UserDataForm(BaseModel):
    name : str
    age : int 
    address : str
    cgpa : float
    email : EmailStr

    password : str = Field(min_length = 8) 

    @field_validator("password")
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
        
        return value

@app.post("/User_Registration")
def userData(
    name : str = Form(...),
    age : int = Form(...),
    address : str = Form(...),
    cgpa : float = Form(...),
    email : str = Form(...),
    password : str = Form(...)
):
    try:
        user = UserDataForm(
            name = name,
            age = age,
            address = address,
            cgpa = cgpa,
            email = email,
            password = password
        )
        if user.email in userCompleteData:
            return user.email,"Already regist"

        userCompleteData[user.email] = {
            "name":name,
            "age":age,
            "address" : address,
            "cgpa": cgpa,
            "email": email,
            "password": password
        }
        return{
            "Message" : "Account created Successfully",
            "Name is " : user.name,
            "Age is ":user.age,
            "Address is ":user.address,
            "CGPA is ":user.cgpa,
            "Email is ":user.email,
            "Password ": "Strong and Valid"
        }
    except ValidationError as e:
        return{
            "Error": "Validation Failed", 
            "Details": e.errors()
        }


@app.get("/find_user")
def find_user(
    email:str,
    password:str
):
    if email in userCompleteData:
        stored_password = userCompleteData[email]["password"]

        if password == stored_password:
            user_name = userCompleteData[email]["name"]
            return{
                "Status" : "Success",
                "Welcome" : user_name
            }
        else:
            return{
                "Message": "Inccorect Password"
            }
    else:
        return{
            "Message":"Invalid Email"
        }

