import sqlite3 
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

connection = sqlite3.connect("test.db",check_same_thread=False)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        address TEXT
    )

""")

connection.commit()

class UserTable(BaseModel):
    id : int
    name : str
    age : int
    address : str



@app.post("/user_table")
def user_table(user : UserTable):
    cursor.execute(
        "INSERT INTO user(name,age,address) VALUES (?,?,?)",
        (user.name,user.age,user.address)
    )
    connection.commit()

    return{
        "Message" : "Data Save is DataBase",
        "Name" : user.name,
        "Age" : user.age,
        "Address" : user.address
    }

@app.get("/user/{user_id}")
def home(user_id:int):
    cursor.execute(
        "SELECT id, name, age, address FROM user WHERE id = ? ",
        (user_id,)
    )
    user_data = cursor.fetchone()
    if user_data:
        return{
            "Message" : "User Found",
            "ID" : user_data[0],
            "Name" : user_data[1],
            "Age" : user_data[2],
            "Address" : user_data[3]
        }
    return "User Not Found"
        
    