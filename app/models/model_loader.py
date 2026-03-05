from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "model/goemotions_model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

def get_model():
    return model, tokenizer