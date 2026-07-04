from fastapi import FastAPI, Depends 
from sqlalchemy import create_engine,Column,INTEGER, String
from sqlalchemy.orm import Session, sessionmaker, declarative_base

app = FastAPI()

DATABASE_URL = "sqlite:///./p.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

class Testing(Base):
    __tablename__ = "userTesting"

    id = Column(INTEGER,primary_key=True,index=True)
    name = Column(String)

Base.metadata.create_all(bind = engine)

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        bd.close()

@app.get("/")
def check(db:Session = Depends(get_db)):
    return{
        "Message" : "Connection is Fine"
    }