"""
Trains a text classification model to detect whether a customer
message is written in English or Hausa.

Reuses the 'language' column already present in the intent-classification
dataset (banking_intents.csv), which contains 300 labelled English
messages and 300 labelled Hausa messages.
"""

import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==========================
# Load Dataset
# ==========================

data = pd.read_csv("chatbot/datasets/banking_intents.csv")

X = data["text"]
y = data["language"]

# ==========================
# Split Dataset
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================
# Build Model
# ==========================
# Character n-grams (rather than word n-grams) are used because they
# capture Hausa-specific spelling patterns (e.g. diacritics, letter
# combinations) even on short messages, which word-level features
# struggle with when the input is only 2-3 words long.

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            analyzer="char_wb",
            ngram_range=(2, 4),
        )
    ),
    (
        "classifier", LinearSVC()
    )
])

# ==========================
# Train Model
# ==========================

model.fit(X_train, y_train)

# ==========================
# Evaluation
# ==========================

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n==============================")
print("LANGUAGE DETECTION MODEL TRAINED")
print("==============================")

print(f"Total Samples : {len(data)}")
print(f"Training Data : {len(X_train)}")
print(f"Testing Data  : {len(X_test)}")

print("\nAccuracy")
print(f"{accuracy*100:.2f}%")

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

# ==========================
# Save Model
# ==========================

joblib.dump(model, "chatbot/language_model.pkl")

print("\nModel saved successfully.")
