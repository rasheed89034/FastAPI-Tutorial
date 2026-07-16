from fastapi import FastAPI,Body
app = FastAPI()

data = []
@app.get("/alluser")
async def allUserData():
    return data

@app.post("/user/create_user")
async def create_new_user(new_user = Body()):
    data.append(new_user)
