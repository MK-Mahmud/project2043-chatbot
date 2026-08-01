def format_response(intent, response):

    title = intent.replace("_", " ").title()

    formatted = f"""
🏦 {title}

────────────────────────────

{response}

────────────────────────────

Is there anything else I can help you with?

• 💳 ATM / Debit Card

• 💰 Loan Services

• 📱 Mobile Banking

• 🏦 Branch Locations
"""

    return formatted