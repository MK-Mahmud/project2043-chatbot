import re

"""
Rule-based sentiment analysis.

An ML alternative (TF-IDF + Naive Bayes / LinearSVC, see
chatbot/train_sentiment.py) was trained and evaluated on a
120-example, 3-class labelled dataset. It reached only ~60%
cross-validated accuracy -- too little labelled data for a 3-class
text classifier to reliably beat a curated keyword list. The
rule-based approach below reached 69.2% on the same data, so it is
used in production. See chatbot/ai/evaluate_sentiment.py for the
side-by-side comparison. Retraining the ML model on a larger, more
varied dataset is listed as future work.
"""


def analyze_sentiment(message):
    """
    Rule-based sentiment analysis using curated positive/negative
    keyword lists. Returns "Positive", "Negative", or "Neutral".
    """

    # Remove punctuation
    message = re.sub(r"[^\w\s]", "", message.lower())

    words = message.split()

    positive_words = {
        "thank",
        "thanks",
        "thankyou",
        "good",
        "great",
        "excellent",
        "happy",
        "nice",
        "wonderful",
        "awesome",
        "perfect",
        "helpful",
        "satisfied",
        "appreciate",
        "amazing",
        "fantastic",
        "love",
        "brilliant",
        "best",
        "beautiful",
    }

    negative_words = {
        "angry",
        "bad",
        "blocked",
        "problem",
        "complaint",
        "hate",
        "failed",
        "failure",
        "error",
        "delay",
        "slow",
        "frustrated",
        "disappointed",
        "unable",
        "rejected",
        "terrible",
        "awful",
        "poor",
        "worst",
        "useless",
    }

    positive_score = sum(word in positive_words for word in words)
    negative_score = sum(word in negative_words for word in words)

    if positive_score > negative_score:
        return "Positive"

    if negative_score > positive_score:
        return "Negative"

    return "Neutral"
