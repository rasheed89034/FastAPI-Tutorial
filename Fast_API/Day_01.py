from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "Welcome To FastAPI Course"
    }

# Methond_01 by using Dictnory of List. 
# @app.get("/users")
# def users():
#     return{
#         "Students":[
#             {
#                 "Name" : "Rasheed Ahmad",
#                 "Age" : 21,
#                 "CGPA" : 3.59,
#                 "Current Semeter" : "4th"
#             },
#             {
#                 "Name" : "Muhammad Bilal",
#                 "Age" : 21,
#                 "CGPA" : 3.33,
#                 "Current Semeter" : "4th"
#             },
#             {
#                 "Name" : "Muazzam Ali",
#                 "Age" : 21,
#                 "CGPA" : 3.00,
#                 "Current Semeter" : "4th"
#             }
#         ]
#     }

# Method_02 by using List of Dictionary.

@app.get("/users")
def usersData():
    return[
        {
            "Name" : "Rasheed Ahmad",
            "Age" : 21,
            "CGPA" : 3.59,
            "Current Semeter" : "4th"
        },
        {
            "Name" : "Muhammad Bilal",
            "Age" : 21,
            "CGPA" : 3.33,
            "Current Semeter" : "4th"
        }
    ]
