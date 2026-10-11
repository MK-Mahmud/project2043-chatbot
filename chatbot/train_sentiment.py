import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

data = pd.read_csv(
    "chatbot/datasets/sentiment_dataset_expanded.csv"
)

X = data["text"]
y = data["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1,2),
            stop_words="english"
        )
    ),
    (
        "classifier",
        MultinomialNB()
    )
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("="*35)
print("SENTIMENT MODEL TRAINED")
print("="*35)

print(
    "Accuracy:",
    round(
        accuracy_score(
            y_test,
            predictions
        )*100,
        2
    ),
    "%"
)

print()

print(
    classification_report(
        y_test,
        predictions
    )
)

print(
    confusion_matrix(
        y_test,
        predictions
    )
)

joblib.dump(
    model,
    "chatbot/sentiment_model.pkl"
)

print()
print("Model saved successfully.")