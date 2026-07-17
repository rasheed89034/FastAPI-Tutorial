from database import Base 
from sqlalchemy import Column,Integer,String,Boolean,Float

class Todos(Base):
    __tablename__ = "userdata"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    address = Column(String)
    cgpa = Column(Float)
    isactive = Column(Boolean,default=False)