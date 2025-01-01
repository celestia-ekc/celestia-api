from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.database import get_db
from db.models import Events
from api.schemas.event import EventResponse
from datetime import date


router = APIRouter()

@router.get("/")
async def events(q: str = Query(None, description="Filter by event type: recentevent or upcomingevent"),db: Session = Depends(get_db)):
    today = date.today()
    try:
        if q == "recentevent":
            events = db.query(Events).filter(Events.event_date < today).all()
        elif q == "upcomingevent":
              events = db.query(Events).filter(Events.event_date >= today).all() 
        else:
             events= db.query(Events).all()
        response = [ EventResponse.from_orm(event) for event in events  ]
        return response
    except Exception as  e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
          

