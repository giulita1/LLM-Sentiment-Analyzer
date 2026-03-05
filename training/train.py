from datasets import load_dataset
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
    TrainingArguments,Trainer)

import evaluate
import torch

MODEL_NAME = "distilbert-base-uncased"

EMOTIONS = [
    "joy",
    "sadness",
    "anger",
    "fear",
    "surprise",
    "neutral"
]

NUM_LABELS = len(EMOTIONS)

#dataset

dataset = load_dataset("go_emotions")

label_names = dataset["train"].features["labels"].feature.names

selected_indices = [label_names.index(e) for e in EMOTIONS]


def filter_example(example):

    for label in example["labels"]:

        if label in selected_indices:
            return True

    return False


dataset = dataset.filter(filter_example)

#multi-hot

def filter_and_binarize(batch):

    new_labels = []

    for labels in batch["labels"]:

        multi_hot = [0] * NUM_LABELS

        for label_id in labels:

            if label_id in selected_indices:

                position = selected_indices.index(label_id)
                multi_hot[position] = 1

        new_labels.append(multi_hot)

    batch["labels"] = new_labels
    return batch


dataset = dataset.map(filter_and_binarize, batched=True)

# tokenizer

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def tokenize(batch):

    return tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )


dataset = dataset.map(tokenize, batched=True)

# format pytorch

dataset.set_format(
    type="torch",
    columns=["input_ids", "attention_mask", "labels"]
)

#model
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=NUM_LABELS,
    problem_type="multi_label_classification"
)

# metric

f1_metric = evaluate.load("f1")

def compute_metrics(eval_pred):

    logits, labels = eval_pred

    probs = torch.sigmoid(torch.tensor(logits))
    preds = (probs > 0.5).int()

    return {
        "f1_micro": f1_metric.compute(
            predictions=preds,
            references=labels,
            average="micro"
        )["f1"]
    }


#training args

training_args = TrainingArguments(

    output_dir="./models/checkpoints",

    evaluation_strategy="epoch",
    save_strategy="epoch",

    logging_dir="./logs",

    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,

    num_train_epochs=3,

    load_best_model_at_end=True
)

#trainer

trainer = Trainer(

    model=model,
    args=training_args,

    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],

    tokenizer=tokenizer,

    compute_metrics=compute_metrics
)

#entrenar

trainer.train()

#guardar modelo

trainer.save_model("./model/goemotions_model")
tokenizer.save_pretrained("./model/goemotions_model")