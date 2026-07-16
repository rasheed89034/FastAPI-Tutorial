from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'title' : 'Title One', 'author':'Author One','book name':'Science'},
    {'title' : 'Title Two', 'author':'Author Two','book name':'Math'},
    {'title' : 'Title Three', 'author':'Author Three','book name':'English'}
]

@app.get("/book/{book_title}")
async def getABook(book_title):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/book/author/{author_name}")
async def getBook(author_name:str):
    for book_ in BOOKS:
        if book_.get('author').casefold() == author_name.casefold():
            return book_