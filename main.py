from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return JSONResponse(content={"message":"Welcome to celestia"},status_code=200,media_type="application/json")