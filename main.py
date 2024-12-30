from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.routers.gallery import router as gallery_router

app = FastAPI()

app.include_router(router=gallery_router, prefix="/gallery", tags=["Gallery"])

@app.get("/")
def home():
    return JSONResponse(content={"message": "Welcome to Celestia"}, status_code=200)
