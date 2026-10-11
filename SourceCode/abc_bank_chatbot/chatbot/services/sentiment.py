def analyze_sentiment(message):

    message = message.lower()

    positive_words = [
        "thank",
        "thanks",
        "good",
        "great",
        "excellent",
        "happy"
    ]

    negative_words = [
        "angry",
        "bad",
        "blocked",
        "problem",
        "complaint",
        "hate"
    ]

    for word in positive_words:
        if word in message:
            return "Positive"

    for word in negative_words:
        if word in message:
            return "Negative"

    return "Neutral"