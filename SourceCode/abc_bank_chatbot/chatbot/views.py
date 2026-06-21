from django.shortcuts import render
from .models import (
    Intent,
    KnowledgeBase,
    ChatHistory,
    UnansweredQuery
)
from .services.intent_classifier import classify_intent
from .services.language_detector import detect_language
from .services.sentiment import analyze_sentiment


def home(request):

    response = ""

    if request.method == "POST":

        message = request.POST.get("message")

        language = detect_language(message)
        sentiment = analyze_sentiment(message)

        detected_intent = classify_intent(message)

        try:

            intent = Intent.objects.get(
                intent_name=detected_intent
            )

            kb = KnowledgeBase.objects.filter(
                intent=intent
            ).first()

            if kb:

                if language == "HAUSA":
                    response = kb.answer_ha
                else:
                    response = kb.answer_en

            else:
                response = "No response available."

        except Intent.DoesNotExist:

            UnansweredQuery.objects.create(
                question=message,
                language=language
            )

            if language == "HAUSA":
                response = (
                    "Yi hakuri, ban gane tambayarka ba. "
                    "Za a duba ta daga baya."
                )
            else:
                response = (
                    "Sorry, I could not understand your request. "
                    "Your question has been saved for review."
                )

        ChatHistory.objects.create(
            message=message,
            response=response,
            language=language,
            sentiment=sentiment
        )

    return render(
        request,
        "chatbot/home.html",
        {"response": response}
    )