from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Session(Base):

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    user = Column(String)
    service = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    data = Column(String)
    status = Column(String)
