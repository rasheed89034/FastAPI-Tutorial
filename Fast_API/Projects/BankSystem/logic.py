import re 
import sqlite3
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Form,HTTPException,status,Request
from pydantic import BaseModel,Field, field_validator, EmailStr, ValidationError
from main import app, connection, cursor

templates = Jinja2Templates(directory="Projects/BankSystem")

class SignUp(BaseModel):
    name : str
    age : int 
    address : str 
    account_type : str
    email : EmailStr
    password : str = Field(min_length=8,max_length=20)
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

class Login(BaseModel):
    email : str
    password : str

class Deposit(BaseModel):
    user_id : int
    amount : float

class Withdrawal(BaseModel):
    user_id : int
    amount : float

@app.get("/signup")
def signup_page(request: Request):
    return templates.TemplateResponse(request=request, name="signup.html")

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


## Paths (SignUP)
@app.post("/signup")
def create_user(
    request: Request,
    name : str = Form(...),
    age : int = Form(...),
    address : str = Form(...),
    account_type : str = Form(...),
    email : str = Form(...),
    password : str = Form(...)
):
    try:
        # pydantic Validtion 
        user_data = SignUp(
            name = name,
            age = age,
            address = address,
            account_type = account_type,
            email = email,
            password = password
        )

        cursor.execute("""
            INSERT INTO signup (name,age,address,account_type,email,password)
            VALUES(?,?,?,?,?,?)
        """,(
            user_data.name,
            user_data.age,
            user_data.address,
            user_data.account_type,
            user_data.email,
            user_data.password
        ))

        connection.commit()

        return templates.TemplateResponse(
            request=request, 
            name="login.html", 
            context={"message": f"Account for {name} created successfully! Please login."}
        )
    except Exception as e:
        return templates.TemplateResponse(
            request=request, 
            name="signup.html", 
            context={"error": str(e)}
        )

## Login 
@app.post("/login")
def login(
    request: Request,
    email : str = Form(...),
    password : str = Form(...)
):
    try:
        cursor.execute("SELECT id , name from signup WHERE email = ? AND password = ?",(email,password))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            cursor.execute("SELECT SUM(amount) FROM deposite WHERE user_id = ?", (user_id,))
            total_deposit = cursor.fetchone()[0] or 0
            cursor.execute("SELECT SUM(amount) FROM withdrawal WHERE user_id = ?", (user_id,))
            total_withdraw = cursor.fetchone()[0] or 0
            current_balance = total_deposit - total_withdraw
            return templates.TemplateResponse(
                request=request, 
                name="services.html", 
                context={
                    "user_id": user_id, 
                    "user_name": user[1],
                    "current_balance": current_balance 
                }
            )
        else:
            return templates.TemplateResponse(
                request=request, 
                name="login.html", 
                context={"request": request, "error": "Invalid Email or Password."}
            )
            
    except Exception as e:
        return templates.TemplateResponse(
            request=request, 
            name="login.html", 
            context={"request": request, "error": f"An error occurred: {str(e)}"}
        )


@app.post("/deposit")
def deposit_money(
    request : Request,
    user_id : int = Form(...),
    amount : float = Form(...)
):
    try:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        cursor.execute("INSERT INTO deposite(amount,user_id) VALUES (?,?)",(amount,user_id))
        connection.commit()

        cursor.execute("SELECT name FROM signup WHERE id = ?",(user_id,))
        user_name = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(amount) FROM deposite WHERE user_id = ?", (user_id,))
        total_deposit = cursor.fetchone()[0] or 0
        cursor.execute("SELECT SUM(amount) FROM withdrawal WHERE user_id = ?", (user_id,))
        total_withdraw = cursor.fetchone()[0] or 0
        current_balance = total_deposit - total_withdraw

        return templates.TemplateResponse(request=request,name="services.html",context={
            "user_id": user_id,
            "user_name": user_name,
            "current_balance": current_balance,
            "message": f"Successfully deposited Rs {amount}!"
        })
    except Exception as e:
        return templates.TemplateResponse(request=request, name="services.html", context={"error": str(e), "user_id": user_id})

@app.post("/withdraw")
def withdraw_amount(
    request : Request,
    user_id : int = Form(...),
    amount : float = Form(...)
):
    try:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        
        cursor.execute("SELECT SUM(amount) FROM deposite WHERE user_id = ?",(user_id,))
        total_deposit = cursor.fetchone()[0] or 0

        cursor.execute("SELECT SUM(amount) FROM withdrawal WHERE user_id = ?", (user_id,))
        total_withdraw = cursor.fetchone()[0] or 0

        current_balance = total_deposit - total_withdraw

        cursor.execute("SELECT name FROM signup WHERE id = ?", (user_id,))
        user_name = cursor.fetchone()[0]

        if amount > current_balance:
            return templates.TemplateResponse(request=request, name="services.html", context={
                "user_id": user_id, 
                "user_name": user_name,
                "current_balance": current_balance,
                "error": f"Insufficient Balance! Your current balance is Rs {current_balance}."
            })

        cursor.execute("INSERT INTO withdrawal (amount, user_id) VALUES (?, ?)", (amount, user_id))
        connection.commit()

        new_balance = current_balance - amount

        return templates.TemplateResponse(request=request, name="services.html", context={
            "user_id": user_id,
            "user_name": user_name,
            "current_balance" : new_balance,
            "message": f"Successfully withdrew Rs {amount}!"
        })
    except Exception as e:
        return templates.TemplateResponse(request=request, name="services.html", context={"error": str(e), "user_id": user_id})