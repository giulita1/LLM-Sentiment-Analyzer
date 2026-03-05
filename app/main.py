from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.services.sentiment_service import predict_sentiment
from app.schemas.request_schema import TextRequest

app = FastAPI()

@app.get('/')
async def serve_frontend():
    return FileResponse('static/index.html')

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

@app.post('/coment')
async def coment(request: TextRequest):
    
    result =  predict_sentiment(request.text)

    return { "predictions": result }