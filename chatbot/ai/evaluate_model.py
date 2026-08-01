import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score
)

# Load dataset
data = pd.read_csv("chatbot/datasets/banking_intents.csv")

X = data["text"]
y = data["intent"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Build pipeline
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            stop_words="english"
        )
    ),
    ("classifier", MultinomialNB())
])

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("\n========== MODEL EVALUATION ==========\n")

print("Accuracy:")
print(f"{accuracy_score(y_test, predictions):.2%}")

print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, predictions))