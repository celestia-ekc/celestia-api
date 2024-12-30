from sqlalchemy import Column, Integer, String,Date,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Gallery(Base):
    __tablename__ = "Gallery"

    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String, nullable=False)
    date_of_image=Column(Date,nullable=False)
    created_at=Column(DateTime,nullable=False)
