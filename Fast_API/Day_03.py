## Optional Parameters. 
## Default Vales. 
## Multiple query parameters.

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# ## Optional. 
# @app.get("/user")
# def getUser(name: str = None):
#     return{
#         "User name is = " : name
#     }
    
# ## Default & Multiple Paramters.
# @app.get("/userData")
# def getAllData(name: str = "Ali", age: int = 20):
#     return{
#         "Name is ": name,
#         "Age is ": age
#     }

# ## Update a user number
# @app.put("/updateNumber")
# def updateNum(name:str = None, number: str = None):
#     return{
#         "Name": name,
#         "Phone Number Update" : number
#     }

