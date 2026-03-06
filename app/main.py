from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.services.sentiment_service import predict_sentiment
from app.schemas.request_schema import TextRequest
import os

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)


@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
   
@app.post('/coment')
async def coment(request: TextRequest):
    
    result =  predict_sentiment(request.text)

    return { "predictions": result }