from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.routers.gallery import router as gallery_router
from api.routers.events import router as event_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  
    "https://celestia-cse.vercel.app" 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)
app.include_router(router=gallery_router, prefix="/gallery", tags=["Gallery"])

app.include_router(router=event_router,prefix="/events",tags=["Events"])

@app.get("/")
def home():
    return JSONResponse(content={"message": "Welcome to Celestia"}, status_code=200)
