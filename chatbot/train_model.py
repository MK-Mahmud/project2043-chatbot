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
y = data["intent"]

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

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1,2),
        )
    ),
    (
        ("classifier", LinearSVC())
    )
])

# ==========================
# Train Model
# ==========================

model.fit(X_train, y_train)

# ==========================
# Predictions
# ==========================

predictions = model.predict(X_test)

# ==========================
# Evaluation
# ==========================

accuracy = accuracy_score(y_test, predictions)

print("\n==============================")
print("MODEL TRAINED SUCCESSFULLY")
print("==============================")

print(f"Total Samples : {len(data)}")
print(f"Training Data : {len(X_train)}")
print(f"Testing Data  : {len(X_test)}")
print(f"Total Intents : {len(data.intent.unique())}")

print("\nAccuracy")

print(f"{accuracy*100:.2f}%")

print("\nClassification Report")

print(classification_report(y_test, predictions))

print("\nConfusion Matrix")

print(confusion_matrix(y_test, predictions))

# ==========================
# Save Model
# ==========================

joblib.dump(model, "chatbot/intent_model.pkl")

print("\nModel saved successfully.")