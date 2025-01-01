from sqlalchemy import Column, Integer, String,Date,DateTime,Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Gallery(Base):
    __tablename__ = "Gallery"

    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String, nullable=False)
    date_of_image=Column(Date,nullable=False)
    created_at=Column(DateTime,nullable=False)

class Events(Base):
    __tablename__ = "Events"

    id = Column(Integer,primary_key=True,autoincrement=True)
    image = Column(String, nullable=False)
    title = Column(String, nullable=False)
    insta_url = Column(String, nullable=True)
    event_date = Column(Date, nullable=False)
    event_time = Column(Time, nullable=True)
    created_at = Column(DateTime, nullable=False)