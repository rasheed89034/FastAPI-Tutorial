from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel,EmailStr,Field,field_validator,ValidationError
import re

app = FastAPI()
userDataDict = {}



class UserCredentials(BaseModel):
    id : str
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

class StudentDetails(UserCredentials):
    name : str
    address : str 

@app.post("/userData")
def userData(
    user : StudentDetails
):
    if user.email in userDataDict:
        return user.email,"Already registor"
    userDataDict[user.email] = {
        "Id is ": user.id,
        "Name is " : user.name,
        "Address is ": user.address,
        "Email is ": user.email,
        "Password is ": user.password,
    }

    return{
        "Name is " : user.name,
        "Email is ": user.email,
        "Password is ": "Valid & Strong"
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

@app.get("/getAllData")
def getAllData():
    return userDataDict

@app.put("/updateUserData")
def updateUserData(
    user : UserCredentials
):
    if user.email in userDataDict:
        if userDataDict[user.email]["Id is "] == user.id:
            userDataDict[user.email]["Password is "] = user.password

            return{
                "Message" : "Password updated successfully",
                "Email is ": user.email
            }
        else:
            return {"Error": "Incorrect ID for this email"}
    else:
        return {"Error": "User not found"}

@app.delete("/delete")
def deleteUserData(id:str):
    for email, user_data in userDataDict.items():
        if user_data["Id is "] == id:
            del userDataDict[email]
        return {"Message": f"User with ID {id} deleted successfully"}
        
    return {"Error": "User ID not found"}

        






