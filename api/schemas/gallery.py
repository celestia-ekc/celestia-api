from pydantic import BaseModel
from datetime import datetime, date

class GalleryBase(BaseModel):
    image: str
    date_of_image: date

class GalleryResponse(GalleryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  