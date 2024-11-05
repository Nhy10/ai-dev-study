# model/model.py
from transformers import BertTokenizer, BertForSequenceClassification
import torch

class SentimentModel:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
        self.model.eval()

    def predict(self, text): # input 문장에 대해 긍정/부정을 판단하여 리턴하는 부분.
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits # 1 또는 0으로 이진 분류
        predicted_class = torch.argmax(logits, dim=1).item()
        return "positive" if predicted_class == 1 else "negative"