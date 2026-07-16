from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def getData():
    return {
        "Message" : "Hello Welcome To FastAPI Course"
    }

BOOKS = [
    {'title' : 'Title One', 'author':'Author One','book name':'Science'},
    {'title' : 'Title Two', 'author':'Author Two','book name':'Math'},
    {'title' : 'Title Three', 'author':'Author Three','book name':'English'}
]

@app.get("/getBooks")
def getAllBooks():
    return BOOKS