# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class Book(Base):
    __tablename__ = "STUDENTS"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    course = Column(String, index=True)