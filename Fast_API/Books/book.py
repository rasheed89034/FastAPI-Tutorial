from fastapi import FastAPI

app = FastAPI()

class Book():
    id : int
    name : str
    description : str 
    author : str
    rating : float

    def __init__(self,id,name,description,author,rating):
        self.id = id
        self.name = name
        self.description = description
        self.author = author
        self.rating = rating


BOOKS = [
    Book(1,"Python","A Nice Book","Ali khan",5),
    Book(2,"Java","Easy to learn","Jawad khan",5),
    Book(3,"Networking","Expalin about Networking","Jamal khan",5),
    Book(4,"DataBase","A Nice Book","Ahmad Ali",5),
]

@app.get("/allBooks")
def getAllBoooks():
    return BOOKS
