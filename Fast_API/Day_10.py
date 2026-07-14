from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel,EmailStr,Field,field_validator,ValidationError
import re

app = FastAPI()
userDataDict = {}

class StudentDetails(BaseModel):
    id : str
    name : str
    address : str 
    email : EmailStr
    password : str = Field(min_length=8,max_length=20)

    @field_validator("password")
    @classmethod

    def checkValidation(cls,value:str):
        if not any(char.isupper() for char in value):
            raise ValueError("One letter must be in capital")
        if not any(char.islower() for char in value):
            raise ValueError("One letter must be in small")
        if not any(char.isdigit() for char in value):
            raise ValueError("(0-9) number is must")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]",value):
            raise ValueError("One special character is must")

        return value


@app.post("/userData")
def userData(
    id:str,
    name:str,
    address : str,
    email : str,
    password : str

):
    try:
        user = StudentDetails(
            id = id,
            name = name,
            address = address,
            email = email,
            password = password
        )
        if user.email in userDataDict:
            return user.email,"Already registor"
        userDataDict[user.email] = {
            "Id is ": id,
            "Name is " : name,
            "Address is ": address,
            "Email is ": email,
            "Password is ": password,
        }

        return{
            "Name is " : name,
            "Email is ": email,
            "Password is ": "Valid & String"
        }

    except ValidationError as e:
        return{
            "Error": "Validation Failed", 
            "Details": e.errors()
        }


@app.get("/userData")
def getUserData(
    email : str,
    password : str
):
    if email in userDataDict:
        stored_password = userDataDict[email]["Password is "]

        if password == stored_password:
            user_name = userDataDict[email]["Name is "]
            user_address = userDataDict[email]["Address is "]
            user_email = userDataDict[email]["Email is "]
            return{
                "Message" : "User Found",
                "Name is ": user_name,
                "Address is ": user_address,
                "Email is ": user_email
            }
        else:
            return{
                "Message": "Inccorect Password"
            }
    else:
        return{
            "Message":"Invalid Email"
        }
        






