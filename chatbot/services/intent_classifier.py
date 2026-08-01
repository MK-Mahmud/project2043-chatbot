import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "intent_model.pkl")

model = joblib.load(MODEL_PATH)


import re

def classify_intent(message):

    message = message.strip()

    # Too short
    if len(message) < 3:
        return "UNKNOWN"

    # Only symbols or numbers
    if not re.search(r"[A-Za-z]", message):
        return "UNKNOWN"

    # Single meaningless word
    words = message.split()

    if len(words) == 1 and len(words[0]) > 12:
        return "UNKNOWN"

    prediction = model.predict([message])

    return prediction[0]