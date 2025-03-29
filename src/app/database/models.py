from sqlalchemy import  Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Contact(Base):
  __tablename__ = "contacts"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False)
  phone = Column(String, nullable=False)
  birthdate = Column(DateTime, default=datetime.date)
  notes = Column(String)
  