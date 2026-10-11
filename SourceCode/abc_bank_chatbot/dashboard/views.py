from django.shortcuts import render
from chatbot.models import ChatHistory, UnansweredQuery


def dashboard_home(request):

    total_chats = ChatHistory.objects.count()

    positive = ChatHistory.objects.filter(
        sentiment="Positive"
    ).count()

    negative = ChatHistory.objects.filter(
        sentiment="Negative"
    ).count()

    english = ChatHistory.objects.filter(
        language="ENGLISH"
    ).count()

    hausa = ChatHistory.objects.filter(
        language="HAUSA"
    ).count()

    unanswered = UnansweredQuery.objects.count()

    context = {
        "total_chats": total_chats,
        "positive": positive,
        "negative": negative,
        "english": english,
        "hausa": hausa,
        "unanswered": unanswered,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )

# Create your views here.
