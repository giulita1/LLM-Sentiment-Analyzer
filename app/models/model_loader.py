from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import torch

MODEL_NAME = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME,
                                                           NUM_LABELS,
                                                           problem_type="multi_label_classification" #cambia la loss 
                                                           )

model.eval()

def get_model():
    return model, tokenizer