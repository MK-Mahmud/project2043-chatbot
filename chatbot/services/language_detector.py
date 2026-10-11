import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "language_model.pkl")

# The trained model is a TF-IDF (character n-gram) + LinearSVC
# classifier, trained on 600 labelled banking messages (300 English,
# 300 Hausa) -- see chatbot/train_language.py. It reached 100% accuracy
# on a held-out 20% test split.
_model = joblib.load(MODEL_PATH)

# Kept as a lightweight fallback for extremely short inputs (1-2
# characters, stray punctuation, etc.) where the classifier has too
# little text to work with.
_HAUSA_KEYWORDS = {
    "ina", "yaya", "rance", "banki", "bude", "asusu", "sannu",
    "barka", "taimako", "don", "allah", "kudi", "katin", "akwai",
    "zan", "bukatar", "na", "dina", "min",
}


def detect_language(message):
    """
    Detect whether a message is written in English or Hausa.

    Uses a trained TF-IDF + LinearSVC classifier as the primary
    method. Falls back to keyword matching only when the message is
    too short for the classifier to make a reliable prediction.
    """

    message = message.strip()

    if len(message) < 3:
        words = message.lower().split()
        if any(word in _HAUSA_KEYWORDS for word in words):
            return "HAUSA"
        return "ENGLISH"

    prediction = _model.predict([message])[0]

    return "HAUSA" if prediction == "Hausa" else "ENGLISH"
