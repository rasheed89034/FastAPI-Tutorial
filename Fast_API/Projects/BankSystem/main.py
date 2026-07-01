import sqlite3
from fastapi import FastAPI
app = FastAPI()

connection = sqlite3.connect("BankMangementSystem.db",check_same_thread=False)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS signup(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age TEXT,
        address TEXT,
        account_type TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS deposite(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount INTEGER,
        user_id INTEGER,
        date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES signup(id)
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS withdrawal(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount INTEGER,
        user_id INTEGER,
        date_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES signup(id)
    )
""")
connection.commit()

import logic