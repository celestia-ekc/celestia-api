from pydantic import BaseModel
from datetime import time, date

class EventResponse(BaseModel):
    id: int
    image: str
    title: str
    insta_url: str
    event_time: time
    event_date: date

    class Config:
        from_attributes = True  

