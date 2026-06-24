from fastapi import FastAPI

app = FastAPI()

## Contact List
phone_book = {}
@app.post("/addNumber")
def user_con_info(name: str = None, phoneNumber: str = None):
    phone_book[name] = name
    phone_book[phoneNumber] = phoneNumber

    return{
        "Message" : "Phone Number Add Successfully"
    }

@app.get("/all_contact")
def show_all_contact():
    return phone_book

@app.put("/updateNumber")
def updateNumner(name:str= None, newNumber : str = None):
    if name in phone_book:
        phone_book[name] = newNumber
    
    else:
        return "User Not found"
    
    return{
        "Message" : "Number Successfully update"
    }

@app.delete("/deleteContact")
def deleteContact(name:str):
    if name in phone_book:
        del phone_book[name]
    else:
        return "User Not Found"
    
    return "Number Successfully Deleted"