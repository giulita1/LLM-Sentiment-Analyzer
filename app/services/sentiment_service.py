import requests
import os

EMOTIONS = ["joy", "sadness", "anger", "fear", "surprise", "neutral"]

MODEL_ID = "giulidimasi/Emotions"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

HF_TOKEN = os.getenv("HF_TOKEN")

def predict_sentiment(text: str):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": text}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            formatted_result = {}
            for prediction in result[0]:
                label = prediction['label']
                score = prediction['score']
                if score > 0.5:
                    formatted_result[label] = float(score)
            
            return formatted_result if formatted_result else {"neutral": 1.0}
            
        else:
            return {"error": f"API Error: {response.status_code}", "details": response.text}

    except Exception as e:
        return {"error": "Connection Failed", "details": str(e)}