def classify_intent(message):

    message = message.lower()

    account_keywords = [
    "account",
    "open account",
    "create account",
    "register",
    "bude account",
    "bude asusu",
    "asusu"
]

    loan_keywords = [
    "loan",
    "borrow",
    "credit",
    "finance",
    "rance"
]

    card_keywords = [
        "atm",
        "card",
        "debit card",
        "blocked card"
    ]

    for word in account_keywords:
        if word in message:
            return "ACCOUNT_OPENING"

    for word in loan_keywords:
        if word in message:
            return "LOAN_INQUIRY"

    for word in card_keywords:
        if word in message:
            return "CARD_SERVICE"

    return "UNKNOWN"