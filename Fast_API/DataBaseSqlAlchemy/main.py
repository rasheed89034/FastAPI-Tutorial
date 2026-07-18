from fastapi import FastAPI,Depends,HTTPException,Path
from database import engine,SessionLocal
import models
from pydantic import BaseModel,Field
from models import Todos
from typing import Annotated 
from sqlalchemy.orm import Session
from starlette import status

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

de_dependencies = Annotated[Session,Depends(get_db)]

class TodoRequest(BaseModel):
    name : str = Field(max_length=40)
    address : str 
    cgpa : float = Field(gt=0,lt=4.0)
    isactive : bool


@app.post("/createUser",status_code=status.HTTP_201_CREATED)
def userData(db:de_dependencies,todo_request:TodoRequest):
    todo_user = Todos(**todo_request.dict())

    db.add(todo_user)
    db.commit()





