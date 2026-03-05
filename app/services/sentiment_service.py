import torch
from app.models.model_loader import get_model

EMOTIONS = [
    "joy",
    "sadness",
    "anger",
    "fear",
    "surprise",
    "neutral"
]

model, tokenizer = get_model()

def predict_sentiment(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs),

    probs = torch.sigmoid(outputs.logits)
    preds = (probs>0.5).int()[0]

    return {
        EMOTIONS[i]: float(probs[0][i])
        for i in range(len(EMOTIONS))
        if preds[i]==1
    }
