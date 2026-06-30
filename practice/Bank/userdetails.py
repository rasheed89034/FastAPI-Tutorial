from fastapi import FastAPI
from pydantic import BaseModel, Field , field_validator, EmailStr , ValidationError
import re
import sqlite3

app = FastAPI()

connection = sqlite3.connect("login.db",check_same_thread=False)

cursor = connection.cursor()

class SignUp(BaseModel):
    name : str
    age : int 
    address : str
    email : EmailStr
    password : str = Field(min_length =8, max_length = 20)

    @field_validator("password")
    @classmethod

    def check_validation(cls,value:str):
        if not any(char.isupper() for char in value):
            raise ValueError ("One Letter must be in capital")
        if not any(char.islower() for char in value):
            raise ValueError("One letter must be in small")
        if not any(char.isdigit() for char in value):
            raise ValueError("0-9 one number is required")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]",value):
            raise ValueError("Special Character is Required")

        return value


cursor.execute("""
    CREATE TABLE IF NOT EXISTS signup(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        address TEXT,
        email TEXT,
        password TEXT
    )
""")

connection.commit()

@app.post("/signup")
def signup(signup:SignUp):
    cursor.execute(
        "INSERT INTO signup(name,age,address,email,password) VALUES(?,?,?,?,?)",
        (signup.name,signup.age,signup.address,signup.email,signup.password)
    )
    connection.commit()

    return{
        "Message" : "Data Save in DataBase",
        "Name" : signup.name,
        "Email" : signup.email,
        "Password" : "Valid and Strong Password"
    }
