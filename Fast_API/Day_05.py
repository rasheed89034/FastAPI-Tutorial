## Pydantic Model(classes)

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, EmailStr
import re

app = FastAPI()

class AlterForm(BaseModel):
    camera_id : int
    anonmaly_type : str
    location : str
    is_active : bool = True

@app.post("/submitData")
def cameraData(data:AlterForm):
    dangerList = ["fire","smoke","fight"]
    if data.anonmaly_type.lower() in dangerList:
        status =  "Emergancy"
    else:
       status = "Normal"

    return {
        "Status" :status,
        "Received Data ID" : data.camera_id,
        "Location" : data.location
    }


## Strong Password

class UserRegistation(BaseModel):
    email : EmailStr
    password : str = Field(min_length = 8, max_length = 20)

    @field_validator("password")
    @classmethod
    def check_striong_password(cls,value:str):
        if not any(char.isupper() for char in value):
            return "One Letter must be in Capital"
        if not any(char.islower() for char in value):
            return "One Letter must be in small"
        
        if not any(char.isdigit() for char in value):
            return "(0-9) one number should be there"
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]",value):
            return "One special character should be there"
        
        return value

@app.post("/enterPassword")
def userRegistation(data : UserRegistation):
    return{
        "Message" : "Account Create Successfullly",
        "Email" : data.email,
        "Password" : "Strong and Valid"
    }