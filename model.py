from transformers import pipeline


class SmartTextAI:

    def __init__(self):

        self.sentiment_model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def analyze(self, text):

        result = self.sentiment_model(text)[0]

        label = result["label"]
        confidence = result["score"]

        return label, confidence