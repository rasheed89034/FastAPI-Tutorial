## Dynamic Routes 
## Data Types
## Validation 
## uv add python-multipart (use for to received data from HTML Form)

from fastapi import FastAPI , Form

app = FastAPI()

@app.post("/submit_form")
def handel_data_form(user_id:int = Form(...), user_name : str = Form(...)):
    return{
        "Message" : "Data Successfully Received From HTMLFrom!",
        "ID is = " : user_id,
        "Name is = ": user_name
    }
