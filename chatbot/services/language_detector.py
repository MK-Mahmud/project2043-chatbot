def detect_language(message):
    """
    Detect whether a message is written primarily
    in Hausa or English using keyword matching.
    """

    message = message.lower()

    words = message.split()

    hausa_keywords = {
        "ina",
        "yaya",
        "rance",
        "banki",
        "bude",
        "asusu",
        "sannu",
        "barka",
        "taimako",
        "don",
        "allah",
        "kudi",
        "katin",
        "akwai",
        "zan",
        "bukatar",
        "na",
        "dina",
        "min"
    }

    for word in words:
        if word in hausa_keywords:
            return "HAUSA"

    return "ENGLISH"