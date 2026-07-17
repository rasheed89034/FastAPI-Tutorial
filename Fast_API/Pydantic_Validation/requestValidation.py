from fastapi import FastAPI,Body
from pydantic import BaseModel

app = FastAPI()

class Books():
    id : int 
    title : str 
    description : str
    author : str
    rating : float

    def __init__(self,id,title,description,author,rating):
        self.id = id 
        self.title = title 
        self.description = description
        self.author = author
        self.rating = rating

BOOKS = [
    Books(1,"Python","A Nice Book","Ali khan",5),
    Books(2,"Java","Easy to learn","Jawad khan",5),
    Books(3,"Networking","Expalin about Networking","Jamal khan",5),
    Books(4,"DataBase","A Nice Book","Ahmad Ali",5),
]

class BookModel(BaseModel):
    id : int 
    title : str 
    description : str
    author : str
    rating : float



@app.get("/allBooks")
def getAllBoooks():
    return BOOKS


## Here is no such proper validation we can assign id and rating even negative
@app.post("/addABook")
def addABook(new_book = Body()):
    BOOKS.append(new_book)
    return "Book Add Successfully"

@app.post("/addNewBook")
def addNewBook(new_book:BookModel):
    new_book = BookModel(**new_book.dict())
    BOOKS.append(new_book)