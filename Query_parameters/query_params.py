from fastapi import FastAPI
app = FastAPI()

userData = [
    {'Name': 'Ahmad','age':21,'cgpa':3.69},
    {'Name': 'Jamal','age':21,'cgpa':3.39},
    {'Name': 'Hamza','age':21,'cgpa':3.69},
]

@app.get("/user")
async def getuserData(cgpa:float):
    users = []
    for user in userData:
        if user.get('cgpa') == cgpa:
            users.append(user)
    return users

@app.get("/user/{name}")
async def read_name_by_cgpa(name:str,cgpa:float):
    user = []
    for person in userData:
        if person.get('Name').casefold() == name.casefold() and person.get('cgpa') == cgpa:
            user.append(person)
    return user