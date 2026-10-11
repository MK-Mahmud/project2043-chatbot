import re


def format_response(intent, answer):
    """
    Normalize a knowledge base answer before it is sent to the customer.

    Knowledge base answers are entered by administrators through plain
    text fields, so this collapses stray whitespace/line breaks that can
    creep in during data entry, keeping replies consistent regardless of
    how they were typed.
    """

    if not answer:
        return answer

    # Collapse repeated whitespace (including newlines) into single spaces
    answer = re.sub(r"\s+", " ", answer).strip()

    return answer
