from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine,INTEGER,Column,String,Float
from sqlalchemy.orm import sessionmaker,Session,declarative_base

app = FastAPI()

DATABASE_URL = "sqlite:///./crud.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Testing(Base):
    __tablename__ = "UserData"

    id = Column(INTEGER,primary_key=True,index=True)
    name = Column(String)
    cgpa = Column(Float)

Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

## Create API (User Data Input)
@app.post("/")
def create_user(name:str,cgpa:float,db:Session = Depends(get_db)):
    user = Testing(name = name,cgpa = cgpa)
    db.add(user)
    db.commit()
    db.refresh(user)
    return{
        "Message" : "Data Save in DataBase",
        "User_details" : user
    }

## Get all user data.
@app.get("/getData")
def getData(db:Session = Depends(get_db)):
    userData = db.query(Testing).all()

    return{
        "Total" : len(userData),
        "Data" : userData
    }

## Get specific user 
@app.get("/specificUser/{user_id}")
def specificUser(user_id = int, db:Session = Depends(get_db)):
    user = db.query(Testing).filter(Testing.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")

    return user

## Update Data 
@app.put("/update/{user_id}")
def updateUserData(user_id : int,cgpa : float, db:Session = Depends(get_db)):
    update = db.query(Testing).filter(Testing.id == user_id).first()


    if not update:
        raise HTTPException(status_code=404,detail="User Not Found")

    update.cgpa = cgpa

    db.commit()
    db.refresh(update)

    return{
        "Message" : "Data Updata",
        "Data" : update
    }


## Delete 
@app.delete("/delete/{user_id}")
def delete(user_id:int,db:Session = Depends(get_db)):
    deleteUser = db.query(Testing).filter(Testing.id == user_id).first()

    if not deleteUser:
        raise HTTPException(status_code=404,detail="User Not Found")

    db.delete(deleteUser)
    db.commit()

    return{
        "Message" : "Data Delete"
    }
    


