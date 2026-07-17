from fastapi import FastAPI,Body
app = FastAPI()

data = []
@app.get("/alluser")
async def allUserData():
    return data

@app.post("/user/create_user")
async def create_new_user(new_user = Body()):
    data.append(new_user)

@app.put("/update/updateuserData")
async def update_user_data(updated_data = Body()):
    for i in range(len(data)):
        if data[i].get('name').casefold() == updated_data.get('name').casefold():
            data[i] = updated_data
            return {
                "Message" : "Data Updated Successfully"
            }
    return {
            "Message" : "User Not Found"
        }

@app.delete("/delete/deleteData")
async def delete_user_data(name:str):
    for i in range(len(data)):
        if data[i].get('name').casefold() == name.casefold():
            data.pop(i)
            break
            return "Data delete Successfully"


