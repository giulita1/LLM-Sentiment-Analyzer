# Emotion Classification API (DistilBERT + GoEmotions)

This project is a **multi-label emotion classification system** built using a transformer-based model.  
It analyzes text and predicts the emotional content of a sentence.

The system is trained on the **GoEmotions dataset** and deployed through a **FastAPI backend** for real-time predictions.

## Features

- Multi-label emotion detection
- Transformer-based NLP model
- API for real-time inference
- Built with Hugging Face Transformers
- Based on Google's GoEmotions dataset

The model can detect the following emotions:

- joy
- sadness
- anger
- fear
- surprise
- neutral

## Technologies Used

- **Python**
- **PyTorch**
- **Hugging Face Transformers**
- **Hugging Face Datasets**
- **FastAPI**
- **DistilBERT**

## Dataset

The model is trained on the **GoEmotions dataset**, created by Google Research.

It contains:

- 58k Reddit comments
- 27 emotion labels

In this project, the dataset is **filtered to six main emotions** and converted into a **multi-label format** using a multi-hot encoding.

## Model

The system uses:

DistilBERT

A lightweight transformer architecture derived from BERT that provides strong NLP performance with lower computational cost.

The model is fine-tuned using:

- Binary Cross Entropy Loss
- Multi-label classification
- Sigmoid activation for predictions

