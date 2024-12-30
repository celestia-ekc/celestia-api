from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from api.schemas.gallery import GalleryResponse
from db.database import get_db
from db.models import Gallery

router = APIRouter()

@router.get("/")
async def get_gallery(db: Session = Depends(get_db)):
    try:
        galleries = db.query(Gallery).all()
        response = [GalleryResponse.from_orm(gallery) for gallery in galleries] 
        return response
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
