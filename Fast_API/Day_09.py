from fastapi import FastAPI,Depends
from sqlalchemy import create_engine,Column,INTEGER,String 
from sqlalchemy.orm import sessionmaker, declarative_base,Session

app = FastAPI()

DATABASE_URL = "sqlite:///./test_.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Test(Base):
    __tablename__ = "userdata"

    id = Column(INTEGER , primary_key=True, index=True)
    name = Column(String)
    address = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db:Session = Depends(get_db)):
    return{
        "Nessage" : "DB Connection is fine"
    }