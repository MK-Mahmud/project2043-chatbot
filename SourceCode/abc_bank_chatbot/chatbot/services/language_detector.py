def detect_language(message):

    message = message.lower()

    hausa_keywords = [
        "ina",
        "yaya",
        "ta",
        "rance",
        "banki",
        "bude",
        "asusu"
    ]

    for word in hausa_keywords:
        if word in message:
            return "HAUSA"

    return "ENGLISH"