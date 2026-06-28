## CURD

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
dataList = []

class DataStore(BaseModel):
    name : str
    age : int 

@app.post("/user")
def userData(
    user : DataStore
):
    dataList.append(user)
    return{
        "Message" : "Data Save in list",
        "Data" : user
    }

@app.get("/user")
def allData():
    return dataList

@app.get("/user/{name}")
def specificUser(name : str):
    for item in dataList:
        if item.name == name:
            return name
        return{
            "error" : "User Not Found"
        }

@app.put("/user/{name}")
def updateData(name : str,new_name:DataStore):
    for index , item in enumerate(dataList):
        if item.name == name:
            dataList[index] = new_name
            return{
                "Message": "update name"
            }
        else:
            return{
                "error" : "User Not Found"
            }

