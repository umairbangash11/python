from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from database import Base, engine





class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    
Base.metadata.create_all(engine)
    


