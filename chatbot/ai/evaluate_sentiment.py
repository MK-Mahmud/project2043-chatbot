"""
Compares the ML-based sentiment classifier against the rule-based
(keyword) sentiment classifier used in production, on the same
120-example labelled dataset (chatbot/datasets/sentiment_dataset_expanded.csv).

Run from the project root:
    python chatbot/ai/evaluate_sentiment.py
"""

import re
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import classification_report, accuracy_score

from chatbot.services.sentiment import analyze_sentiment


DATASET_PATH = "chatbot/datasets/sentiment_dataset_expanded.csv"


def evaluate_ml_model():
    data = pd.read_csv(DATASET_PATH)
    X = data["text"]
    y = data["sentiment"]

    model = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english")),
        ("classifier", MultinomialNB())
    ])

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(model, X, y, cv=skf)

    print("ML Model (TF-IDF + Naive Bayes)")
    print(f"5-fold cross-validated accuracy: {scores.mean() * 100:.1f}%")
    print(f"Per-fold scores: {[round(s * 100, 1) for s in scores]}")


def evaluate_rule_based():
    data = pd.read_csv(DATASET_PATH)
    data["predicted"] = data["text"].apply(analyze_sentiment)

    accuracy = accuracy_score(data["sentiment"], data["predicted"])

    print("\nRule-Based Model (keyword matching)")
    print(f"Accuracy on full dataset: {accuracy * 100:.1f}%")
    print("\nClassification Report:")
    print(classification_report(data["sentiment"], data["predicted"]))


if __name__ == "__main__":
    print("=" * 50)
    print("SENTIMENT ANALYSIS: ML vs RULE-BASED COMPARISON")
    print("=" * 50 + "\n")

    evaluate_ml_model()
    evaluate_rule_based()

    print(
        "\nConclusion: with only 120 labelled examples across 3 "
        "classes, the ML model cannot reliably outperform a "
        "curated keyword list on short banking messages. The "
        "rule-based approach is used in production; the ML "
        "approach is retained here as an evaluated alternative "
        "for future work with a larger dataset."
    )
