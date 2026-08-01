import re

def analyze_sentiment(message):
    """
    Improved rule-based sentiment analysis.
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